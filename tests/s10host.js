// The person at the television has to be able to stop.
//
// The Short List keeps your turn while you keep being right: take another, or
// stop while the pot is worth something. A phone has a button for stopping.
// The television had none, so whoever sat at it could take and take and never
// hand over, and the turn stopped moving - with the screen still saying it was
// their go. Exactly the hole Closest Wins had.
const path=require("path"),fs=require('fs'),{JSDOM}=require('jsdom');
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const probs=[];
const dom=new JSDOM(fs.readFileSync(SRC,'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,ev=x=>w.eval(x);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const $=id=>d.getElementById(id);
setTimeout(()=>{
  ev("S.lang='fi';S.game='s10';S.len=5;S.cats=[]");
  // Henkka sits at the television; the other two are on phones
  ev("S.players=[{id:'a',name:'Henkka',score:0},{id:'b',name:'Ale',score:0,pid:'p2'},{id:'c',name:'B',score:0,pid:'p3'}]");
  ev("show('s-quiz');quizStart()");
  ev("s10SetTurn('a')");
  ev("drawQuiz()");

  if(!$('s10-stand'))probs.push('the television gives the person sitting at it no way to stop');

  // take a right one: the turn must stay, and the way out must still be there
  const okIdx=ev("Q.cands.findIndex(c=>c.ok&&c.by===null)");
  ev("s10Take(S.players[0],"+okIdx+")");
  // one pick each, then round the table: a right answer hands the turn on too
  if(ev("Q.turn")==='a')probs.push('the turn stayed put after a pick — play has to go round');
  const pot=ev("Q.pot.a||0");
  if(pot<=0)probs.push('a right answer paid nothing into the pot');
  console.log('  after one right answer the turn moved to '+ev("JSON.stringify(Q.turn)")+', pot '+pot);
  // back round to this player, who may now stop and keep the pot
  ev("s10SetTurn('a');drawQuiz()");
  const btn=$('s10-stand');
  if(!btn)probs.push('on their turn again, there is still no way to stop');
  else if(btn.textContent.indexOf(String(pot))<0)
    probs.push('the stop button does not say what stopping is worth: "'+btn.textContent+'"');
  else console.log('  back on their turn, the button says "'+btn.textContent+'"');
  btn&&btn.click();
  if(ev("S.players[0].score")!==pot)
    probs.push('stopping did not bank the pot: score is '+ev("S.players[0].score")+', pot was '+pot);
  if(ev("Q.turn")==='a')probs.push('the turn never left after stopping');
  else console.log('  stopping banked '+pot+' and the turn moved to '+ev("JSON.stringify(Q.turn)"));
  if($('s10-stand'))probs.push('the stop button is offered when it is not that person turn');

  // and it is never offered for a player who is on a phone
  ev("s10SetTurn('b');drawQuiz()");
  if($('s10-stand'))probs.push('the television offers to stop on behalf of a player holding a phone');

  if(probs.length){console.log('FAIL:');probs.forEach(p=>console.log('  x '+p));process.exit(1)}
  console.log('ok - the person at the television can stop, bank the pot and hand the turn on');
  process.exit(0);
},600);
