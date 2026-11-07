// One party, several games, one evening: the game score is the game's, and
// what it adds up to by the end of the night is kept alongside it.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
const MISS={className:'',textContent:'',innerHTML:'',hidden:true};
const $=id=>d.getElementById(id)||(probs.push('there is no '+id+' on the page'),MISS);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled&&el.dispatchEvent)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
const night=n=>w.eval("(S.players.find(function(p){return p.name==='"+n+"'})||{}).night");
const score=n=>w.eval("(S.players.find(function(p){return p.name==='"+n+"'})||{}).score");
setTimeout(()=>{
  // a party of three opens, and nobody has an evening yet
  w.eval(`PARTY.role='host';PARTY.code='TEST';S.game='trivia';
    S.players=[{id:0,name:'Henkka',icon:0,score:0},
               {id:1,name:'Mia',icon:1,pid:'p2',score:0},
               {id:2,name:'Jussi',icon:2,pid:'p3',score:0}];
    S.games=0;S.banked=false;S.players.forEach(function(p){p.night=0});`);

  // --- first game ---
  w.eval(`Q.deck=new Array(5);Q.round=5;Q.revealed=true;Q.current=TRIVIA[0];
    S.players[0].score=30;S.players[1].score=50;S.players[2].score=10;
    quizFinish();`);
  if(w.eval('S.games')!==1)probs.push('the first game was not counted: '+w.eval('S.games'));
  if(night('Mia')!==50)probs.push("Mia's evening did not take the first game: "+night('Mia'));
  if(/Tonight/.test($('final-board').innerHTML))
    probs.push('a single game is shown as if it were an evening of them');
  if(!/50 pts/.test($('final-board').innerHTML))probs.push('the game board is wrong');

  // ending twice must not pay twice
  w.eval('quizFinish();');
  if(night('Mia')!==50)probs.push('ending the game twice paid the evening twice: '+night('Mia'));
  if(w.eval('S.games')!==1)probs.push('ending twice counted two games');

  // --- Play another, in the same room ---
  click($('restart'));
  if(score('Mia'))probs.push("the new game did not start Mia at nought: "+score('Mia'));
  if(night('Mia')!==50)probs.push('Play another threw away the evening: '+night('Mia'));
  if(w.eval('PARTY.code')!=='TEST')probs.push('Play another closed the room');

  // --- second game, and the evening adds up ---
  w.eval(`S.game='s10';Q.deck=new Array(5);Q.round=5;Q.revealed=true;Q.current=s10Bank()[0];
    S.players[0].score=70;S.players[1].score=10;S.players[2].score=20;
    quizFinish();`);
  if(w.eval('S.games')!==2)probs.push('the second game was not counted');
  if(night('Henkka')!==100)probs.push("Henkka's evening is "+night('Henkka')+', not 30+70');
  if(night('Mia')!==60)probs.push("Mia's evening is "+night('Mia')+', not 50+10');
  if(night('Jussi')!==30)probs.push("Jussi's evening is "+night('Jussi')+', not 10+20');

  const board=$('final-board').innerHTML;
  if(!/Tonight/.test(board))probs.push('the evening is nowhere on the final screen');
  if(!/2 games/.test(board))probs.push('the evening does not say how many games');
  if(!/100 pts/.test(board))probs.push("the evening's leader is not shown");
  // the game's own winner is still the game's
  if(!/70 pts/.test(board))probs.push('the game board was replaced by the evening');
  // and the evening is led by the one who won the night, not the last game
  const order=(board.split('Tonight')[1]||'').match(/\d\. [A-Za-zÀ-ÿ]+/g)||[];
  if(order[0]&&!/Henkka/.test(order[0]))
    probs.push('the evening is in the wrong order: '+order.join(', '));

  // --- a new party is a new evening ---
  w.eval('openLobby&&openLobby()');
  if(w.eval('S.games'))probs.push('a new party carried the old evening in: '+w.eval('S.games'));

  console.log(probs.length?'FAIL:':'ok - the evening: each game its own, and a total by the end of the night');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1100);
