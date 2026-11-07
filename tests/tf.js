// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// True or False: two answers, a run that pays more, and one wrong one resets it
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
setTimeout(()=>{
  if(!d.querySelector('#s-setup [data-game="tf"]'))probs.push('no True or False card on the shelf');
  w.eval("S.game='tf';S.lang='fi';S.len=6;S.cats=[]");
  const bank=w.eval('catBank().length');
  if(bank<20)probs.push('the statement bank is thin: '+bank);
  // every row must offer exactly the two words, and name the right one
  const bad=w.eval("(function(){var b=catBank(),W=TFWORDS.fi,bad=0;"
    +"for(var i=0;i<b.length;i++){if(b[i][2]!==W[0]&&b[i][2]!==W[1])bad++;if(!b[i][6])bad++;}return bad})()");
  if(bad)probs.push(bad+' statements are malformed');
  w.eval('quizStart()');
  if(w.eval('Q.options.length')!==2)probs.push('the phone was offered '+w.eval('Q.options.length')+' answers');
  if(w.eval("Q.options.join('|')")!=='Totta|Tarua')probs.push('the two answers are wrong: '+w.eval("Q.options.join('|')"));
  const c=w.eval('Q.correct');
  if(c!==0&&c!==1)probs.push('no correct answer: '+c);
  // a run of three, then a miss
  w.eval("S.players=[mkPlayer('A',0,0,'pid1')];S.players[0].score=0;S.players[0].run=0");
  const score=()=>w.eval('S.players[0].score'), run=()=>w.eval('S.players[0].run');
  for(let i=0;i<3;i++){
    w.eval('Q.answers={0:Q.correct};Q.order=[0];Q.revealed=false;quizReveal()');
  }
  if(run()!==3)probs.push('the run did not build: '+run());
  if(score()!==10+20+30)probs.push('the run did not pay more: '+score()+' expected 60');
  w.eval('Q.answers={0:(Q.correct===0?1:0)};Q.order=[0];Q.revealed=false;quizReveal()');
  if(run()!==0)probs.push('a wrong answer did not end the run');
  if(score()!==60)probs.push('a wrong answer changed the score: '+score());
  // the quiz is untouched by any of this
  w.eval("S.game='trivia';S.players=[mkPlayer('A',0,0,'pid1')];S.len=4;S.cats=[];quizStart()");
  if(w.eval('Q.options.length')!==4)probs.push('the quiz lost its four answers');
  w.eval('Q.answers={0:Q.correct};Q.order=[0];Q.revealed=false;quizReveal()');
  if(w.eval('S.players[0].score')!==15)probs.push('quiz scoring changed: '+w.eval('S.players[0].score'));
  // the phone draws two big buttons
  w.eval("S.game='tf';PARTY.role='chair';PARTY.pid='pid1'");
  w.eval("PARTY.stage={v:1,game:'tf',phase:'live',round:2,of:6,revealed:false,correct:-1,vote:null,"
    +"setup:'',remote:false,vid:'',ask:'Banaanikasvi on ruoho.',cat:'Tiede',pic:'',"
    +"options:['Totta','Tarua'],seats:[{id:0,pid:'pid1',name:'A',icon:0,photo:'',said:false,pick:-1,"
    +"score:30,run:2,team:[],passed:false,full:false,blockUsed:false,total:30,reserved:false}]};drawPad()");
  const btns=d.querySelectorAll('#pad-quiz button');
  if(btns.length!==2)probs.push('the phone shows '+btns.length+' answers, expected 2');
  if(!$('pad-quiz').className.includes('two'))probs.push('the two answers are not laid out big');
  if($('pad-run').hidden)probs.push('the phone does not show the run');
  // the phone speaks the language the questions are in, so ask the page what
  // that sentence should say rather than assuming English
  const wantRun=w.eval("T('run_row',{n:2,m:30})");
  if($('pad-run').textContent!==wantRun)
    probs.push('the run line is "'+$('pad-run').textContent+'", expected "'+wantRun+'"');
  if(!/2/.test($('pad-run').textContent))probs.push('the run line does not say how long the run is');
  console.log(probs.length?'FAIL:':'ok - True or False plays, the run pays, the quiz is untouched');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
