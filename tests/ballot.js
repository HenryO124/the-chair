// A topic on the ballot must have rounds behind it, and a game must never
// deal nothing.
//
// "Kuuluisa henkilö" sat in the picture table with no pictures behind it. It
// was kept out of the ballot by a second list, written by hand, which is the
// arrangement that has already gone wrong three times in this page. Now the
// ballot is read off the pictures themselves.
const path=require("path"),fs=require('fs'),{JSDOM}=require('jsdom');
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const probs=[];
const dom=new JSDOM(fs.readFileSync(SRC,'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,ev=x=>w.eval(x);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
setTimeout(()=>{
  ev("S.lang='fi';S.players=[{id:'a',name:'A',score:0},{id:'b',name:'B',score:0}]");

  // ---- every topic offered must have rounds behind it, in every game ----
  for(const g of ['picture','trivia','tf','s10','near']){
    ev("S.game='"+g+"';S.cats=[];S.len=10");
    const keys=JSON.parse(ev("JSON.stringify(ballot())"));
    for(const k of keys){
      ev("S.cats=['"+k+"']");
      const n=ev("catBank().length");
      if(!n)probs.push(g+': the ballot offers "'+k+'" and nothing is behind it');
    }
    if(g==='picture'&&!keys.length)probs.push('picture: the ballot is empty');
  }

  // ---- a category in the table with no rounds may not reach the ballot ----
  ev("S.game='picture';S.cats=[]");
  const offered=JSON.parse(ev("JSON.stringify(ballot())"));
  const counts=JSON.parse(ev("JSON.stringify(PICTURES.reduce((m,r)=>((m[r[0]]=(m[r[0]]||0)+1),m),{}))"));
  const empty=Object.keys(JSON.parse(ev("JSON.stringify(PICCAT.en)"))).filter(k=>!counts[k]);
  for(const k of empty)
    if(offered.indexOf(k)>=0)probs.push('"'+k+'" has no pictures and is on the ballot anyway');
  // and one that does have rounds must not be left off
  for(const k of Object.keys(counts))
    if(counts[k]>0&&offered.indexOf(k)<0&&(k in JSON.parse(ev("JSON.stringify(PICCAT.en)"))))
      probs.push('"'+k+'" has '+counts[k]+' pictures and is missing from the ballot');

  // ---- an impossible setting must not wedge the game ----
  // a saved setting from an older build can still name a topic with nothing in it
  ev("S.game='picture';S.cats=['Person'];S.len=15");
  try{ev("show('s-quiz');quizStart()")}catch(e){probs.push('an empty topic threw: '+e.message)}
  const deck=ev("Q.deck?Q.deck.length:-1");
  if(deck<1)probs.push('a topic with nothing in it dealt a deck of '+deck+' and the screen is stuck');
  else console.log('  an impossible topic falls back to the whole bank: '+deck+' rounds');

  console.log('  ballot offers '+offered.length+' picture topics, every one with rounds behind it');
  if(probs.length){console.log('FAIL:');probs.forEach(p=>console.log('  x '+p));process.exit(1)}
  console.log('ok - no topic is offered that cannot be played, and no setting deals nothing');
  process.exit(0);
},600);
