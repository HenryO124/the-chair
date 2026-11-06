// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// a painting from Picture Guess must not follow the room into Name the Artist
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,$=id=>dom.window.document.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
setTimeout(()=>{
  w.eval("S.players=[mkPlayer('A',0,0,'p1')];S.len=3;S.cats=[]");
  // play one Picture Guess question, so a qid is lying around
  w.eval("S.game='picture';quizStart()");
  if(!w.eval('stageState().pic'))probs.push('Picture Guess sent no picture');
  const was=w.eval('JSON.stringify(Q.qid)');
  // now the room switches to Name the Artist
  w.eval("S.game='artist';quizStart()");
  const pic=w.eval('stageState().pic');
  if(pic)probs.push('A PICTURE LEAKED INTO NAME THE ARTIST: '+pic.slice(0,60)+' (qid was '+was+')');
  if(w.eval('Q.qid'))probs.push('the old question id is still set: '+w.eval('JSON.stringify(Q.qid)'));
  // and True or False has no picture either
  w.eval("S.game='tf';quizStart()");
  if(w.eval('stageState().pic'))probs.push('True or False sent a picture');
  // while Picture Guess still does
  w.eval("S.game='picture';quizStart()");
  if(!w.eval('stageState().pic'))probs.push('Picture Guess lost its picture');
  console.log(probs.length?'FAIL:':'ok - pictures stay in the game they belong to');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
