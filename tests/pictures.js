// The picture judging page, driven the way the house will drive it.
// Commons is not reachable from this container, so the pictures themselves are
// stood in for — that is precisely why this page exists, and precisely the
// thing it must not pretend to have checked.
const path=require("path"),fs=require('fs'),http=require('http'),url=require('url');
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const {chromium}=require('playwright');
const probs=[];
const srv=http.createServer((q,r)=>{
  const f=path.join(ROOT,decodeURIComponent(url.parse(q.url).pathname.split('?')[0]));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end()}else{
    r.writeHead(200,{'content-type':/\.json$/.test(f)?'application/json':
      /\.js$/.test(f)?'text/javascript':'text/html'});r.end(d)}})});
const PNG=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==','base64');

(async()=>{
  const cands=JSON.parse(fs.readFileSync(path.join(ROOT,'pic_candidates.json'),'utf8'));
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/pictures.html';
  const b=await chromium.launch();
  const ctx=await b.newContext({viewport:{width:1280,height:900}});
  const p=await ctx.newPage();
  p.on('pageerror',e=>probs.push('JS error: '+String(e).slice(0,130)));
  // every picture loads except the third, which is dead
  let dead=cands[2]?cands[2].u:'';
  await p.route('**commons.wikimedia.org/**',route=>{
    if(route.request().url()===dead)return route.fulfill({status:404,body:''});
    route.fulfill({status:200,contentType:'image/png',body:PNG});
  });
  await p.goto(base);
  await p.waitForTimeout(1500);

  const n=await p.evaluate(()=>CAND.length);
  console.log('  '+n+' candidates loaded');
  if(n!==cands.length)probs.push('the page sees '+n+' candidates, the file holds '+cands.length);

  const first=await p.evaluate(()=>({ask:document.getElementById('ask').textContent,
    ok:(document.querySelector('#ans .ok')||{}).textContent,
    n:document.querySelectorAll('#ans span').length,
    src:document.getElementById('shot').getAttribute('src')||''}));
  console.log('  first card: '+first.ask+'  ->  '+first.ok);
  if(!first.ask)probs.push('the card asks nothing');
  if(first.n!==4)probs.push('the card shows '+first.n+' answers, expected four');
  if(!first.ok)probs.push('the correct answer is not marked, so there is nothing to check against');
  if(first.src.indexOf('commons.wikimedia.org')<0)probs.push('the picture is not being fetched: '+first.src);

  // the dead one must be skipped, not put in front of a person
  await p.click('#yes'); await p.waitForTimeout(400);
  await p.click('#yes'); await p.waitForTimeout(900);
  const st=await p.evaluate(()=>({dead:dead.slice(),cur:cur&&cur.id,
                                  decided:Object.keys(decided).length}));
  console.log('  after two takes: '+st.decided+' decided, '+st.dead.length+' unreachable, now on '+st.cur);
  if(!st.dead.length)probs.push('a picture that would not load was still put in front of a person');
  if(st.cur===cands[2].id)probs.push('the page is sitting on the picture that will never load');

  await p.click('#no'); await p.waitForTimeout(400);
  await p.keyboard.press('ArrowRight'); await p.waitForTimeout(400);
  await p.keyboard.press('ArrowLeft'); await p.waitForTimeout(400);

  // a reload may not ask again about anything settled
  const seen=await p.evaluate(()=>Object.keys(decided));
  await p.reload(); await p.waitForTimeout(1500);
  const kept=await p.evaluate(()=>Object.keys(decided).length);
  if(kept!==seen.length)probs.push('a reload lost '+(seen.length-kept)+' decisions');
  const now=await p.evaluate(()=>cur&&cur.id);
  if(seen.indexOf(now)>=0)probs.push('after the reload it asked again about '+now);
  console.log('  a reload kept all '+kept+' decisions');

  // the output is what has to come back here
  await p.evaluate(()=>finish(true));
  await p.waitForTimeout(300);
  const out=await p.evaluate(()=>document.getElementById('out').value);
  let parsed=null;
  try{parsed=JSON.parse(out)}catch(e){probs.push('the text to paste back is not JSON')}
  if(parsed){
    if(!Array.isArray(parsed.take))probs.push('no list of taken pictures in the output');
    if(!Array.isArray(parsed.dead))probs.push('no list of unreachable pictures in the output');
    const ids=new Set(cands.map(c=>c.id));
    if((parsed.take||[]).some(k=>!ids.has(k)))probs.push('the output names a picture that is not a candidate');
    console.log('  output: '+(parsed.take||[]).length+' taken, '+(parsed.dead||[]).length+' unreachable');
  }
  console.log('  '+await p.evaluate(()=>document.getElementById('tally').textContent));

  await b.close();srv.close();
  if(probs.length){console.log('FAIL:');probs.forEach(x=>console.log('  x '+x));process.exit(1)}
  console.log('ok - one picture, one decision; an unreachable picture is counted and skipped');
  process.exit(0);
})().catch(e=>{console.log('FAIL:');console.log('  x '+String(e).slice(0,400));process.exit(1)});
