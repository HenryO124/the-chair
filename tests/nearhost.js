// The person at the television has to be able to play Closest Wins.
//
// Every other game lets the host answer for whoever sits at the screen without
// a phone. This one had nothing on the screen to answer with, so a host playing
// from a laptop could only watch his own question go by.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const probs=[];
const dom=new JSDOM(fs.readFileSync(SRC,'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,ev=x=>w.eval(x);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
setTimeout(()=>{
  ev("S.lang='fi';S.game='near';S.len=5;S.cats=[]");
  ev("S.players=[{id:'a',name:'Henkka',score:0},{id:'b',name:'Mia',score:0,pid:'p2'}]");
  try{ev("nearStart()")}catch(e){probs.push('nearStart threw: '+e.message)}

  const box=d.getElementById('near-host');
  if(!box)probs.push('the television gives the person sitting at it nothing to type into');
  const label=d.querySelector('#q-options .nearhost label');
  if(label&&label.textContent.indexOf('Henkka')<0)
    probs.push('the box does not say whose guess it is: '+label.textContent);
  // the phone player must NOT get a box on the television
  if(box){
    box.value='1906';
    d.getElementById('near-hostgo').click();
    const g=JSON.parse(ev('JSON.stringify(Q.guesses)'));
    if(g.a!==1906)probs.push('the typed number never became a guess: '+JSON.stringify(g));
    if('b' in g)probs.push("the television answered for the phone player too");
  }
  // once the person at the screen has guessed, the box goes away
  const again=d.getElementById('near-host');
  if(again)probs.push('the box is still there after that person has guessed');

  // half-typed text survives somebody else guessing
  ev("nearNext&&nearNext()");
  const b2=d.getElementById('near-host');
  if(!b2)probs.push('no box on the second question');
  else{
    b2.value='12';
    b2.dispatchEvent(new w.Event('input',{bubbles:true}));
    ev("nearGuess(S.players[1],999)");          // the phone answers, the screen redraws
    const b3=d.getElementById('near-host');
    if(!b3)probs.push('the box vanished when the phone answered');
    else if(b3.value!=='12')
      probs.push('a phone answering wiped what was half typed: '+JSON.stringify(b3.value));
  }
  // a comma is a decimal mark here, and rubbish is refused rather than counted
  ev("nearNext&&nearNext()");
  const b4=d.getElementById('near-host');
  if(b4){
    b4.value='ei tietoa';
    d.getElementById('near-hostgo').click();
    const g=JSON.parse(ev('JSON.stringify(Q.guesses)'));
    if('a' in g)probs.push('"ei tietoa" was taken as a number');
    b4.value='3,5';
    d.getElementById('near-hostgo').click();
    const g2=JSON.parse(ev('JSON.stringify(Q.guesses)'));
    if(g2.a!==3.5)probs.push('a Finnish decimal comma was not understood: '+JSON.stringify(g2));
  }
  if(probs.length){console.log('FAIL:');probs.forEach(p=>console.log('  x '+p));process.exit(1)}
  console.log('ok - the person at the television can play Closest Wins, and nobody else is answered for');
  process.exit(0);
},500);
