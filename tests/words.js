// The phone speaks the language the questions are in.
// A Finnish player used to read a Finnish question under the words GENERAL
// KNOWLEDGE and press a button marked "Leave the game".
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
const MISS={textContent:'',hidden:true};
const $=id=>d.getElementById(id)||(probs.push('there is no '+id),MISS);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
setTimeout(()=>{
  if(w.eval('typeof T')!=='function'){
    console.log('FAIL:');console.log('  x this page has no words of its own');process.exit(1);
  }
  // ---- every key the English table has, the other two have as well ----
  const keys=JSON.parse(w.eval('JSON.stringify(Object.keys(EN))'));
  ['fi','sv'].forEach(L=>{
    const have=JSON.parse(w.eval('JSON.stringify(Object.keys(WORDS.'+L+'))'));
    const missing=keys.filter(k=>have.indexOf(k)<0);
    if(missing.length)probs.push(L+' is missing '+missing.length+' of them: '+missing.slice(0,6).join(', '));
    const extra=have.filter(k=>keys.indexOf(k)<0);
    if(extra.length)probs.push(L+' has words English does not: '+extra.join(', '));
  });
  // ---- every hole in an English sentence is in the other two ----
  keys.forEach(k=>{
    const en=w.eval('EN['+JSON.stringify(k)+']');
    const holes=(en.match(/\{\w+\}/g)||[]).sort().join(',');
    ['fi','sv'].forEach(L=>{
      const t=w.eval('WORDS.'+L+'['+JSON.stringify(k)+']');
      if(t===undefined)return;
      const h=(t.match(/\{\w+\}/g)||[]).sort().join(',');
      if(h!==holes)probs.push(L+'.'+k+' has holes '+(h||'none')+', English has '+(holes||'none'));
      if(!String(t).trim())probs.push(L+'.'+k+' is empty');
      if(t===en&&/[a-z]{4}/.test(en)&&k.indexOf('meta')!==0)
        probs.push(L+'.'+k+' is still the English sentence');
    });
  });
  // ---- an unknown key falls back to English rather than vanishing ----
  w.eval("S.lang='fi'");
  if(w.eval("T('no_such_key')")!=='')probs.push('an unknown key returned something');
  if(w.eval("T('reveal')")===w.eval("EN.reveal"))probs.push('Finnish did not replace Reveal');
  w.eval("S.lang='en'");
  if(w.eval("T('reveal')")!==w.eval("EN.reveal"))probs.push('English did not come back');
  // holes are filled, in each language
  ['en','fi','sv'].forEach(L=>{
    w.eval("S.lang='"+L+"'");
    const t=w.eval("T('q_of',{i:3,n:15})");
    if(/\{/.test(t))probs.push(L+' left a hole unfilled: '+t);
    if(t.indexOf('3')<0||t.indexOf('15')<0)probs.push(L+' lost a number: '+t);
  });

  // ---- and the phone really uses them ----
  w.eval(`S.lang='fi';
    PARTY.role='chair';PARTY.code='ABCDEF';PARTY.pid='p2';
    PARTY.stage={v:1,game:'trivia',phase:'live',round:3,of:15,revealed:false,
      ask:'Mikä kaasu?',cat:'Luonnontiede',options:['a','b','c','d'],correct:-1,nextIn:0,
      seats:[{id:1,pid:'p2',name:'Mia',icon:1,score:10}]};
    show('s-chair');
    document.getElementById('chair-join').hidden=true;
    document.getElementById('chair-pad').hidden=false;
    drawPad();dressButtons();`);
  const round=$('pad-round').textContent;
  if(/Question|Record/.test(round))probs.push('the phone still says Question in English: '+round);
  if(round.indexOf('3')<0||round.indexOf('15')<0)probs.push('the round line lost its numbers: '+round);
  if(/general knowledge/i.test($('meta').textContent))
    probs.push('the top bar is still English: '+$('meta').textContent);
  if(/Leave the game/.test($('pad-leave').textContent))
    probs.push('the leave button is still English: '+$('pad-leave').textContent);

  // switching back to English switches the phone back
  w.eval("S.lang='en';drawPad();dressButtons();");
  const back=$('pad-round').textContent;
  if(back!==w.eval("T('cat_q_of',{cat:'Luonnontiede',i:3,n:15})"))
    probs.push('English did not come back on the phone: '+back);
  if(!/question 3 of 15/.test(back))
    probs.push('the English round line is not the English one: '+back);

  console.log(probs.length?'FAIL:':'ok - the phone speaks the language the questions are in');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1100);
