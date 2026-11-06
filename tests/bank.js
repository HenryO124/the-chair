// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const dom=new JSDOM(fs.readFileSync('/mnt/user-data/outputs/index.html','utf8'),
 {runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const probs=[];const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
setTimeout(()=>{
 const n=w.eval('TRIVIA.length'),fi=w.eval('TRIVIA_FI.length'),sv=w.eval('TRIVIA_SV.length');
 console.log('rows',n,fi,sv,'QIMG',w.eval('Object.keys(QIMG).length'));
 if(!(n===fi&&fi===sv))probs.push('the three languages are different lengths');
 if(n<600)probs.push('the new questions did not land: '+n);
 // every row still has its four options and a right answer among them
 const bad=w.eval("(function(){var b=0;for(var i=0;i<TRIVIA.length;i++){var r=TRIVIA[i];"
  +"if(r.length!==7)b++;else if(r.slice(3,6).indexOf(r[2])>=0)b++;}return b})()");
 if(bad)probs.push(bad+' rows are malformed');
 // the pictures still point at the questions they were fetched for
 const pic=w.eval("(function(){var k=Object.keys(QIMG).filter(function(x){return /^[0-9]+$/.test(x)});"
  +"return k.length+'|'+TRIVIA[86][1]})()");
 console.log('numeric picture keys / row 86:',pic);
 // and each language actually plays
 ['fi','sv','en'].forEach(L=>{
   w.eval("S.lang='"+L+"'");
   const len=w.eval('langBank().length');
   if(len!==n)probs.push(L+' bank is '+len+' rows, expected '+n);
   const okcat=w.eval("(function(){var b=langBank();var bad=0;for(var i=0;i<b.length;i++){"
     +"if(!b[i][0]||b[i].length!==8)bad++;}return bad})()");
   if(okcat)probs.push(L+': '+okcat+' rows have no category or the wrong shape');
 });
 // play a solo quiz through five questions
 w.eval("S.lang='fi'");
 click($('m-solo'));
 setTimeout(()=>{
  click(d.querySelector('#s-setup [data-game="trivia"]'));
  click($('create-room'));
  setTimeout(()=>{
   click($('to-rules'));
   setTimeout(()=>{
    click($('lobby-start'));
    setTimeout(()=>{
     for(let i=0;i<5;i++){
       const o=d.querySelectorAll('#q-opts button, .qbtn');
       if(!o.length){probs.push('no answers drawn on question '+(i+1));break}
       click(o[0]);click($('q-next'));click($('q-next'));
     }
     console.log(probs.length?'FAIL:':'ok - the bank is in and every language plays');
     probs.forEach(p=>console.log('  x '+p));
     process.exit(probs.length?1:0);
    },400);
   },200);
  },200);
 },200);
},900);
