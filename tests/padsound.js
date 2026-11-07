// A phone cannot start a video with the sound on unless a finger asked for it.
//
// The embed went onto the phone with autoplay=1 and mute=0 on the very first
// record. A mobile browser does not turn that down politely — it refuses the
// whole thing, so the record never played at all and the phone sat silent with
// a button that claimed the sound was on.
const path=require("path"),fs=require('fs'),http=require('http'),url=require('url');
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const {chromium}=require('playwright');
const probs=[];
const srv=http.createServer((q,r)=>{
  const f=path.join(ROOT,decodeURIComponent(url.parse(q.url).pathname.split('?')[0]));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end()}else{
    r.writeHead(200,{'content-type':/\.js$/.test(f)?'text/javascript':'text/html'});r.end(d)}})});

(async()=>{
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/index.html';
  const b=await chromium.launch();
  const ctx=await b.newContext({viewport:{width:390,height:844}});
  const p=await ctx.newPage();
  p.on('pageerror',e=>probs.push('JS error: '+String(e).slice(0,120)));
  // nothing may actually reach YouTube from a test
  await p.route('**youtube-nocookie.com/**',r=>r.fulfill({status:200,contentType:'text/html',body:'<i></i>'}));
  await p.goto(base);
  await p.waitForTimeout(1800);
  try{await p.click('#intro-skip',{timeout:500})}catch(e){}

  const paint=async()=>p.evaluate(()=>{
    // the pad lives inside the join screen; show it so the player has a size
    try{show('s-chair')}catch(e){}
    const cp=document.getElementById('chair-pad');if(cp)cp.hidden=false;
    const jf=document.getElementById('join-form');if(jf)jf.hidden=true;
    padVid='';
    drawPadScreen({phase:'live',game:'artist',vid:'dQw4w9WgXcQ',round:1,players:[],remote:true});
    const f=document.querySelector('#pad-screen iframe');
    const tap=document.querySelector('#pad-screen .tapsound');
    const on=document.getElementById('pad-sound2');
    return {src:f?f.getAttribute('src'):'', label:(tap||on||{textContent:''}).textContent.trim(),
            wants:!!tap};
  });

  // ---- first record on a phone that has never tapped ----
  let r=await paint();
  if(!r.src)probs.push('the phone never got a player at all');
  if(/mute=0/.test(r.src))
    probs.push('the first record is handed to the phone unmuted — the browser will refuse it outright');
  if(!/mute=1/.test(r.src))probs.push('the embed does not say whether it is muted: '+r.src.slice(0,90));
  if(!r.wants)probs.push('nothing on the phone invites the tap that would turn the sound on');
  // the invitation has to be the size of a thumb, not a footnote
  const big=await p.evaluate(()=>{const t=document.querySelector('#pad-screen .tapsound');
    if(!t)return null;const b=t.getBoundingClientRect();return {w:Math.round(b.width),h:Math.round(b.height)}});
  if(big&&(big.w<180||big.h<44))
    probs.push('the invitation is only '+big.w+'x'+big.h+' — nobody will find it');
  console.log('  before any tap: '+(/mute=1/.test(r.src)?'muted':'LOUD')+', button says "'+r.label+'"');

  // ---- one tap, and it plays with sound ----
  await p.evaluate(()=>document.getElementById('pad-sound').click());
  await p.waitForTimeout(250);
  r=await paint();
  if(!/mute=0/.test(r.src))probs.push('after the tap the record is still muted: '+r.src.slice(0,90));
  if(r.wants)probs.push('the phone is still asking for a tap it has already had');
  console.log('  after one tap:  '+(/mute=0/.test(r.src)?'sound on':'STILL MUTED')+', button says "'+r.label+'"');

  // ---- and it is remembered, so it is one tap a night, not one a record ----
  const p2=await ctx.newPage();
  await p2.route('**youtube-nocookie.com/**',q=>q.fulfill({status:200,contentType:'text/html',body:'<i></i>'}));
  await p2.goto(base);
  await p2.waitForTimeout(1600);
  try{await p2.click('#intro-skip',{timeout:500})}catch(e){}
  const again=await p2.evaluate(()=>{
    padVid='';
    drawPadScreen({phase:'live',game:'artist',vid:'dQw4w9WgXcQ',round:2,players:[],remote:true});
    const f=document.querySelector('#pad-screen iframe');
    return f?f.getAttribute('src'):'';
  });
  if(!/mute=0/.test(again))probs.push('the phone forgot it had been given permission: '+again.slice(0,90));
  else console.log('  a later page on the same phone: sound on, no second tap needed');

  // ---- in a shared room the phone must say why it is silent ----------------
  const room=await p.evaluate(()=>{
    padVid='';
    drawPadScreen({phase:'live',game:'artist',vid:'dQw4w9WgXcQ',round:3,players:[],remote:false});
    const box=document.getElementById('pad-screen');
    return {iframe:!!box.querySelector('iframe'),
            says:(box.textContent||'').trim(),hidden:box.hidden};
  });
  if(room.iframe)probs.push('the phone plays the record even though the room shares one screen');
  if(room.hidden||!room.says)
    probs.push('the phone goes blank in a shared room and looks broken instead of saying why');
  else console.log('  in a shared room the phone says: "'+room.says+'"');

  await b.close();srv.close();
  if(probs.length){console.log('FAIL:');probs.forEach(x=>console.log('  x '+x));process.exit(1)}
  console.log('ok - the phone starts muted, asks for one tap, and remembers it');
  process.exit(0);
})().catch(e=>{console.log('FAIL:');console.log('  x '+String(e).slice(0,300));process.exit(1)});
