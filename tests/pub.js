// Public parties: the choice is on the page, the room announces itself, the
// front page lists it, and the panel stays quiet when nothing is open.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
setTimeout(()=>{
// This suite was written against the English page and checks wording. The
// interface now speaks Finnish by default, so it asks for English first;
// the Finnish and Swedish wording is covered by words.js and uilang.js.
  try{w.eval("S.lang='en';typeof dressUI==='function'&&dressUI()")}catch(e){}

  // --- the choice exists where the room waits, and it starts private ---
  if(!$('vis'))probs.push('no public/private choice on the waiting page');
  if(w.eval('!!S.public'))probs.push('a new room is public by default');

  // --- a public room publishes one retained line about itself ---
  const sent=[];
  w.eval(`PARTY.role='host';PARTY.code='TEST';
    PARTY.client={publish:function(t,p,o){SENT.push([t,p,o&&o.retain])}};
    S.players=[{name:'Henry'},{name:'Mia',pid:'p2'}];S.game='trivia';`);
  w.SENT=sent;
  click(d.querySelector('#vis [data-v="public"]'));
  if(!w.eval('!!S.public'))probs.push('choosing Public did not take');
  const ping=sent.filter(r=>/\/dir\//.test(r[0])&&r[1]);
  if(!ping.length)probs.push('a public room did not announce itself');
  else{
    if(ping[0][2]!==true)probs.push('the line is not retained, so nobody arriving later sees it');
    let m={};try{m=JSON.parse(ping[0][1])}catch(e){probs.push('the line is not readable JSON')}
    if(m.c!=='TEST')probs.push('the line carries the wrong room');
    if(m.g!=='trivia')probs.push('the line does not say which game');
    if(!m.m||!m.s)probs.push('the line is missing how full it is or whether it is live');
    if(/pid|p2/.test(ping[0][1]))probs.push('the line carries something personal');
  }
  if($('vis-note')&&!/anyone/i.test($('vis-note').textContent))
    probs.push('the choice does not say what public means');

  // --- going private clears the line again ---
  sent.length=0;
  click(d.querySelector('#vis [data-v="private"]'));
  if(!sent.filter(r=>/\/dir\//.test(r[0])&&r[1]==='').length)
    probs.push('going private left the room listed');

  // --- the front page lists what it hears ---
  w.eval(`DIR.client={};DIR.rooms={};PARTY.code='';
    DIR.rooms['AB12']={c:'AB12',n:'Mia',g:'s10',p:3,m:8,s:'wait',t:Date.now()};
    drawRooms();`);
  const list=$('pub-list').textContent;
  if(!/Mia/.test(list))probs.push('a room we heard about is not listed');
  if(!/Short List/.test(list))probs.push('the listing does not name the game');
  if(!/AB12/.test(list))probs.push('the listing does not show the code');
  const panel=$('pub-list').closest('.hpanel');
  if(panel&&panel.classList.contains('quiet'))probs.push('the panel is still folded with a room in it');

  // --- a room that stops talking falls off ---
  w.eval(`DIR.rooms['AB12'].t=Date.now()-200000;drawRooms();`);
  if(/Mia/.test($('pub-list').textContent))probs.push('a stale room is still listed');

  // --- and with nothing open the panel is one quiet line ---
  if(panel&&!panel.classList.contains('quiet'))
    probs.push('the empty panel is still the biggest box on the page');
  if(!$('pub-start'))probs.push('the empty panel does not offer to open a party');

  console.log(probs.length?'FAIL:':'ok - public parties: the choice, the line, the listing, the quiet panel');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
