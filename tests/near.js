// Closest Wins: the answer is a number, nobody gets options, and the closest
// guess takes it.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
const MISS={textContent:'',innerHTML:'',hidden:true,className:'',value:''};
const $=id=>d.getElementById(id)||(probs.push('there is no '+id),MISS);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const ev=x=>w.eval(x);
const score=i=>ev('S.players['+i+'].score||0');
setTimeout(()=>{
  if(ev("typeof nearStart")!=='function'){
    console.log('FAIL:');console.log('  x this page has no Closest Wins');process.exit(1);
  }
  // ---- a number is a number however the bank wrote it ----
  // a comma is a decimal mark in Finnish and Swedish, and a thousands mark in
  // the bank; both have to work, and 1,2,3 is neither
  const nums={'206':206,'1,440':1440,'1 440':1440,'3.5':3.5,'-2':-2,
              '3,5':3.5,'0,25':0.25,'12 345':12345,'1,234,567':1234567};
  Object.keys(nums).forEach(k=>{
    if(ev('asNumber('+JSON.stringify(k)+')')!==nums[k])
      probs.push('asNumber('+k+') is '+ev('asNumber('+JSON.stringify(k)+')'));
  });
  ['','abc','1989 or so','1,2,3',' '].forEach(k=>{
    if(ev('asNumber('+JSON.stringify(k)+')')!==null)
      probs.push('asNumber took '+JSON.stringify(k)+' as a number');
  });

  // ---- the bank has questions whose answer really is a number ----
  ev("S.lang='fi'");
  const bank=JSON.parse(ev('JSON.stringify(nearBank())'));
  if(bank.length<20)probs.push('only '+bank.length+' questions to play with');
  if(bank.some(r=>typeof r[2]!=='number'||!isFinite(r[2])))
    probs.push('a question came through without a number for an answer');
  if(bank.some(r=>!r[1]||!String(r[1]).trim()))probs.push('a question has no text');

  // ---- a round ----
  ev(`S.game='near';S.lang='en';S.len=5;S.cats=[];
    PARTY.role='host';PARTY.code='TESTAA';
    S.players=[{id:0,name:'Henkka',icon:0,score:0},
               {id:1,name:'Mia',icon:1,pid:'p2',score:0},
               {id:2,name:'Jussi',icon:2,pid:'p3',score:0}];
    show('s-quiz');quizStart();`);
  if(ev('Q.deck.length')!==5)probs.push('the deck is '+ev('Q.deck.length'));
  if(!ev('Q.current'))probs.push('no question came up');
  // No answer may be pickable: the whole game is that nobody is given the
  // number. The box the person at the television types into is not an answer,
  // so this asks for option buttons by name rather than for buttons at all.
  if(d.querySelectorAll('#q-options button[data-opt]').length)
    probs.push('this game gave the room options to pick from');
  const stray=[...d.querySelectorAll('#q-options button')]
    .map(b=>b.id).filter(id=>id!=='near-hostgo');
  if(stray.length)
    probs.push('unexpected button(s) on the Closest Wins screen: '+stray.join(', '));
  if(!/qasking/.test($('q-screen').innerHTML))probs.push('the question is not on the screen');

  // the answer must not be on the screen before the reveal
  const right=ev('Q.current[2]');
  if($('q-options').textContent.indexOf(String(right))>=0)
    probs.push('the answer was on the screen before anybody guessed');

  // ---- three guesses, and the closest takes it ----
  ev('nearGuess(S.players[0],'+(right+12)+')');
  if(ev('Q.revealed'))probs.push('one guess ended the round');
  ev('nearGuess(S.players[1],"'+(right-3)+'")');     // a phone sends a string
  if(ev('Q.guesses["1"]')!==right-3)probs.push('a typed number was not read: '+ev('Q.guesses["1"]'));
  // rubbish is ignored rather than scored
  ev('nearGuess(S.players[2],"about twenty")');
  if('2' in JSON.parse(ev('JSON.stringify(Q.guesses)')))probs.push('a guess that was not a number was accepted');
  if(ev('Q.revealed'))probs.push('the round ended before everybody had guessed');
  ev('nearGuess(S.players[2],'+(right+40)+')');
  if(!ev('Q.revealed'))probs.push('the round did not end when everybody had guessed');
  if(score(1)!==10)probs.push('the closest guess scored '+score(1)+', expected 10');
  if(score(0)||score(2))probs.push('a guess that was not closest scored');

  // ---- exactly right is worth double, and a tie shares ----
  ev(`nearNext();const r=Q.current[2];
    nearGuess(S.players[0],r);nearGuess(S.players[1],r);nearGuess(S.players[2],r+500);`);
  // Mia already had 10 from the first round; both get 20 for being exact
  if(score(0)!==20||score(1)!==30)
    probs.push('exactly right paid '+[score(0),score(1)].join(',')+', expected 20 and 30');
  if(score(2))probs.push('a guess 500 out still scored');
  // and the board shows it
  if(!/nearans/.test($('q-options').innerHTML))probs.push('the answer is not shown after the reveal');
  if($('q-options').textContent.indexOf('Henkka')<0)probs.push('the guesses are not listed');

  // ---- nobody guessing pays nobody ----
  const was=[score(0),score(1),score(2)].join(',');
  ev('nearNext();nearReveal();');
  if([score(0),score(1),score(2)].join(',')!==was)probs.push('a question nobody answered paid out');

  // ---- what the phone is told ----
  ev('nearNext();nearGuess(S.players[1],1);');
  let st=JSON.parse(ev('JSON.stringify(nearState("live"))'));
  if(st.right!==null)probs.push('THE ANSWER WAS SENT TO THE PHONES BEFORE THE REVEAL');
  if(st.seats.some(s=>s.guess!==undefined))probs.push('a guess was shown to the other phones early');
  if(!st.seats.some(s=>s.said))probs.push('the phone is not told who has guessed');
  ev('nearReveal();');
  st=JSON.parse(ev('JSON.stringify(nearState("live"))'));
  if(typeof st.right!=='number')probs.push('the answer was not sent after the reveal');

  // ---- and a big number is readable from a sofa ----
  if(ev('fmtNum(1440)').replace(/ /g,' ')!=='1 440')
    probs.push('a thousand is printed as '+ev('fmtNum(1440)'));

  console.log(probs.length?'FAIL:':'ok - Closest Wins: no options, closest takes it, exactly right doubles');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1200);
