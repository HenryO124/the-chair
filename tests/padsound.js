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
    padVid='';
    drawPadScreen({phase:'live',game:'artist',vid:'dQw4w9WgXcQ',round:1,players:[],remote:true});
    const f=document.querySelector('#pad-screen iframe'),s=document.getElementById('pad-sound');
    return {src:f?f.getAttribute('src'):'', label:s?s.textContent.trim():'',
            wants:s?s.className.indexOf('wants')>=0:false};
  });

  // ---- first record on a phone that has never tapped ----
  let r=await paint();
  if(!r.src)probs.push('the phone never got a player at all');
  if(/mute=0/.test(r.src))
    probs.push('the first record is handed to the phone unmuted — the browser will refuse it outright');
  if(!/mute=1/.test(r.src))probs.push('the embed does not say whether it is muted: '+r.src.slice(0,90));
  if(!r.wants)probs.push('nothing on the phone invites the tap that would turn the sound on');
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

  await b.close();srv.close();
  if(probs.length){console.log('FAIL:');probs.forEach(x=>console.log('  x '+x));process.exit(1)}
  console.log('ok - the phone starts muted, asks for one tap, and remembers it');
  process.exit(0);
})().catch(e=>{console.log('FAIL:');console.log('  x '+String(e).slice(0,300));process.exit(1)});
