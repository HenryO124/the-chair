// The record page, driven the way the house will drive it.
//
// It cannot be checked against Apple from here — iTunes is not reachable from
// this container, which is the mistake that cost a whole afternoon once. So
// Apple is stood in for, and everything else is real: banks.js is loaded from
// disk, the catalogue is read off it, the cards advance, a record with nothing
// to hear skips itself, the decisions survive a reload, and the text at the end
// is the text that has to be pasted back here.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const {chromium}=require('playwright');
const http=require('http'),fs=require('fs'),url=require('url');

const probs=[];
const srv=http.createServer((q,r)=>{
  const f=path.join(ROOT,decodeURIComponent(url.parse(q.url).pathname.split('?')[0]));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end()}else{
    r.writeHead(200,{'content-type':/\.js$/.test(f)?'text/javascript':'text/html'});r.end(d)}})});

// The catalogue, read here so the stand-in can answer with the record that was
// actually asked for. banks.js is a list of plain assignments, so evaluating it
// gives the same CATALOG the browser will see.
const BANKS=path.join(ROOT,'banks.js');
let CATALOG=null;
try{ (0,eval)(fs.readFileSync(BANKS,'utf8')); CATALOG=global.CATALOG||CATALOG; }
catch(e){ probs.push('banks.js would not evaluate here: '+String(e).slice(0,90)); }
if(!CATALOG||!CATALOG.length){probs.push('no catalogue in banks.js')}

// Two records are made deliberately silent, so the skip path runs for real.
const SILENT=(CATALOG||[]).slice(0,2).map(a=>a[0]+' '+a[5]);
const BY_TERM={};
(CATALOG||[]).forEach(a=>{BY_TERM[a[0]+' '+a[5]]={artist:a[0],track:a[5]}});

(async()=>{
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const base='http://127.0.0.1:'+srv.address().port+'/records.html';
  const b=await chromium.launch();
  const ctx=await b.newContext({viewport:{width:390,height:844}});
  const p=await ctx.newPage();
  p.on('pageerror',e=>probs.push('JS error: '+String(e).slice(0,130)));

  // Stand in for Apple: answer with the record that was asked for, except the
  // two chosen to be silent, so the skip path is exercised for real.
  let asked=0;
  await p.route('**itunes.apple.com/**',route=>{
    asked++;
    const u=new URL(route.request().url());
    const term=u.searchParams.get('term')||'';
    const rec=BY_TERM[term];
    const silent=SILENT.indexOf(term)>=0;
    const body=JSON.stringify({results:(silent||!rec)?[]:[{
      artistName:rec.artist, trackName:rec.track,
      previewUrl:'http://127.0.0.1:1/silence.m4a', artworkUrl100:''}]});
    route.fulfill({status:200,contentType:'application/json',body});
  });

  await p.goto(base);
  await p.waitForTimeout(2500);

  const total=await p.evaluate(()=>CAT&&CAT.length);
  if(!total){probs.push('the page never got the catalogue out of banks.js')}
  else console.log('  '+total+' records came out of banks.js');

  // The first card has to name a real record, not a placeholder.
  const first=await p.evaluate(()=>({act:document.getElementById('act').textContent,
                                     trk:document.getElementById('trk').textContent,
                                     yes:document.getElementById('yes').disabled}));
  if(/Ladataan|Levyjä ei saatu/.test(first.act))probs.push('the first card never loaded: '+first.act);
  else console.log('  first card: '+first.act+' '+first.trk);
  if(first.yes)probs.push('the buttons are still dead after the first card loaded');

  // Ten decisions, alternating, through the real buttons.
  for(let i=0;i<10;i++){
    await p.click(i%2?'#no':'#yes');
    await p.waitForTimeout(250);
  }
  const after=await p.evaluate(()=>Object.keys(decided).length);
  if(after<10)probs.push('ten taps produced only '+after+' decisions');
  else console.log('  ten taps, '+after+' decisions recorded');

  // The keyboard has to work too: the house will use it on a laptop.
  await p.keyboard.press('ArrowRight');
  await p.waitForTimeout(250);
  await p.keyboard.press('ArrowLeft');
  await p.waitForTimeout(250);
  const afterKeys=await p.evaluate(()=>Object.keys(decided).length);
  if(afterKeys!==after+2)probs.push('the arrow keys recorded '+(afterKeys-after)+' of 2 decisions');

  // Reload: nothing decided may be asked again.
  const seen=await p.evaluate(()=>Object.keys(decided));
  await p.reload();
  await p.waitForTimeout(2200);
  const kept=await p.evaluate(()=>Object.keys(decided).length);
  if(kept!==afterKeys)probs.push('a reload lost '+(afterKeys-kept)+' decisions');
  else console.log('  a reload kept all '+kept+' decisions');
  const nowShowing=await p.evaluate(()=>cur?cur[0]+' | '+cur[5]:'');
  if(seen.indexOf(nowShowing)>=0)probs.push('after the reload it asked again about '+nowShowing);

  // A record Apple has nothing for is counted, not shown.
  const skipped=await p.evaluate(()=>skipped.length);
  console.log('  '+skipped+' record(s) skipped for having nothing to hear');

  // The end screen, which is the only output that matters.
  await p.evaluate(()=>finish());
  await p.waitForTimeout(300);
  const out=await p.evaluate(()=>document.getElementById('out').value);
  let parsed=null;
  try{parsed=JSON.parse(out)}catch(e){probs.push('the text to paste back is not JSON: '+String(out).slice(0,60))}
  if(parsed){
    const keys=Object.keys(parsed);
    console.log('  the end screen offers '+keys.length+' accepted keys, e.g. '+(keys[0]||'—'));
    if(!keys.length)probs.push('nothing was accepted, so there is nothing to paste back');
    if(keys.some(k=>k.indexOf(' | ')<0))
      probs.push('a key is not in the "Artist | Track" shape the game looks up');
    if(Object.values(parsed).some(v=>v!==1))probs.push('a key carries something other than 1');
  }
  const tally=await p.evaluate(()=>document.getElementById('tally').textContent);
  console.log('  '+tally);

  // ---- the bug that cost a whole pass: a refusal is not an empty shelf ----
  // Apple rate-limits. The first version of this page wrote every 403 down as
  // "this record does not exist" and declared 118 acts silent, Bowie and
  // Aretha among them. So: refuse the first two requests for a record and
  // make sure it still ends up in front of a person.
  const c2=await b.newContext({viewport:{width:390,height:844}});
  const p2=await c2.newPage();
  p2.on('pageerror',e=>probs.push('rate-limit page JS error: '+String(e).slice(0,130)));
  let refusals=0;
  await p2.route('**itunes.apple.com/**',route=>{
    const u=new URL(route.request().url());
    const term=u.searchParams.get('term')||'';
    const rec=BY_TERM[term];
    if(refusals<2){refusals++;return route.fulfill({status:403,contentType:'text/plain',body:'no'})}
    route.fulfill({status:200,contentType:'application/json',body:JSON.stringify({results:rec?[{
      artistName:rec.artist,trackName:rec.track,
      previewUrl:'http://127.0.0.1:1/silence.m4a',artworkUrl100:''}]:[]})});
  });
  await p2.goto(base);
  await p2.waitForTimeout(7000);
  const st2=await p2.evaluate(()=>({act:document.getElementById('act').textContent,
                                    skipped:skipped.length,
                                    live:!document.getElementById('yes').disabled}));
  console.log('  after '+refusals+' refusals: card shows "'+st2.act+'", '
              +st2.skipped+' written off, buttons '+(st2.live?'live':'dead'));
  if(st2.skipped>0)
    probs.push('a refused lookup was written down as a record with nothing to hear');
  if(!st2.live)
    probs.push('the page never recovered from the refusals — the card is still dead');

  await b.close();srv.close();
  if(probs.length){console.log('FAIL:');probs.forEach(x=>console.log('  x '+x));process.exit(1)}
  console.log('ok - the record page loads the catalogue, takes decisions, remembers them,');
  console.log('     survives Apple refusing, and hands back pasteable keys');
  process.exit(0);
})().catch(e=>{console.log('FAIL:');console.log('  x '+String(e).slice(0,400));process.exit(1)});
