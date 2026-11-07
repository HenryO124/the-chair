// The host sits at this device: the name on the chip is the name in the room.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const d=new JSDOM(fs.readFileSync(SRC,'utf8'),
 {runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=d.window,doc=w.document,$=id=>doc.getElementById(id);
const probs=[];
setTimeout(()=>{
  // Henkka names himself in Settings, then opens a room
  $('set-name').value='Henkka';
  $('set-name').dispatchEvent(new w.Event('change'));
  if(w.eval('MYNAME')!=='Henkka')probs.push('the name did not stick');
  if(!/Henkka/.test($('me-name').textContent))probs.push('the chip does not say Henkka');
  if(w.eval("(S.players[0]||{}).name")!=='Henkka')
    probs.push('the host chair is still '+w.eval("JSON.stringify((S.players[0]||{}).name)"));
  w.eval("PARTY.role='host';PARTY.code='TEST';drawRoomBar();drawLobbyList()");
  const bar=$('rb-joined').textContent+' '+$('lobby-list').textContent;
  if(/Player 1/.test(bar))probs.push('the room still announces Player 1: '+bar.trim().slice(0,60));
  if(!/Henkka/.test(bar))probs.push('the room does not show Henkka: '+bar.trim().slice(0,60));
  // and a name typed straight into the chair is not trampled
  w.eval("S.players[0].name='Kalle'");
  $('set-name').value='Henkka2';
  $('set-name').dispatchEvent(new w.Event('change'));
  if(w.eval("S.players[0].name")!=='Kalle')
    probs.push('renaming the device overwrote a name typed into the chair');
  console.log(probs.length?'FAIL:':'ok - the host plays under their own name');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
