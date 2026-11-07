// Smart 10's turn: round the table, keep going while you are right,
// stop whenever you like, and the last one in just carries on.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const d=new JSDOM(fs.readFileSync(SRC,'utf8'),
 {runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=d.window;const probs=[];
const ev=x=>w.eval(x);
setTimeout(()=>{
  ev(`S.game='s10';S.lang='en';
    S.players=[{id:0,name:'A',score:0},{id:1,name:'B',score:0},{id:2,name:'C',score:0}];
    Q.deck=s10Bank().slice(0,3);Q.round=0;Q.on=true;Q.first=undefined;s10Next();`);
  const right=()=>ev("(function(){for(var i=0;i<Q.cands.length;i++)if(Q.cands[i].ok&&Q.cands[i].by===null)return i;return -1})()");
  const wrong=()=>ev("(function(){for(var i=0;i<Q.cands.length;i++)if(!Q.cands[i].ok&&Q.cands[i].by===null)return i;return -1})()");

  const first=ev('Q.turn');
  if(first!==0)probs.push('the first question did not start with the first player: '+first);

  // out of turn does nothing
  ev('s10Take(S.players[1],'+right()+')');
  if(ev('Q.pot[1]'))probs.push('B took one on A’s turn');

  // A is right, so it is still A's turn
  ev('s10Take(S.players[0],'+right()+')');
  if(ev('Q.turn')!==0)probs.push('being right handed the turn away');
  // A stops; the turn goes to B
  ev('s10Stand(S.players[0])');
  if(ev('Q.turn')!==1)probs.push('stopping did not pass the turn: '+ev('Q.turn'));
  if(ev('S.players[0].score')!==10)probs.push('stopping did not pay: '+ev('S.players[0].score'));
  // B is wrong; the turn goes to C, and C is the last one in
  ev('s10Take(S.players[1],'+wrong()+')');
  if(ev('Q.turn')!==2)probs.push('a wrong pick did not pass the turn: '+ev('Q.turn'));
  if(ev("Q.state[1]")!=='out')probs.push('a wrong pick left B in');
  // the last player in keeps the turn however many they take
  for(let k=0;k<3;k++){
    const r=right(); if(r<0)break;
    ev('s10Take(S.players[2],'+r+')');
    if(ev('Q.turn')!==2)probs.push('the last player in lost the turn after a pick');
  }
  if(ev('Q.revealed'))probs.push('the round ended itself while C was still deciding');
  ev('s10Stand(S.players[2])');
  if(!ev('Q.revealed'))probs.push('the round did not end when the last player stopped');

  // the next question starts with the next player at the table
  ev('quizNext()');
  if(ev('Q.turn')!==1)probs.push('the next question did not rotate the start: '+ev('Q.turn'));
  ev('quizNext()');
  if(ev('Q.turn')!==2)probs.push('the start did not keep rotating: '+ev('Q.turn'));

  // the phones are told whose turn it is
  const st=JSON.parse(ev('JSON.stringify(s10State("live"))'));
  if(st.turn!==2)probs.push('the phones were not told whose turn it is: '+st.turn);
  if(st.turnName!=='C')probs.push('the phones were not told the name: '+st.turnName);

  console.log(probs.length?'FAIL:':'ok - the turn: round the table, keep going while right, stop when you like');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1100);
