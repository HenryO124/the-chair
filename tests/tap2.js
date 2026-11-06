// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// the answer buttons must survive a stage message: replacing them mid-press
// is how a tap gets thrown away
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
function page(hash){
  return new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,
    url:'https://party.test/t/'+(hash||''),
    beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
}
const D=page(),w=D.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
setTimeout(()=>{
  const stage=(round,revealed)=>({v:1,game:'picture',phase:'live',round:round,of:5,
    revealed:!!revealed,correct:revealed?1:-1,vote:null,setup:'',remote:false,vid:'',
    ask:'What is this?',cat:'Landmarks',pic:'https://x/y.jpg?width=500',
    options:['Oslo','Bergen','Tromso','Trondheim'],
    seats:[{id:0,pid:'abcdef',name:'Me',icon:0,photo:'',said:false,pick:-1,score:0,team:[],
            passed:false,full:false,blockUsed:false,total:0,reserved:false}]});
  w.eval("PARTY.role='chair';PARTY.code='ABCD';PARTY.pid='abcdef'");
  w.eval('PARTY.stage='+JSON.stringify(stage(1))+';drawPad()');
  const first=[...d.querySelectorAll('#pad-quiz button')];
  if(first.length!==4)probs.push('expected four answers, got '+first.length);
  // six more stage messages arrive while the player is thinking
  for(let i=0;i<6;i++){w.eval('PARTY.stage='+JSON.stringify(stage(1))+';drawPad()')}
  const after=[...d.querySelectorAll('#pad-quiz button')];
  const same=first.length===after.length&&first.every((b,i)=>b===after[i]);
  if(!same)probs.push('THE ANSWER BUTTONS WERE REPLACED while the question was still open - a tap landing then is lost');
  // a new question must give new buttons with the new words
  const s2=stage(2);s2.options=['Turku','Tampere','Oulu','Vaasa'];
  w.eval('PARTY.stage='+JSON.stringify(s2)+';drawPad()');
  const next=[...d.querySelectorAll('#pad-quiz button')];
  if(next[0]===first[0])probs.push('a new question reused the old buttons');
  if(!/Turku/.test($('pad-quiz').textContent))probs.push('the new question did not reach the phone');
  // the reveal still colours them without rebuilding
  const before=[...d.querySelectorAll('#pad-quiz button')];
  const s3=stage(2,true);s3.options=['Turku','Tampere','Oulu','Vaasa'];
  w.eval('PARTY.stage='+JSON.stringify(s3)+';drawPad()');
  const rev=[...d.querySelectorAll('#pad-quiz button')];
  if(!rev.every((b,i)=>b===before[i]))probs.push('the reveal rebuilt the grid');
  if(!rev[1].className.includes('right'))probs.push('the right answer was not marked: '+rev[1].className);
  if(!rev.every(b=>b.disabled))probs.push('the answers stayed tappable after the reveal');

  // a guest who followed an invitation does not download the menu music
  const G=page('#ABCD'),gw=G.window;
  setTimeout(()=>{
    if(gw.eval('musicOn'))probs.push('an invited guest still preloads the menu music');
    if(!w.eval('musicOn'))probs.push('the host screen lost its music');
    console.log(probs.length?'FAIL:':'ok - the tap survives, the reveal is cheap, no music for a guest');
    probs.forEach(p=>console.log('  x '+p));
    process.exit(probs.length?1:0);
  },700);
},800);
