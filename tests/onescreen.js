// exactly one screen may be visible at a time, at every size
const {chromium}=require('playwright');
const http=require('http'),fs=require('fs'),path=require('path'),url=require('url');
const ROOT=process.env.CHAIR_ROOT||'/home/claude/the-chair';
const T={'.html':'text/html','.js':'text/javascript','.txt':'text/plain'};
const srv=http.createServer((q,r)=>{const f=path.join(ROOT,decodeURIComponent(url.parse(q.url).pathname));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end()}else{r.writeHead(200,{'content-type':T[path.extname(f)]||'application/octet-stream'});r.end(d)}})});
(async()=>{
  const probs=[];
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/index.html';
  const b=await chromium.launch();
  for(const [w,h,tag] of [[1920,1080,'tv'],[1366,768,'laptop'],[390,844,'phone']]){
    const p=await b.newPage({viewport:{width:w,height:h}});
    await p.goto(base);
    await p.waitForTimeout(2400);
    try{await p.click('#intro-skip',{timeout:1200})}catch(e){}
    for(const id of ['s-home','s-setup','s-lobby','s-quiz','s-chair','s-break','s-final']){
      const seen=await p.evaluate(s=>{
        show(s);
        return [...document.querySelectorAll('.screen')]
          .filter(e=>getComputedStyle(e).display!=='none')
          .map(e=>e.id);
      },id);
      if(seen.length!==1||seen[0]!==id)
        probs.push(tag+': on '+id+' the browser was showing '+(seen.join('+')||'nothing'));
    }
    await p.close();
  }
  await b.close();srv.close();
  console.log(probs.length?'FAIL:':'ok - one screen at a time, at every size');
  probs.forEach(x=>console.log('  x '+x));
  process.exit(probs.length?1:0);
})();
