// After the reveal, the phone shows what everybody guessed.
//
// The television has always shown the board. The phone had every number it
// needed in the stage it was already being sent, and drew none of it: the
// person holding it saw their own guess and nothing else, which is the half of
// Closest Wins worth watching.
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
  ev("S.lang='fi'");
  const stage=g=>({v:1,game:'near',phase:'live',round:3,of:15,revealed:g,
    ask:'Montako päivää talvisota kesti?',cat:'Historia',right:g?105:null,note:'',
    options:[],correct:-1,seats:[
      {id:'a',name:'Henkka',icon:0,score:0,said:1,guess:g?100:undefined},
      {id:'b',name:'Mia',icon:1,score:0,said:1,guess:g?105:undefined},
      {id:'c',name:'Eero',icon:2,score:0,said:1,guess:g?300:undefined}]});

  // ---- before the reveal nothing may leak ----
  ev("drawPadNear("+JSON.stringify(stage(false))+",{id:'a',name:'Henkka'})");
  if(d.querySelectorAll('#pad-quiz .pnrow').length)
    probs.push('the phone shows the other guesses before the reveal');

  // ---- after it, everyone, nearest first ----
  ev("drawPadNear("+JSON.stringify(stage(true))+",{id:'a',name:'Henkka'})");
  const rows=[...d.querySelectorAll('#pad-quiz .pnrow')];
  if(rows.length!==3){probs.push('the phone shows '+rows.length+' guesses, expected 3')}
  else{
    const names=rows.map(r=>r.querySelector('.pnn').textContent);
    if(names.join(',')!=='Mia,Henkka,Eero')
      probs.push('wrong order, nearest first: '+names.join(', '));
    if(!rows[0].className.includes('win'))probs.push('the closest guess is not marked as the winner');
    if(rows[1].className.includes('win'))probs.push('somebody who did not win is marked as winner');
    const me=rows.filter(r=>r.className.includes('me')).map(r=>r.querySelector('.pnn').textContent);
    if(me.join()!=='Henkka')probs.push('"me" is marked on: '+(me.join()||'nobody'));
    if(rows[0].querySelector('.pnd').textContent.indexOf('täsmälleen')<0)
      probs.push('an exact guess is not called exact: '+rows[0].querySelector('.pnd').textContent);
    if(rows[2].querySelector('.pnd').textContent.indexOf('195')<0)
      probs.push('the distance is wrong on the far guess: '+rows[2].querySelector('.pnd').textContent);
    console.log('  '+names.map((n,i)=>n+' '+rows[i].querySelector('.png').textContent
      +' ('+rows[i].querySelector('.pnd').textContent+')').join('   '));
  }
  // ---- a phone that never guessed still sees the board ----
  ev("drawPadNear("+JSON.stringify(stage(true))+",{id:'z',name:'Myöhäinen'})");
  if(d.querySelectorAll('#pad-quiz .pnrow').length!==3)
    probs.push('somebody who did not guess cannot see the board either');
  if(d.querySelectorAll('#pad-quiz .pnrow.me').length)
    probs.push('a phone that did not guess has a row marked as its own');

  if(probs.length){console.log('FAIL:');probs.forEach(p=>console.log('  x '+p));process.exit(1)}
  console.log('ok - after the reveal every phone shows every guess, nearest first');
  process.exit(0);
},500);
