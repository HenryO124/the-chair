// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// Smart Ten: ten candidates, some true, a pot that grows and can be lost
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
setTimeout(()=>{
  if(!d.querySelector('#s-setup [data-game="s10"]'))probs.push('no Smart Ten card on the shelf');
  w.eval("S.game='s10';S.lang='fi';S.cats=[];S.len=4;S.players=[mkPlayer('A',0,0,'p1'),mkPlayer('B',1,1,'p2')]");
  const bank=w.eval('catBank().length');
  if(bank<8)probs.push('the set bank is thin: '+bank);
  // every set: ten candidates, three to six true, all with text
  const bad=w.eval("(function(){var b=s10Bank(),bad=[],thin=0;for(var i=0;i<b.length;i++){var c=b[i][3];"
   +"var t=c.filter(function(x){return x.ok}).length;"
   +"if(c.length!==10)bad.push(i+':'+c.length+' candidates');"
   // Henry's rule is that the number of true candidates varies between 4 and 9,
   // so that nobody can count. Exactly one inherited set is a legitimate 3 —
   // Finland has three land borders and the world does not bend for a rule —
   // so one is tolerated and a second would be a drift worth knowing about.
   +"if(t<3||t>9)bad.push(i+':'+t+' true');"
   +"if(t<4)thin++;"
   +"if(c.some(function(x){return !x.t}))bad.push(i+':empty candidate');"
   +"if(!b[i][1])bad.push(i+':no question');}if(thin>1)bad.push(thin+' sets have fewer than 4 true');return bad.join(', ')})()");
  if(bad)probs.push(bad);
  w.eval('quizStart()');
  if(!w.eval('Q.cands&&Q.cands.length===10'))probs.push('the round did not deal ten candidates');
  const A=()=>w.eval('S.players[0]'), score=()=>w.eval('S.players[0].score');
  const right=()=>w.eval("(function(){for(var i=0;i<Q.cands.length;i++)if(Q.cands[i].ok&&Q.cands[i].by===null)return i;return -1})()");
  const wrong=()=>w.eval("(function(){for(var i=0;i<Q.cands.length;i++)if(!Q.cands[i].ok&&Q.cands[i].by===null)return i;return -1})()");
  // play goes round the table: only whoever's turn it is may take
  if(w.eval('Q.turn')===undefined||w.eval('Q.turn')===null)
    probs.push('the round opened with nobody to play');
  w.eval('s10SetTurn(0)');
  w.eval('s10Take(S.players[1],'+right()+')');     // not their turn
  if(w.eval('Q.pot[1]'))probs.push('a player took one out of turn');

  // Play goes round the table: one pick each, then the next player, right or
  // wrong. The pot still builds across a player's own turns — 10, then 20,
  // then 30 — so stopping keeps costing something.
  for(let k=0;k<3;k++){
    w.eval('s10SetTurn(0)');
    w.eval('s10Take(S.players[0],'+right()+')');
    if(w.eval('Q.turn')===0)probs.push('a right pick kept the turn; play has to go round');
  }
  if(w.eval('Q.pot[0]')!==60)probs.push('the pot is '+w.eval('Q.pot[0]')+', expected 60');
  if(score()!==0)probs.push('an unbanked pot was already scored');
  // the other player takes a wrong one and is out with nothing
  w.eval('s10SetTurn(1)');
  w.eval('s10Take(S.players[1],'+right()+')');
  w.eval('s10SetTurn(1)');
  w.eval('s10Take(S.players[1],'+wrong()+')');
  if(w.eval('Q.turn')!==0)probs.push('a wrong pick did not pass the turn on');
  if(w.eval("Q.state[1]")!=='out')probs.push('a wrong pick did not end that round: '+w.eval('Q.state[1]'));
  if(w.eval('Q.pot[1]')!==0)probs.push('a wrong pick kept the pot');
  if(w.eval('S.players[1].score')!==0)probs.push('a wrong pick still scored');
  // banking keeps it
  w.eval('s10SetTurn(0)');
  w.eval('s10Stand(S.players[0])');
  if(score()!==60)probs.push('banking did not pay: '+score());
  if(!w.eval('Q.revealed'))probs.push('the round did not end when nobody was left in');

  // a taken candidate cannot be taken again
  const before=w.eval('JSON.stringify(Q.cands.map(function(c){return c.by}))');
  w.eval('s10Take(S.players[0],0)');
  if(w.eval('JSON.stringify(Q.cands.map(function(c){return c.by}))')!==before)
    probs.push('a candidate was claimed after the round ended');
  // the phone gets ten candidates and its own pot
  const st=JSON.parse(w.eval('JSON.stringify(s10State("live"))'));
  if(!st.cands||st.cands.length!==10)probs.push('the phone was sent '+(st.cands||[]).length+' candidates');
  if(st.seats[0].pot===undefined||st.seats[0].st===undefined)probs.push('the seat carries no pot or state');
  if(JSON.stringify(st).length>4000)probs.push('the payload is '+JSON.stringify(st).length+' bytes');
  // and it draws
  w.eval("PARTY.role='chair';PARTY.pid='p1';PARTY.stage="+JSON.stringify(st)+";drawPad()");
  const btns=d.querySelectorAll('#pad-quiz button[data-pick]');
  if(btns.length!==10)probs.push('the phone drew '+btns.length+' candidates');
  // next question deals a fresh round
  w.eval('quizNext()');
  if(w.eval('Q.revealed'))probs.push('the next round opened already revealed');
  if(w.eval("Q.state[0]")!=='in')probs.push('a player did not come back in for the next round');
  if(w.eval('Q.cands.some(function(c){return c.by!==null})'))probs.push('the new round kept old claims');
  // taking the last true one must NOT end the round: a player still in has to
  // decide to stop, and the room must not be told the truths have run out
  w.eval(`Q.revealed=false;
    S.players=[{id:0,name:'A',score:0},{id:1,name:'B',score:0}];
    Q.cands=[{t:'t1',ok:true,by:null},{t:'t2',ok:true,by:null},
             {t:'f1',ok:false,by:null},{t:'f2',ok:false,by:null}];
    Q.state={0:'in',1:'in'};Q.pot={0:0,1:0};Q.picks={0:0,1:0};
    s10SetTurn(0);
    // play goes round the table now, so each pick is made by whoever has the
    // turn rather than by the same player twice
    [0,1].forEach(function(i){
      var who=S.players.find(function(p){return p.id===Q.turn});
      if(who)s10Take(who,i);
    });`);
  if(w.eval('Q.cands.some(function(c){return c.by===null&&c.ok})'))
    probs.push('the test did not actually take every true candidate');
  if(w.eval('Q.revealed'))
    probs.push('THE ROUND ENDED ITSELF once the last true one was taken, so nobody had to decide to stop');
  if(w.eval("Q.state[0]")!=='in')
    probs.push('the player who took them all was cashed out without banking');
  if(w.eval('S.players[0].score'))
    probs.push('the pot was paid out before anyone banked: '+w.eval('S.players[0].score'));
  // and it ends as soon as the last one standing banks
  w.eval('s10Stand(S.players[0]);s10Stand(S.players[1]);');
  if(!w.eval('Q.revealed'))probs.push('the round did not end after everyone banked');
  if(!w.eval('S.players[0].score'))probs.push('banking paid nothing');
  w.eval('Q.revealed=false;');

  console.log(probs.length?'FAIL:':'ok - Smart Ten: ten candidates, a pot that grows, banked or lost');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
