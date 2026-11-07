// Items 11-18: the host's side of the room.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
const MISS={className:'',textContent:'',hidden:true,missing:true};
const $=id=>d.getElementById(id)||(probs.push('there is no '+id+' on the page'),MISS);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled&&el.dispatchEvent)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
setTimeout(()=>{
  // a host with an open room, two phones in it, and somebody at the door
  w.eval(`PARTY.role='host';PARTY.code='TEST';PARTY.client=null;
    S.game='trivia';MAX_CHAIRS=3;
    S.players=[{id:0,name:'',icon:0},
               {id:1,name:'Mia',icon:1,pid:'p2'},
               {id:2,name:'Jussi',icon:2,pid:'p3'}];
    KNOCKS.p9={pid:'p9',name:'Anna',icon:3};`);

  // ---- 11. a knock is visible wherever the host is ----
  w.eval(`show('s-quiz');drawKnocks();`);
  if($('knockbar').hidden)probs.push('a knock during a quiz is invisible to the host');
  if(!/Anna/.test($('knockbar').textContent))probs.push('the knock does not say who is at the door');
  w.eval(`show('s-break');drawKnocks();`);
  if(!$('knockbar').hidden)probs.push('the floating knock still shows on the break screen, which lists them anyway');
  w.eval(`delete KNOCKS.p9;show('s-quiz');drawKnocks();`);
  if(!$('knockbar').hidden)probs.push('the knock bar stayed up after the door was dealt with');
  w.eval(`KNOCKS.p9={pid:'p9',name:'Anna',icon:3};drawKnocks();`);

  // ---- 14. raising the ceiling opens the door ----
  if(/LET THEM IN/.test($('knocks').innerHTML))
    probs.push('a full room still offers to let somebody in');
  w.eval('setMax(MAX_CHAIRS+1)');
  if(!/LET THEM IN/.test($('knocks').innerHTML))
    probs.push('making room did not redraw the door: still says the room is full');
  w.eval('setMax(3)');

  // ---- 12. the hardware Back on the game menu must not end the party ----
  w.eval(`show('s-setup')`);
  const before=w.eval('PARTY.code');
  w.eval('goBack()');
  if(w.eval('PARTY.code')!==before)probs.push('BACK ON THE GAME MENU SHUT THE ROOM DOWN');
  if(w.eval('screenNow()')!=='s-lobby')
    probs.push('Back on the game menu went to '+w.eval('screenNow()')+' instead of the lobby');

  // ---- 13. and on the lobby it does something ----
  w.eval(`show('s-lobby')`);
  const moved=w.eval('goBack()');
  if(!moved||w.eval('screenNow()')!=='s-setup')
    probs.push('Back on the lobby is inert: still at '+w.eval('screenNow()'));
  if(w.eval('PARTY.code')!==before)probs.push('Back from the lobby shut the room down');

  // ---- 18. the Chair's settings stay out of a quiz ----
  w.eval("S.game='trivia';dressRules()");
  if(!$('teamsize').hidden||!$('teamsize').previousElementSibling.hidden)
    probs.push('"Singers per team" is still offered in a quiz');

  // ---- 17. every chair listed once ----
  w.eval('drawLobbyList()');
  const names=[...d.querySelectorAll('#lobby-list .who')].map(e=>e.textContent.trim());
  const seen={};names.forEach(x=>{seen[x]=(seen[x]||0)+1});
  const twice=Object.keys(seen).filter(k=>seen[k]>1);
  if(twice.length)probs.push('the lobby lists '+twice.join(', ')+' twice');

  // ---- 16. an empty row is not a player ----
  w.eval('delete KNOCKS.p9');
  click($('lobby-start'));
  const left=w.eval('JSON.stringify(S.players.map(function(p){return p.name}))');
  if(/""/.test(left))probs.push('the nameless empty row went into the game and will never answer: '+left);
  if(w.eval('S.players.length')!==2)probs.push('the wrong people went into the game: '+left);

  // ---- 15. the phone is told what is happening ----
  const st=JSON.parse(w.eval('JSON.stringify(stageState())'));
  if(!('knocks' in st))probs.push('the stage says nothing about who is at the door');
  w.eval(`PARTY.role='chair';PARTY.pid='p9';PARTY.code='TEST';
    PARTY.stage={phase:'lobby',game:'trivia',seats:[],knocks:['p9'],full:true,
      round:0,of:10,options:[],revealed:false};
    show('s-chair');drawPad();`);
  const said=$('pad-state').textContent;
  if(said===w.eval("T('door_asking')")||!said)
    probs.push('a phone at a full door is still just asking for a chair: '+said);
  const wantFull=w.eval("T('door_full')");
  if(said!==wantFull)
    probs.push('the phone is not told the room is full: "'+said+'", expected "'+wantFull+'"');

  console.log(probs.length?'FAIL:':'ok - the host: knocks seen, Back safe, empty row dropped, phone told');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1100);
