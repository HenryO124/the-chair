// Twelve phones and a television, on a real broker.
//
// tests/room.js replaces window.mqtt with a bus between two pages, so it proves
// the game logic and nothing about the network. This one runs an actual MQTT
// broker on this machine, serves the page with its broker list pointed at it,
// and opens a television plus as many phones as asked for. The page's own
// mqtt.js does the connecting, the subscribing and the publishing: real
// WebSocket frames, real retained messages, real client ids.
//
// What it still does not prove: that the three public brokers behave the same
// under twelve clients, and that a phone on household wifi gets through at all.
// Only the house can answer that, with real phones, before the guests arrive.
//
//   node tests/crowd.js          12 phones
//   node tests/crowd.js 20       twenty
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const PHONES=parseInt(process.argv[2]||'12',10);
const {chromium}=require('playwright');
const http=require('http'),fs=require('fs'),url=require('url'),WS=require('ws');

const probs=[];
const note=s=>console.log('  '+s);

// ---------------------------------------------------------------- the broker
const Aedes=require('aedes').Aedes||require('aedes').default||require('aedes');
const aedes=new Aedes();
const brokerHttp=http.createServer();
const wss=new WS.Server({server:brokerHttp,handleProtocols:()=>'mqtt'});
let connected=0,published=0;
wss.on('connection',sock=>{
  connected++;
  aedes.handle(WS.createWebSocketStream(sock));
});
aedes.on('publish',p=>{if(p&&p.topic&&p.topic.indexOf('$SYS')!==0)published++});

// ------------------------------------------------------------- the page host
// The page ships with three public brokers hard-coded. Rewrite that one line on
// the way out rather than keeping a test hook in the shipped file.
let brokerPort=0;
const srv=http.createServer((q,r)=>{
  const f=path.join(ROOT,decodeURIComponent(url.parse(q.url).pathname.split('?')[0]));
  fs.readFile(f,(e,d)=>{
    if(e){r.writeHead(404);r.end();return}
    let body=d;
    if(/index\.html$/.test(f)){
      const s=d.toString('utf8');
      const out=s.replace(/const BROKERS=\[[^\]]*\];/,
        "const BROKERS=['ws://127.0.0.1:"+brokerPort+"/mqtt'];");
      if(out===s){probs.push('could not point the page at the local broker');}
      body=Buffer.from(out,'utf8');
    }
    r.writeHead(200,{'content-type':/\.js$/.test(f)?'text/javascript':'text/html'});
    r.end(body);
  });
});

const NAMES=['Mia','Eero','Aino','Väinö','Sofia','Oskari','Helmi','Leevi','Iida',
             'Niilo','Venla','Onni','Sanni','Elias','Peppi','Taneli','Kerttu',
             'Aarne','Vilma','Jalmari'];

(async()=>{
  await new Promise(r=>brokerHttp.listen(0,'127.0.0.1',r));
  brokerPort=brokerHttp.address().port;
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/index.html';
  note('broker on 127.0.0.1:'+brokerPort+', page on '+base);

  const b=await chromium.launch();
  // A phone opens the invitation link itself, hash and all, exactly as it would
  // after scanning the QR: followInvitation() runs at boot and does the dialling.
  const open=async(tag,viewport,hash)=>{
    const ctx=await b.newContext({viewport});
    const p=await ctx.newPage();
    p.on('pageerror',e=>probs.push(tag+' JS error: '+String(e).slice(0,120)));
    await p.goto(base+(hash||''));
    await p.waitForTimeout(1200);
    try{await p.click('#intro-skip',{timeout:400})}catch(e){}
    return {p,ctx,tag};
  };
  // Wait for a page to have a live broker connection rather than guessing at
  // a number of milliseconds; a real network is slower than a fake bus.
  const dialled=async(ph,ms)=>{
    const until=Date.now()+(ms||12000);
    while(Date.now()<until){
      if(await ph.p.evaluate(()=>!!(window.PARTY&&PARTY.client)))return true;
      await ph.p.waitForTimeout(150);
    }
    return false;
  };

  // ---- the television opens a room, over the real broker ----
  const tv=await open('television',{width:1600,height:900});
  await tv.p.evaluate(()=>{
    localStorage.setItem('thechair.lang','fi');
    S.lang='fi';S.game='trivia';S.len=5;S.cats=[];MYNAME='Henkka';
    try{MAX_CHAIRS=24}catch(e){}
    try{openModes('create')}catch(e){}
    try{pickGame('trivia')}catch(e){}
    try{openLobby()}catch(e){}
  });
  await tv.p.waitForTimeout(3000);
  const code=await tv.p.evaluate(()=>PARTY.code);
  const key=await tv.p.evaluate(()=>PARTY.key);
  const role=await tv.p.evaluate(()=>PARTY.role);
  if(!code||code.length!==6){
    console.log('FAIL:');
    console.log('  x the television never opened a room over a real broker (role '+role+')');
    probs.forEach(p=>console.log('  x '+p));
    process.exit(1);
  }
  note('room '+code+' is open, the television is '+role);

  // ---- the phones arrive, one after another, as they would in a kitchen ----
  const phones=[];
  const t0=Date.now();
  const hash='#'+code+(key?'-'+key:'');
  for(let i=0;i<PHONES;i++){
    const name=NAMES[i%NAMES.length]+(i>=NAMES.length?String(Math.floor(i/NAMES.length)+1):'');
    const ph=await open('phone '+(i+1),{width:390,height:844},hash);
    if(!await dialled(ph))probs.push(name+"'s phone never reached the broker");
    await ph.p.evaluate(n=>{
      const f=document.getElementById('join-name');if(f)f.value=n;
      const g=document.getElementById('join-go');if(g)g.click();
    },name);
    phones.push(ph);
  }
  await tv.p.waitForTimeout(4000);
  const joinSecs=((Date.now()-t0)/1000).toFixed(1);

  const seated=await tv.p.evaluate(()=>S.players.map(p=>p.name));
  note(seated.length+' of '+PHONES+' phones took a chair in '+joinSecs+'s');
  if(seated.length<PHONES)
    probs.push('only '+seated.length+' of '+PHONES+' phones are in the room: '+JSON.stringify(seated));

  // ---- one question, every phone answering at once ----
  await tv.p.evaluate(()=>{show('s-quiz');try{quizStart()}catch(e){}});
  await tv.p.waitForTimeout(2500);

  const asked=await tv.p.evaluate(()=>{
    const e=document.getElementById('q-screen');return e?(e.textContent||'').trim().slice(0,70):''});
  if(!asked)probs.push('the television is in the quiz but shows no question');
  else note('the television asks: '+asked);

  // every phone taps in the same second, which is what a room actually does
  const taps=await Promise.all(phones.map(async(ph,i)=>{
    try{
      return await ph.p.evaluate(n=>{
        const bs=[...document.querySelectorAll('#pad-quiz .qbtn')];
        if(!bs.length)return 'nothing to tap';
        bs[n%bs.length].click();
        return 'ok';
      },i);
    }catch(e){return 'threw: '+String(e).slice(0,60)}
  }));
  const mute=taps.map((t,i)=>t==='ok'?null:(i+1)+': '+t).filter(Boolean);
  if(mute.length)probs.push(mute.length+' phone(s) could not answer — '+mute.slice(0,4).join('; '));

  await tv.p.waitForTimeout(3500);
  const landed=await tv.p.evaluate(()=>Object.keys((window.Q&&Q.answers)||{}).length);
  note(landed+' of '+PHONES+' answers reached the television');
  if(landed<PHONES)probs.push('only '+landed+' of '+PHONES+' answers arrived');

  note(connected+' websocket connections, '+published+' messages through the broker');

  await b.close();srv.close();brokerHttp.close();aedes.close();

  if(probs.length){
    console.log('FAIL:');probs.forEach(p=>console.log('  x '+p));process.exit(1);
  }
  console.log('ok - '+PHONES+' phones joined one room over a real broker and all answered');
  process.exit(0);
})().catch(e=>{console.log('FAIL:');console.log('  x '+String(e).slice(0,400));process.exit(1)});
