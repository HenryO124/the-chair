// A real television and a real phone, in two browsers, for every game.
//
// Every other suite drives the phone by calling drawPad() directly, which is
// how Closest Wins shipped with no box to type a guess into and passed its own
// tests. This one joins a room with a code, takes a chair, reads what the phone
// actually shows, taps what a player would tap, and checks the answer arrives
// on the television. The broker is replaced by a bus between the two pages, so
// everything is exercised except the network itself.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const {chromium}=require('playwright');
const http=require('http'),fs=require('fs'),url=require('url');

const srv=http.createServer((q,r)=>{
  const f=path.join(ROOT,decodeURIComponent(url.parse(q.url).pathname.split('?')[0]));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end()}else{
    r.writeHead(200,{'content-type':/\.js$/.test(f)?'text/javascript':'text/html'});r.end(d)}})});

const matches=(filter,topic)=>{
  const f=filter.split('/'),t=topic.split('/');
  for(let i=0;i<f.length;i++){
    if(f[i]==='#')return true;
    if(f[i]==='+'){if(t[i]===undefined)return false;continue}
    if(f[i]!==t[i])return false;
  }
  return f.length===t.length;
};
function makeBus(){
  const subs=[],retained=new Map();
  return {
    async pub(topic,payload,retain){
      if(retain){ if(payload==='')retained.delete(topic); else retained.set(topic,payload) }
      for(const s of subs){
        if(!matches(s.filter,topic))continue;
        try{await s.page.evaluate(([t,p])=>window.__deliver&&window.__deliver(t,p),[topic,payload])}catch(e){}
      }
    },
    async sub(page,filter){
      subs.push({page,filter});
      for(const [t,p] of retained)
        if(matches(filter,t))
          try{await page.evaluate(([a,b])=>window.__deliver&&window.__deliver(a,b),[t,p])}catch(e){}
    },
    reset(){subs.length=0;retained.clear()}
  };
}
const FAKE_MQTT=`
window.mqtt={connect(){
  const handlers={};
  const api={options:{},
    on(ev,fn){(handlers[ev]=handlers[ev]||[]).push(fn);
      if(ev==='connect')setTimeout(()=>fn(),10);return api},
    subscribe(t,o,cb){(Array.isArray(t)?t:[t]).forEach(f=>window.__sub(f));
      if(typeof o==='function')o(null);else if(cb)cb(null);return api},
    unsubscribe(){return api},
    publish(t,p,o,cb){window.__pub(t,String(p==null?'':p),!!(o&&o.retain));
      if(typeof o==='function')o();else if(cb)cb();return api},
    end(){return api}};
  window.__deliver=(t,p)=>{(handlers.message||[]).forEach(fn=>{
    try{fn(t,{toString:()=>p,length:p.length})}catch(e){}})};
  return api;}};`;

const probs=[];
(async()=>{
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/index.html';
  const b=await chromium.launch();

  for(const game of ['near','finger','s10','trivia','tf','picture','artist']){
    const bus=makeBus();
    const open=async(tag,viewport)=>{
      const ctx=await b.newContext({viewport});
      const p=await ctx.newPage();
      p.on('pageerror',e=>probs.push(game+' '+tag+' JS error: '+String(e).slice(0,110)));
      await p.exposeFunction('__pub',(t,pl,r)=>bus.pub(t,pl,r));
      await p.exposeFunction('__sub',f=>bus.sub(p,f));
      await p.addInitScript(FAKE_MQTT);
      await p.goto(base);
      await p.waitForTimeout(1600);
      try{await p.click('#intro-skip',{timeout:500})}catch(e){}
      return {p,ctx};
    };
    const tv=await open('television',{width:1600,height:900});
    const ph=await open('phone',{width:390,height:844});

    await tv.p.evaluate(async g=>{
      localStorage.setItem('thechair.lang','fi');
      S.lang='fi';S.game=g;S.len=5;S.cats=[];MYNAME='Henkka';
      try{openModes('create')}catch(e){}
      try{pickGame(g)}catch(e){}
      await new Promise(r=>setTimeout(r,40));
      try{openLobby()}catch(e){}
    },game);
    await tv.p.waitForTimeout(1400);
    const code=await tv.p.evaluate(()=>PARTY.code);
    const key=await tv.p.evaluate(()=>PARTY.key);
    if(!code||code.length!==6){probs.push(game+': the room never opened');await tv.ctx.close();await ph.ctx.close();continue}

    await ph.p.evaluate(([c,k])=>{
      localStorage.setItem('thechair.lang','fi');
      location.hash='#'+c+(k?'-'+k:'');
      S.lang='fi';
      try{joinWithCode&&joinWithCode(c,k)}catch(e){}
    },[code,key]);
    await ph.p.waitForTimeout(800);
    await ph.p.evaluate(()=>{
      const n=document.getElementById('join-name');if(n)n.value='Mia';
      const g=document.getElementById('join-go');if(g)g.click();
    });
    await ph.p.waitForTimeout(1400);

    const seated=await tv.p.evaluate(()=>S.players.map(p=>p.name));
    if(!seated.includes('Mia'))probs.push(game+': the phone joined but took no chair — '+JSON.stringify(seated));

    await tv.p.evaluate(()=>{show('s-quiz');try{quizStart()}catch(e){}});
    await tv.p.waitForTimeout(1500);
    // The Short List is taken in turns, so a phone whose turn it is not has
    // nothing to tap and is right to show nothing. Hand the turn to the phone
    // before asking whether it can play.
    const turned=await tv.p.evaluate(()=>{
      if(typeof s10SetTurn!=='function'||typeof Q.turn==='undefined')return null;
      const guest=S.players.find(p=>p.pid);
      if(!guest)return null;
      s10SetTurn(guest.id);try{drawQuiz();publishStage()}catch(e){}
      return guest.name;
    });
    if(turned)await tv.p.waitForTimeout(1200);

    // what a player can actually tap or type, whatever the game calls it
    const can=await ph.p.evaluate(()=>{
      const live=e=>e&&!e.hidden&&e.offsetParent!==null&&!e.disabled;
      const inp=[...document.querySelectorAll('#s-chair input[type=text],#s-chair input:not([type]),#pad-near')].filter(live);
      const btn=[...document.querySelectorAll('#s-chair button')].filter(live)
        .filter(e=>!/leave|poistu|lähde|tauko/i.test(e.textContent||''));
      return {inputs:inp.length,buttons:btn.length,
        round:(document.getElementById('pad-round')||{textContent:''}).textContent.trim().slice(0,40)};
    });
    if(!can.inputs&&!can.buttons)
      probs.push(game+': THE PHONE HAS NOTHING TO ANSWER WITH');

    // answer the way that game is answered
    await ph.p.evaluate(()=>{
      const live=e=>e&&!e.hidden&&e.offsetParent!==null&&!e.disabled;
      const i=document.getElementById('pad-near');
      if(live(i)){i.value='42';i.dispatchEvent(new Event('input',{bubbles:true}));
        const lock=document.getElementById('pad-nearlock');if(lock)lock.click();return}
      const b=[...document.querySelectorAll('#s-chair button')].filter(live)
        .filter(e=>!/leave|poistu|lähde|tauko/i.test(e.textContent||''));
      if(b.length)b[0].click();
    });
    await tv.p.waitForTimeout(1400);

    const heard=await tv.p.evaluate(()=>{
      const n=o=>o?Object.keys(o).length:0;
      return n(Q.guesses)+n(Q.answers)+n(Q.votes)+((Q.cands||[]).filter(c=>c&&c.by).length);
    });
    if(!heard)probs.push(game+': THE ANSWER NEVER REACHED THE TELEVISION (phone had '
      +can.inputs+' fields, '+can.buttons+' buttons)');

    console.log('  '+game.padEnd(8)+'tuoli '+(seated.includes('Mia')?'ok':'EI')
      +(turned?'   vuoro: '+turned:'')
      +'   puhelin: '+can.inputs+' kenttää '+can.buttons+' nappia'
      +'   vastaus perillä: '+(heard?'ok':'EI')+'   "'+can.round+'"');
    await tv.ctx.close();await ph.ctx.close();
  }

  await b.close();srv.close();
  console.log(probs.length?'FAIL:':'ok - a phone joins, sees the game and answers it, in every game');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
})().catch(e=>{console.log('FAIL:');console.log('  x the harness fell over: '+e.message);process.exit(1)});
