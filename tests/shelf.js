// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
setTimeout(()=>{
  const card=d.querySelector('#s-setup [data-game="chair"]');
  if(!card)probs.push('the card is gone from the page entirely');
  else if(!card.hidden)probs.push('THE CHAIR IS STILL ON THE SHELF');
  const chip=d.querySelector('#mode-filter [data-g="chair"]');
  if(chip&&!chip.hidden)probs.push('the filter chip is still there');
  const visible=[...d.querySelectorAll('#s-setup .gamecard')].filter(c=>!c.hidden).map(c=>c.dataset.game);
  if(visible.length!==4)probs.push('the shelf shows '+visible.join(',')); 
  click($('m-create'));
  setTimeout(()=>{
    if(w.eval('S.game')==='chair')probs.push('it is still the game that opens by default');
    if(!w.eval("document.querySelector('#s-setup .gamecard.sel:not([hidden])')"))
      probs.push('nothing is selected on the shelf');
    // and it cannot be chosen by accident
    w.eval("pickGame('chair')");
    if(w.eval('S.game')==='chair')probs.push('a shelved game could still be picked');
    // the other four still work
    ['artist','trivia','picture','tf'].forEach(g=>{
      w.eval("pickGame('"+g+"')");
      if(w.eval('S.game')!==g)probs.push(g+' can no longer be picked');
    });
    console.log(probs.length?'FAIL:':'ok - The Chair is off the shelf, the other four play');
    probs.forEach(p=>console.log('  x '+p));
    process.exit(probs.length?1:0);
  },300);
},800);
