// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// the front page: hero, filters, the list of open rooms, and the way in
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
const at=()=>[...d.querySelectorAll('.screen')].filter(s=>s.classList.contains('on')).map(s=>s.id).join('+');
setTimeout(()=>{
  if(at()!=='s-home')probs.push('the front page is not the first thing you see: '+at());
  ['m-create','m-code','m-solo','m-learn','home-code','home-go','pub-list','mode-filter','pub-filter','me-chip']
    .forEach(id=>{if(!$(id))probs.push('#'+id+' is missing')});
  if(!/Player 1/.test($('me-name').textContent))probs.push('the chip does not say Player 1: '+$('me-name').textContent);
  if(/Odessa/.test(d.body.textContent))probs.push('Odessa is still on the page');
  if(!/Nothing open|Looking for/.test($('pub-list').textContent))probs.push('no empty state for the room list');

  // a room announces itself
  w.eval("DIR.rooms={ABCD:{c:'ABCD',n:'Anna',g:'chair',p:5,m:8,s:'wait',t:Date.now()},"
        +"EFGH:{c:'EFGH',n:'Mike',g:'picture',p:8,m:8,s:'live',t:Date.now()}};drawRooms()");
  let rows=[...d.querySelectorAll('#pub-list .prow')];
  if(rows.length!==2)probs.push('the list shows '+rows.length+' rooms, expected 2');
  if(!/Anna/.test($('pub-list').textContent))probs.push('the host name is missing from the row');
  if(!/In progress/.test($('pub-list').textContent))probs.push('no state tag on the row');

  // filters
  click(d.querySelector('#pub-filter [data-f="wait"]'));
  rows=[...d.querySelectorAll('#pub-list .prow')];
  if(rows.length!==1)probs.push('the Waiting filter left '+rows.length+' rows');
  click(d.querySelector('#pub-filter [data-f="all"]'));
  click(d.querySelector('#mode-filter [data-g="picture"]'));
  rows=[...d.querySelectorAll('#pub-list .prow')];
  if(rows.length!==1||!/Mike/.test($('pub-list').textContent))probs.push('the game filter picked the wrong room');
  click(d.querySelector('#mode-filter [data-g="all"]'));

  // joining from the list, and from the code box
  click(d.querySelector('#pub-list button[data-join="ABCD"]'));
  if(at()!=='s-chair')probs.push('Join went to '+at());
  if($('join-code').value!=='ABCD')probs.push('Join did not carry the code: '+$('join-code').value);
  click($('nav-home'));
  $('home-code').value='wxyz';
  click($('home-go'));
  if($('join-code').value!=='WXYZ')probs.push('the code box did not carry: '+$('join-code').value);

  // renaming this device
  click($('nav-home'));
  click($('me-chip'));
  const inp=$('me-name').querySelector('input');
  if(!inp)probs.push('the name chip does not open');
  else{inp.value='Henry';inp.dispatchEvent(new w.Event('blur'));
    if(!/Henry/.test($('me-name').textContent))probs.push('the new name did not stick');
    if($('join-name').value!=='Henry')probs.push('the name did not reach the join form');}

  // and the old road still works
  click($('m-create'));
  setTimeout(()=>{
    if(at()!=='s-setup')probs.push('Create a party went to '+at());
    if(!$('rb-vis'))probs.push('no public/private switch on menu 2');
    else{click($('rb-vis'));
      if(!/Public/.test($('rb-vis').textContent))probs.push('the switch does not say Public: '+$('rb-vis').textContent);
      if(!w.eval('S.public'))probs.push('the room did not go public');}
    console.log(probs.length?'FAIL:':'ok - front page, filters, open rooms, join, name, menu 2');
    probs.forEach(p=>console.log('  x '+p));
    process.exit(probs.length?1:0);
  },300);
},600);
