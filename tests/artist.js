// Name the Artist looks a record up by its artist's name. A one-word act name
// sits inside a great many other act names, and 55 of the acts in this
// collection have one-word names — so a careless match plays the wrong record
// under the right name, and the room cannot tell.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const probs=[];
const dom=new JSDOM(fs.readFileSync(SRC,'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window;
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const score=(a,b)=>w.eval('nameScore('+JSON.stringify(a)+','+JSON.stringify(b)+')');
setTimeout(()=>{
  if(typeof w.eval('typeof nameScore')!=='string'||w.eval('typeof nameScore')!=='function'){
    console.log('FAIL:');console.log('  x there is no artist matching at all');process.exit(1);
  }
  // ---- the same act, written differently, is still the same act ----
  [['The Beatles','Beatles'],['Beatles','The Beatles'],['ABBA','ABBA'],
   ['Beyonce','Beyoncé'],['Simon & Garfunkel','Simon and Garfunkel'],
   ['Macklemore','Macklemore & Ryan Lewis'],['Gloria Estefan','Gloria Estefan & Miami Sound Machine'],
   // iTunes writes these without the dots; the owner's own check turned up
   // Run-D.M.C. as "missing" when the record is plainly there
   ['Run-D.M.C.','RUN DMC'],['Run-D.M.C.','Run-DMC'],['Salt-N-Pepa','Salt N Pepa'],
   ['AC/DC','AC DC'],['R.E.M.','REM'],
  ].forEach(([a,b])=>{
    if(score(a,b)!==2)probs.push('"'+a+'" no longer matches "'+b+'" (scored '+score(a,b)+')');
  });
  // ---- a different act is a different act, however the name starts ----
  [['Prince','Prince Royce'],['Cher','Cher Lloyd'],['Europe','Europe 2000'],
   ['Ghost','Ghost Hounds'],['Queen','Queen Latifah'],['Alabama','Alabama Shakes'],
   ['Kiss','Kiss Daniel'],['Garbage','Garbage Truck Band'],
  ].forEach(([a,b])=>{
    if(score(a,b)===2)probs.push('"'+a+'" is taken for "'+b+'" — that plays the wrong record');
  });
  // ---- every one-word act in the real collection, against an impostor ----
  let ones=0,bad=0;
  const cat=JSON.parse(w.eval('JSON.stringify(CATALOG.map(r=>r[0]))'));
  cat.forEach(name=>{
    if(String(name).trim().split(/\s+/).length!==1)return;
    ones++;
    ['Hounds','Royce','Lloyd','Experience','Tribute Band'].forEach(tail=>{
      if(score(name,name+' '+tail)===2){bad++;
        if(bad<4)probs.push('"'+name+'" matches "'+name+' '+tail+'"');}
    });
  });
  if(ones<20)probs.push('only '+ones+' one-word acts found — is the collection loaded?');
  if(bad)probs.push(bad+' one-word acts in the collection still match an impostor');

  console.log(probs.length?'FAIL:':'ok - a record is matched to its own artist and not to a namesake ('+ones+' one-word acts checked)');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1400);
