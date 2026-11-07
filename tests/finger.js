// Point the Finger: a prompt, the room as the answers, and a score for
// agreeing with everybody else.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
const MISS={textContent:'',innerHTML:'',hidden:true,className:''};
const $=id=>d.getElementById(id)||(probs.push('there is no '+id),MISS);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const ev=x=>w.eval(x);
const score=i=>ev('S.players['+i+'].score||0');
setTimeout(()=>{
  if(ev("typeof fingerStart")!=='function'){
    console.log('FAIL:');console.log('  x this page has no Point the Finger');process.exit(1);
  }
  // ---- the bank is real and reads in the language in use ----
  ev("S.lang='fi'");
  const fi=ev('fingerBank()[0][1]'), en=(ev("S.lang='en'"),ev('fingerBank()[0][1]'));
  if(!fi||!en)probs.push('the prompt bank is empty');
  if(fi===en)probs.push('the Finnish prompt is the English one: '+fi);
  if(ev('fingerBank().length')<10)probs.push('only '+ev('fingerBank().length')+' prompts');

  // ---- a round ----
  ev(`S.game='finger';S.lang='en';S.len=5;
    PARTY.role='host';PARTY.code='TESTAA';
    S.players=[{id:0,name:'Henkka',icon:0,score:0},
               {id:1,name:'Mia',icon:1,pid:'p2',score:0},
               {id:2,name:'Jussi',icon:2,pid:'p3',score:0},
               {id:3,name:'Anna',icon:3,pid:'p4',score:0}];
    show('s-quiz');quizStart();`);
  if(ev('Q.deck.length')!==5)probs.push('the deck is '+ev('Q.deck.length')+' prompts, expected 5');
  if(!ev('Q.current'))probs.push('no prompt came up');
  if(ev('Q.revealed'))probs.push('the round opened already revealed');

  // the four answers are the four people
  const btns=[...d.querySelectorAll('#q-options button')];
  if(btns.length!==4)probs.push('the room has 4 people but '+btns.length+' answers');
  const names=btns.map(b=>b.textContent.trim()).join(',');
  if(names.indexOf('Henkka')<0||names.indexOf('Anna')<0)
    probs.push('the answers are not the people: '+names);
  if($('q-ask').textContent!==ev('Q.current[1]'))probs.push('the prompt is not on the screen');

  // ---- three point at Anna, Anna points at Henkka ----
  ev('fingerVote(S.players[0],3)');
  if(ev('Q.revealed'))probs.push('one vote ended the round');
  if(ev('JSON.stringify(Q.votes)')!=='{"0":3}')probs.push('the vote was not recorded: '+ev('JSON.stringify(Q.votes)'));
  // a vote for somebody who is not in the room is ignored
  ev('fingerVote(S.players[1],99)');
  if(ev('Q.votes["1"]')!==undefined)probs.push('a vote for a stranger was accepted');
  ev('fingerVote(S.players[1],3)');
  ev('fingerVote(S.players[2],3)');
  if(ev('Q.revealed'))probs.push('the round ended before everybody had voted');
  ev('fingerVote(S.players[3],0)');
  if(!ev('Q.revealed'))probs.push('the round did not end when everybody had voted');

  // ---- the room picked Anna, so the three who said Anna score ----
  if(score(0)!==10||score(1)!==10||score(2)!==10)
    probs.push('agreeing with the room paid nothing: '+[score(0),score(1),score(2)].join(','));
  if(score(3)!==0)probs.push('Anna scored for pointing at a minority: '+score(3));
  const tally=JSON.parse(ev('JSON.stringify(Q.tally)'));
  if(tally['3']!==3||tally['0']!==1)probs.push('the tally is wrong: '+JSON.stringify(tally));
  // and the screen shows it
  const won=[...d.querySelectorAll('#q-options button.right')];
  if(won.length!==1||won[0].textContent.indexOf('Anna')<0)
    probs.push('the screen does not show who the room picked');
  if(!/3/.test(won[0].textContent))probs.push('the screen does not show the count');

  // ---- nobody voting scores nobody ----
  ev('fingerNext();');
  if(ev('Q.revealed'))probs.push('the next prompt opened revealed');
  if(ev('JSON.stringify(Q.votes)')!=='{}')probs.push('the votes carried over');
  const was=[score(0),score(1),score(2),score(3)].join(',');
  ev('fingerReveal();');
  if([score(0),score(1),score(2),score(3)].join(',')!==was)
    probs.push('a prompt nobody voted on paid out anyway');

  // ---- changing your mind before the reveal is allowed ----
  ev('fingerNext();fingerVote(S.players[0],1);fingerVote(S.players[0],2);');
  if(ev('Q.votes["0"]')!==2)probs.push('a change of mind was refused');
  // but not after
  ev('fingerReveal();fingerVote(S.players[0],1);');
  if(ev('Q.votes["0"]')!==2)probs.push('a vote was taken after the reveal');

  // ---- the phone is sent the room, and who won, and nothing else ----
  const st=JSON.parse(ev('JSON.stringify(fingerState("live"))'));
  if(st.game!=='finger')probs.push('the phone is not told which game this is');
  if(!st.seats||st.seats.length!==4)probs.push('the phone was not sent the room');
  if(st.seats.some(s=>s.name===undefined))probs.push('a seat went out without a name');
  if(JSON.stringify(st).indexOf('"ask"')<0)probs.push('the prompt was not sent');
  if(st.seats.filter(s=>s.won).length<1)probs.push('the phone is not told who the room picked');

  // ---- and the game ends like the others ----
  ev('Q.round=Q.deck.length;');
  ev("$('q-next').click();");
  if(w.eval('screenNow()')!=='s-final')probs.push('the last prompt did not reach the standings');

  console.log(probs.length?'FAIL:':'ok - Point the Finger: the room is the answer, and agreeing with it scores');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1200);
