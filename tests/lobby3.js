// The waiting page leads with whatever the host needs at that moment.
//
// It used to lead, always, with a room code the size of a door, a QR block
// and an invitation URL — on the second game of the evening as well, right
// after a screen that has just told the room nobody needs inviting again.
// And "Playing without a phone?" was a bordered panel holding one line.
//
// Before anybody has arrived the code and the QR are the point and nothing
// here touches them. Once somebody is in a chair, or a game has been played
// tonight, `#s-lobby` carries data-party and the stylesheet folds the
// invitation into one line. Nothing is taken away: the code comes back in one
// click, on a button whose words are already in UITEXT in all three languages.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const ev=x=>w.eval(x);
const $=id=>d.getElementById(id);
const css=html.slice(html.indexOf('<style'),html.indexOf('</style>'));

const host="S.players=[{id:0,name:'Henkka',icon:0,score:0}];";
const guests="S.players=[{id:0,name:'Henkka',icon:0,score:0},"+
             "{id:1,name:'Mia',icon:1,score:0,pid:'p1'}];";

setTimeout(()=>{
  const lob=$('s-lobby');
  if(!lob){probs.push('there is no s-lobby on the page');return done()}
  if(typeof w.lobbyMode!=='function'){
    probs.push('lobbyMode() is gone — nothing decides which lobby this is');
    return done();
  }
  const mode=()=>[lob.getAttribute('data-party'),lob.getAttribute('data-again')];

  // ---- 1. an empty room: the code and the QR are the whole point ----
  ev("PARTY.role='host';PARTY.code='TESTAA';S.lang='fi';S.games=0;"+host+"lobbyMode();");
  let m=mode();
  if(m[0])probs.push('a room nobody has joined is already dressed as a party');
  if(m[1])probs.push('a night with no games behind it says a game has been played');

  // ---- 2. somebody has taken a chair ----
  ev("S.games=0;"+guests+"lobbyMode();");
  m=mode();
  if(!m[0])probs.push('a chair has been taken and the code still leads the screen');
  if(m[1])probs.push('the first game of the night is announced as the next one');

  // ---- 3. a game has been played: the room is assembled, host or not ----
  ev("S.games=2;"+host+"lobbyMode();");
  m=mode();
  if(!m[0])probs.push('a second game still opens on a full-size invitation');
  if(!m[1])probs.push('a second game is not announced as the next game');

  // ---- 4. and it goes back when a new party is opened ----
  ev("S.games=0;"+host+"lobbyMode();");
  if(mode()[0])probs.push('the lobby never goes back to leading with the code');

  // ---- 5. the code is always one click away ----
  const peek=$('lobby-peek');
  if(!peek)probs.push('nothing brings the code back: there is no lobby-peek button');
  else{
    if(!lob.contains(peek))probs.push('the button that reopens the code is not on the lobby');
    ev("S.games=3;"+guests+"lobbyMode();");
    peek.click();
    const over=$('joinover');
    if(!over||over.hidden)
      probs.push('the button that should reopen the code and QR opened nothing');
    if(over&&$('jo-code')&&$('jo-code').textContent.indexOf('TESTAA')<0)
      probs.push('the reopened invitation does not carry the room code: '+$('jo-code').textContent);
  }
  // the code, the QR and the invitation are hidden by stylesheet, never removed
  ['lobby-code','lobby-qr','lobby-link','copy-link'].forEach(id=>{
    if(!$(id))probs.push(id+' has been taken off the page altogether');
  });

  // ---- 6. the stylesheet is what does the folding ----
  [[/#s-lobby\[data-party\][^{]*\.lobbygrid\s*>\s*\.lobbycode\{[^}]*display:flex/,
    'the invitation does not fold into one row when the room is assembled'],
   [/#s-lobby\[data-party\][^{]*#lobby-qr[^{]*\{[^}]*display:none/,
    'the QR block still takes its full height once everyone has arrived'],
   [/#s-lobby \.lobbycode\.nophone\{[^}]*border:0/,
    '"playing without a phone" is still a bordered panel when it is closed']
  ].forEach(([re,what])=>{if(!re.test(css))probs.push(what)});

  // ---- 7. nothing new was written in English only ----
  ['Show the code and QR big','Your next game starts here'].forEach(k=>{
    ['fi','sv'].forEach(l=>{
      if(!ev('UITEXT['+JSON.stringify(l)+'] && UITEXT['+JSON.stringify(l)+'][' +
             JSON.stringify(k)+']'))
        probs.push('"'+k+'" has no '+l+': the lobby would read English');
    });
  });
  if(html.indexOf('<h2 class="lobbyagain">Your next game starts here</h2>')<0)
    probs.push('the heading for an assembled room is gone');

  done();
},1400);

function done(){
  console.log(probs.length?'FAIL:':'ok - the lobby leads with the code, then with the chairs and the settings');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
}
