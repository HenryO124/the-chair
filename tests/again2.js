// Four to seven hours is several games, and a party that asks the same
// question twice in one evening looks broken to the people playing it.
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
const ev=x=>w.eval(x);
setTimeout(()=>{
  if(ev('typeof seenSet')!=='function'){
    console.log('FAIL:');console.log('  x the party remembers nothing between games');process.exit(1);
  }
  ev("S.lang='fi';S.cats=[];S.game='trivia';S.seen={};");

  // ---- a whole evening of one game, on every topic ----
  const ids=d=>JSON.parse(ev('JSON.stringify('+d+'.map(r=>String(r[r.length-1]))) '));
  const bank=ev('catBank().length');
  let all=[],rounds=0;
  for(let i=0;i<4;i++){
    const got=ids('evenDeck(catBank(),30)');
    if(got.length!==30)probs.push('round '+(i+1)+' dealt '+got.length+' questions');
    all=all.concat(got);rounds++;
  }
  const dupes=all.length-new Set(all).size;
  if(dupes)probs.push(rounds+' rounds of 30 from '+bank+' questions repeated '+dupes+' of them');

  // ---- one topic only: the case that used to break inside two rounds ----
  ev("S.seen={};S.cats=['History'];");
  const one=ev('catBank().length');
  let a=ids('evenDeck(catBank(),30)'),b=ids('evenDeck(catBank(),30)');
  const over=a.filter(x=>b.indexOf(x)>=0).length;
  if(over)probs.push('on one topic ('+one+' questions) the second round repeated '+over+' of the first');

  // ---- and it still deals when the bank really is spent ----
  ev("S.seen={};");
  let last=[];
  for(let i=0;i<Math.ceil(one/30)+2;i++)last=ids('evenDeck(catBank(),30)');
  if(last.length!==30)probs.push('once the bank was spent a round dealt '+last.length+' questions');
  if(new Set(last).size!==30)probs.push('the round after the bank was spent repeated itself inside one deck');

  // ---- each game keeps its own memory ----
  ev("S.seen={};S.cats=[];S.game='trivia';");
  const t=ids('evenDeck(catBank(),20)');
  ev("S.game='tf';");
  if(Object.keys(JSON.parse(ev('JSON.stringify(S.seen)'))).length!==1)
    probs.push('switching game did not give the new game its own memory');
  ev("S.game='trivia';");
  const t2=ids('evenDeck(catBank(),20)');
  if(t.filter(x=>t2.indexOf(x)>=0).length)probs.push('coming back to a game forgot what it had asked');

  // ---- a new party starts the evening again ----
  ev("S.game='trivia';");
  const before=Object.keys(JSON.parse(ev('JSON.stringify(S.seen)'))).length;
  if(!before)probs.push('nothing was remembered at all');

  console.log(probs.length?'FAIL:':'ok - an evening of several games does not ask the same question twice');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1300);
