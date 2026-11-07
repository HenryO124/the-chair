// The game menu may never be wider than the window it is in.
//
// `.home` was `minmax(240px,0.9fr) 2fr` and `.shelf` was
// `repeat(auto-fit,minmax(300px,1fr))`. Every one of those tracks has a floor
// it will not shrink below — an `fr` track's automatic minimum is its
// content's min-content, and the shelf's own minimum is a written-out 300px —
// so when the space for a track falls under its floor the track keeps the
// floor and the grid grows out past the right edge of the window. Whichever
// card is sitting at that edge is then sliced in half by it, which is exactly
// what the host kept photographing.
//
// This sweeps the menu across every width a television, a laptop, a tablet or
// a phone can present and asserts two things at each one: the document is not
// wider than the window, and no game card reaches past the window's right
// edge. On the unfixed page it fails from 300px to 314px, where the last card
// runs up to 16px past the edge.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
const {chromium}=require('playwright');
const http=require('http'),fs=require('fs'),url=require('url');
const T={'.html':'text/html','.js':'text/javascript','.txt':'text/plain','.json':'application/json'};
const srv=http.createServer((q,r)=>{
  const f=path.join(path.dirname(BUNDLE),decodeURIComponent(url.parse(q.url).pathname));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end()}
    else{r.writeHead(200,{'content-type':T[path.extname(f)]||'application/octet-stream'});r.end(d)}})});

const WIDTHS=[];
for(let w=280;w<=2600;w+=6)WIDTHS.push(w);
// the sizes a room actually meets, and the ones either side of where the
// shelf changes its mind about how many columns it wants
[300,306,314,320,360,390,414,768,820,1024,1100,1242,1274,1280,1366,1440,1536,
 1600,1698,1700,1702,1760,1800,1890,1905,1920,2000,2048,2560].forEach(w=>{
  if(WIDTHS.indexOf(w)<0)WIDTHS.push(w)});
WIDTHS.sort((a,b)=>a-b);

(async()=>{
  const probs=[];
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/'+path.basename(BUNDLE);
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1920,height:1000}});
  await p.goto(base);
  await p.waitForTimeout(2400);
  try{await p.click('#intro-skip',{timeout:1500})}catch(e){}
  // Finnish, because that is the language the room reads it in
  await p.evaluate(()=>{try{S.lang='fi';dressUI()}catch(e){};show('s-setup')});
  let cards=await p.evaluate(()=>
    [...document.querySelectorAll('#s-setup .gamecard')].filter(e=>e.offsetParent).length);
  if(cards<4)probs.push('only '+cards+' game cards are on the menu — this is not measuring anything');
  for(const w of WIDTHS){
    await p.setViewportSize({width:w,height:1000});
    const m=await p.evaluate(()=>{
      const de=document.documentElement;
      const sh=document.querySelector('#s-setup .shelf');
      const out=[];
      document.querySelectorAll('#s-setup .gamecard').forEach(c=>{
        if(!c.offsetParent)return;
        const r=c.getBoundingClientRect();
        if(r.right>de.clientWidth+0.5)
          out.push((c.querySelector('.gname')||{textContent:'?'}).textContent.trim()
            +' ends '+Math.round(r.right-de.clientWidth)+'px past the edge');
      });
      return {sw:de.scrollWidth,cw:de.clientWidth,out,
        cols:sh?getComputedStyle(sh).gridTemplateColumns.split(' ').length:0};
    });
    if(m.sw>m.cw+0.5)
      probs.push(w+'px: the menu is '+(m.sw-m.cw)+'px wider than the window'
        +(m.out.length?' — '+m.out[0]:''));
    else if(m.out.length)
      probs.push(w+'px: a card hangs off the right edge — '+m.out[0]);
    if(probs.length>6){probs.push('…and more');break}
  }
  await b.close();srv.close();
  console.log(probs.length?'FAIL:':'ok - the game menu fits its window at every width from 280 to 2600');
  probs.forEach(x=>console.log('  x '+x));
  process.exit(probs.length?1:0);
})();
