const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const dom=new JSDOM(fs.readFileSync(''+SRC+'','utf8'),
 {runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const probs=[];const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
setTimeout(()=>{
  const hidden=id=>{const e=$(id);return !e||e.hidden};
  [['tf','statements'],['s10','questions'],['trivia','questions'],['picture','pictures']].forEach(([g,word])=>{
    w.eval("S.game='"+g+"';dressRules()");
    if(!hidden('eras'))probs.push(g+': the record years are still on screen');
    if(!hidden('genres'))probs.push(g+': the genre picker is still on screen');
    if(!hidden('teamsize'))probs.push(g+': the team size is still on screen');
    if(hidden('cats'))probs.push(g+': no topics');
    if(hidden('lang'))probs.push(g+': no language picker');
    const lab=$('length').previousElementSibling.textContent.toLowerCase();
    if(lab.indexOf(word)<0)probs.push(g+': the length says "'+lab+'", expected '+word);
    const n=w.eval('catBank().length');
    if(!n)probs.push(g+': the bank is empty');
  });
  w.eval("S.game='chair';dressRules()");
  if(hidden('eras'))probs.push('The Chair lost its years');
  if(hidden('teamsize'))probs.push('The Chair lost its team size');
  console.log(probs.length?'FAIL:':'ok - every game shows its own settings');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
