// Can the room actually press the answers?
// Name the Artist once lost its video frame to a stylesheet rule meant for
// text-only questions; the player then sat on top of answers A and B and no
// jsdom suite could see it, because jsdom has no layout. This one asks a real
// browser what is under each button, in every game, on a television.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
const {chromium}=require('playwright');
const http=require('http'),fs=require('fs'),url=require('url');

const TYPES={'.html':'text/html','.js':'text/javascript','.mp3':'audio/mpeg','.txt':'text/plain'};
const server=http.createServer((req,res)=>{
  const f=path.join(ROOT,decodeURIComponent(url.parse(req.url).pathname));
  fs.readFile(f,(e,d)=>{
    if(e){res.writeHead(404);res.end('no');return}
    res.writeHead(200,{'content-type':TYPES[path.extname(f)]||'application/octet-stream'});
    res.end(d);
  });
});

(async()=>{
  const probs=[];
  await new Promise(r=>server.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+server.address().port+'/'+path.basename(BUNDLE);
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1920,height:1080}});
  p.on('pageerror',e=>probs.push('JS error: '+String(e.message).slice(0,120)));
  await p.goto(base);
  await p.waitForTimeout(2200);
  try{await p.click('#intro-skip',{timeout:1500})}catch(e){}
  await p.evaluate(()=>needBanks());
  // the bank chunk is a third of a megabyte; give it room on a slow machine
  for(let i=0;i<40&&!(await p.evaluate(()=>haveBanks()));i++)await p.waitForTimeout(250);
  if(!(await p.evaluate(()=>haveBanks())))probs.push('the question bank never arrived');

  for(const game of ['trivia','picture','tf','s10','artist']){
    const r=await p.evaluate(async(g)=>{
      S.game=g;S.lang='fi';
      S.players=[{id:0,name:'Henkka',score:0,night:0}];
      Q.on=false;Q.revealed=false;Q.round=0;Q.deck=[];Q.current=null;Q.cands=null;
      show('s-quiz');quizStart();
      await new Promise(r=>setTimeout(r,900));
      const btns=[...document.querySelectorAll('#q-options button')];
      const hidden=[];
      btns.forEach((btn,i)=>{
        const r=btn.getBoundingClientRect();
        if(r.width<40||r.height<20){hidden.push(i+':no size');return}
        if(r.bottom>innerHeight||r.top<0){hidden.push(i+':off screen');return}
        const el=document.elementFromPoint(r.left+r.width/2,r.top+r.height/2);
        if(el!==btn&&!btn.contains(el))
          hidden.push(i+':under '+(el?el.tagName+'.'+String(el.className).split(' ')[0]:'nothing'));
      });
      const stage=document.getElementById('q-stage');
      const wall=document.querySelector('#s-quiz .videowall');
      const next=document.getElementById('q-next').getBoundingClientRect();
      // the "a newer build is out" notice must not land on Reveal
      let banner=null;
      const nv=document.querySelector('.newver');
      if(nv){
        const was=nv.hidden; nv.hidden=false;
        const a=nv.getBoundingClientRect();
        banner=!(a.right<next.left||a.left>next.right||a.bottom<next.top||a.top>next.bottom);
        nv.hidden=was;
      }
      // two in three quiz questions have no picture, but some do, and then the
      // frame is right to be there. Ask the data, not the DOM: a picture that
      // fails to load still means this question was meant to have one.
      const hasPic=!!(typeof QIMG!=='undefined'&&QIMG[String(Q.qid)]);
      return {count:btns.length,hidden:hidden,hasPic:hasPic,bannerOnReveal:banner,
        wallH:wall?Math.round(wall.getBoundingClientRect().height):-1,
        centred:stage.className.includes('centred'),
        nextOnScreen:next.bottom<=innerHeight+1&&next.top>=0};
    },game);

    const want={trivia:4,picture:4,tf:2,s10:10,artist:4}[game];
    if(r.count!==want)probs.push(game+': '+r.count+' answers on screen, expected '+want);
    if(r.hidden.length)probs.push(game+': answers nobody can press — '+r.hidden.join(', '));
    if(!r.nextOnScreen)probs.push(game+': the Reveal button is off the screen');
    if(r.bannerOnReveal)probs.push(game+': the new-build notice sits on top of Reveal');
    // a record and a picture need their frame; a written question must not keep one
    if(game==='artist'&&r.wallH<200)
      probs.push('artist: the stage collapsed to '+r.wallH+'px, so the video has nowhere to go');
    if(game==='picture'&&r.wallH<200)
      probs.push('picture: the stage collapsed to '+r.wallH+'px, so the picture has nowhere to go');
    if(r.hasPic&&r.wallH<200)
      probs.push(game+': this one has a picture and the frame collapsed to '+r.wallH+'px');
    if((game==='trivia'||game==='tf')&&!r.hasPic&&!r.centred)
      probs.push(game+': a question with nothing to show still reserves a picture frame');
  }

  await b.close();
  server.close();
  console.log(probs.length?'FAIL:':'ok - every game: the answers are on the screen and nothing covers them');
  probs.forEach(x=>console.log('  x '+x));
  process.exit(probs.length?1:0);
})();
