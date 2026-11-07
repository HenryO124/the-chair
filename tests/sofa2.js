// Nothing may be painted across Reveal.
//
// On the one-page quiz layout (`@media (min-width:860px) and
// (min-height:620px)`) the picture wall is `flex:1 1 auto` with a
// `min-height:48vh` floor, and the question, the answers and the player
// chips are every one of them `flex:0 0 auto`. On a screen shorter than
// about a thousand pixels the five of them want more height than the stage
// has; the floor stops the picture handing any of it back; the chips spill
// out of the bottom of the stage and land on top of the Reveal button.
// 1366x768 and 1920x900 both did it, by 30 to 45 pixels.
//
// A host who cannot see or hit Reveal cannot run the round, so this walks
// the television and laptop shapes a room actually uses and asserts that
// nothing from the scoreboard touches that button, and that the button is
// on the screen at all.
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

const SHAPES=[[1920,1080,'a television'],[1920,900,'a television in a window'],
              [1366,768,'a laptop'],[1600,900,'a laptop'],[2560,1440,'a big television'],
              [1280,720,'the smallest television']];

// Closest Wins and Point the Finger, in their own tab: a stage squeezed into
// a 16:9 box is a question nobody in the room can read.
async function p2(b,base,w,h){
  const p=await b.newPage({viewport:{width:w,height:h}});
  const bad=[];
  try{
    await p.goto(base);await p.waitForTimeout(2400);
    try{await p.click('#intro-skip',{timeout:1500})}catch(e){}
    await p.evaluate(()=>{try{S.lang='fi'}catch(e){};show('s-setup')});
    await p.waitForTimeout(1200);
    for(const g of ['near','finger']){
      const r=await p.evaluate(game=>{
        const bank=game==='near'?(typeof NEAR!=='undefined'&&NEAR):(typeof FINGERS!=='undefined'&&FINGERS);
        if(!bank||!bank.length)return null;
        S.game=game;S.players=[];
        ['Henkka','Mia','Jussi','Anna-Liisa','Pekka','Olli'].forEach((n,i)=>
          S.players.push({id:i,name:n,icon:i,score:i+1,pid:i?'p'+i:undefined}));
        Q.deck=new Array(10);Q.round=2;Q.current=bank[0];Q.revealed=false;Q.on=true;
        if(game==='near')Q.guesses={};
        else{Q.votes={};Q.options=S.players.slice(0,4).map(x=>x.id)}
        show('s-quiz');drawQuiz();try{fitScreen()}catch(e){}
        const wall=document.querySelector('#s-quiz .videowall');
        const sw=document.querySelector('#s-quiz .screenwrap');
        if(!wall||!sw||!wall.offsetParent)return {skip:true};
        return {wall:Math.round(wall.getBoundingClientRect().width),
                wrap:Math.round(sw.getBoundingClientRect().width)};
      },g);
      if(!r||r.skip)continue;
      if(r.wall>0&&r.wrap<r.wall-2)
        bad.push(g+' is squeezed into a '+r.wrap+'px box inside a '+r.wall
          +'px stage — it has no video to put in one');
    }
  }finally{await p.close()}
  return bad;
}

(async()=>{
  const probs=[];
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/'+path.basename(BUNDLE);
  const b=await chromium.launch();
  for(const [w,h,what] of SHAPES){
    const p=await b.newPage({viewport:{width:w,height:h}});
    await p.goto(base);
    await p.waitForTimeout(2400);
    try{await p.click('#intro-skip',{timeout:1500})}catch(e){}
    await p.evaluate(()=>{try{S.lang='fi'}catch(e){};show('s-setup')});
    await p.waitForTimeout(1200);     // the question banks arrive on their own
    const m=await p.evaluate(()=>{
      if(typeof TRIVIA==='undefined'||!TRIVIA.length)return {noBank:true};
      S.game='trivia';S.players=[];
      ['Henkka','Mia','Jussi','Anna-Liisa','Pekka','Olli','Riikka','Kristiina']
        .forEach((n,i)=>S.players.push({id:i,name:n,icon:i,score:i+1,pid:i?'p'+i:undefined}));
      const r=TRIVIA[0];
      Q.deck=new Array(15);Q.round=4;Q.current=r;Q.qid='';
      Q.options=[r[3],r[2],r[4],r[5]];Q.correct=1;Q.answers={1:0,2:1};
      Q.revealed=false;Q.on=true;
      show('s-quiz');drawQuiz();try{dressUI()}catch(e){}
      const n=document.getElementById('q-next');
      if(!n||!n.offsetParent)return {noButton:true};
      const nb=n.getBoundingClientRect();
      const lap=[];
      document.querySelectorAll('#s-quiz .qsc').forEach(c=>{
        if(!c.offsetParent)return;
        const r2=c.getBoundingClientRect();
        if(r2.left<nb.right&&r2.right>nb.left&&r2.top<nb.bottom&&r2.bottom>nb.top)
          lap.push(c.textContent.trim().slice(0,16)+' by '+Math.round(
            Math.min(r2.bottom,nb.bottom)-Math.max(r2.top,nb.top))+'px');
      });
      return {lap,off:Math.round(nb.bottom-document.documentElement.clientHeight),
        gap:Math.round(nb.top-document.getElementById('q-scores').getBoundingClientRect().bottom)};
    });
    // ---- and nothing but a record is squeezed into a 16:9 box ----
    // fitScreen() used to ask isAsking(), so Closest Wins got a box it had
    // nothing to put in: on a television its wall is 1680x96 and the box
    // inside it was 171x96, which wraps the question into a column two
    // words wide and prints it across the counter and the chips.
    const box=await p2(b,base,w,h);
    (box||[]).forEach(x=>probs.push(w+'x'+h+' ('+what+'): '+x));

    if(m.noBank)probs.push(w+'x'+h+': the question bank never arrived — nothing was measured');
    else if(m.noButton)probs.push(w+'x'+h+': there is no Reveal button on the quiz');
    else{
      if(m.lap&&m.lap.length)
        probs.push(w+'x'+h+' ('+what+'): the scoreboard is painted across Reveal — '+m.lap.join(', '));
      if(m.off>0)probs.push(w+'x'+h+' ('+what+'): Reveal is '+m.off+'px below the bottom of the screen');
    }
    await p.close();
  }
  await b.close();srv.close();
  console.log(probs.length?'FAIL:':'ok - Reveal is on the screen and nothing is painted across it');
  probs.forEach(x=>console.log('  x '+x));
  process.exit(probs.length?1:0);
})();
