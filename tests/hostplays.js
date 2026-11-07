// Can the person sitting at the television actually play, in every game?
//
// Three times tonight the answer was no, one game at a time: Closest Wins had
// no box to type a number into, the Short List had no way to stop and hand the
// turn on, and both were found by the owner mid-game rather than here. The
// screen can act for whoever sits at it — that is how a room with one laptop
// and no spare phone plays at all — and whether it can was being decided
// game by game, in different places, by hand.
//
// So this asks all seven the same question at once, and will ask it of the
// eighth the day somebody writes one.
const path=require("path"),fs=require('fs'),{JSDOM}=require('jsdom');
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const probs=[];
const dom=new JSDOM(fs.readFileSync(SRC,'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,ev=x=>w.eval(x);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));

setTimeout(()=>{
  const games=JSON.parse(ev("JSON.stringify(Object.keys(GAMELABEL).filter(g=>!SHELVED[g]))"));
  if(!games.length){console.log('FAIL:');console.log('  x no list of games to walk');process.exit(1)}

  for(const g of games){
    ev("S.lang='fi';S.game="+JSON.stringify(g)+";S.len=5;S.cats=[]");
    // one person at the television with no phone, one person on a phone
    ev("S.players=[{id:'a',name:'Henkka',score:0},{id:'b',name:'Mia',score:0,pid:'p2'},"
       +"{id:'c',name:'Ale',score:0,pid:'p3'}]");
    try{ev("show('s-quiz');quizStart()")}catch(e){probs.push(g+': the game would not start — '+e.message);continue}
    if(ev("isS10()"))ev("s10SetTurn('a')");
    try{ev("drawQuiz()")}catch(e){probs.push(g+': drawing the screen threw — '+e.message);continue}

    const opts=d.querySelectorAll('#q-options button[data-opt]:not([disabled])').length;
    const fields=d.querySelectorAll('#q-options input:not([disabled])').length;
    const extra=[...d.querySelectorAll('#q-options button:not([data-opt]):not([disabled])')].length;
    const stand=ev("isS10()")&&!!d.getElementById('s10-stand');
    const can=opts+fields+extra+(stand?1:0);
    if(!can)probs.push(g+': the person at the television has nothing to press or type');
    else console.log('  %s  %d answer(s), %d field(s)%s',
      g.padEnd(8), opts, fields, stand?', and a way to stop':'');
  }

  // and the Short List's stop button must not survive into another game
  ev("S.game='s10';S.players=[{id:'a',name:'Henkka',score:0},{id:'b',name:'Mia',score:0,pid:'p2'}];"
     +"show('s-quiz');quizStart();s10SetTurn('a');drawQuiz()");
  if(!d.getElementById('s10-stand'))probs.push('the Short List lost its stop button');
  for(const g of ['near','trivia','finger']){
    ev("S.game="+JSON.stringify(g)+";S.players=[{id:'a',name:'Henkka',score:0},{id:'b',name:'Mia',score:0,pid:'p2'}];");
    try{ev("quizStart();drawQuiz()")}catch(e){}
    const b=d.getElementById('s10-stand'),box=d.getElementById('s10-rules');
    if(b&&box&&!box.hidden)probs.push(g+': the Short List stop button is still on the screen');
  }

  if(probs.length){console.log('FAIL:');probs.forEach(p=>console.log('  x '+p));process.exit(1)}
  console.log('ok - in every game the person at the television can play');
  process.exit(0);
},700);
