// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
setTimeout(()=>{
  if(!$('nav-set'))probs.push('no Settings in the nav');
  click($('nav-set'));
  if($('setover').hidden)probs.push('the settings card did not open');
  // the language it opens on is the one in use
  const on=[...d.querySelectorAll('#set-lang button')].filter(b=>b.className.includes('sel'));
  if(on.length!==1||on[0].dataset.g!==w.eval('S.lang'))
    probs.push('the card does not show the language in use: '+on.map(b=>b.dataset.g));
  // switching it switches the questions
  click(d.querySelector('#set-lang [data-g="sv"]'));
  if(w.eval('S.lang')!=='sv')probs.push('the language did not change');
  const q=w.eval('langBank()[0][2]');
  if(!q||w.eval('TRIVIA[0][1]')===w.eval('langBank()[0][2]'))
    probs.push('the Swedish bank reads the same as the English one');
  // the lobby's own picker agrees
  const lob=[...d.querySelectorAll('#lang button')].filter(b=>b.className.includes('sel'));
  if(!lob.length||lob[0].dataset.g!=='sv')probs.push('the lobby picker disagrees: '+lob.map(b=>b.dataset.g));
  // and it is remembered
  if(w.localStorage.getItem('thechair.lang')!=='sv')probs.push('the choice was not remembered');
  // the name
  $('set-name').value='Henry';
  $('set-name').dispatchEvent(new w.Event('change'));
  if(!/Henry/.test($('me-name').textContent))probs.push('the name did not reach the chip');
  // music off
  click(d.querySelector('#set-music [data-m="off"]'));
  if(w.eval('musicOn'))probs.push('music did not turn off');
  click($('set-close'));
  if(!$('setover').hidden)probs.push('the card would not close');
  console.log(probs.length?'FAIL:':'ok - settings: language, name, music');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
