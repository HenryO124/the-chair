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
    // Picture Guess, Name the Artist and Point the Finger have no topics at
    // all. For the picture game that is deliberate: the hand-kept list of
    // fourteen was wrong, and a round is better for mixing a mushroom with a
    // cathedral than for serving fifteen mushrooms.
    if(g==='picture'&&keys.length)
      probs.push('picture: the ballot offers topics again — this game has none');
  }

  // ---- with no topics, every picture is always in play ----
  ev("S.game='picture';S.cats=[]");
  const all=ev("catBank().length");
  const rows=ev("PICTURES.length");
  if(all!==rows)probs.push('the picture game deals '+all+' of '+rows+' pictures');
  else console.log('  every one of the '+rows+' pictures is in play, with no topic to exclude it');
  // a category the table has never heard of must still ask something sane
  const ask=ev("(PICASK[S.lang]||PICASK.en)['*']||''");
  if(!ask)probs.push('a picture in an unknown category would be asked nothing at all');

  // ---- an impossible setting must not wedge the game ----
  // a saved setting from an older build can still name a topic with nothing in it
  ev("S.game='picture';S.cats=['Person'];S.len=15");
  try{ev("show('s-quiz');quizStart()")}catch(e){probs.push('an empty topic threw: '+e.message)}
  const deck=ev("Q.deck?Q.deck.length:-1");
  if(deck<1)probs.push('a topic with nothing in it dealt a deck of '+deck+' and the screen is stuck');
  else console.log('  an impossible topic falls back to the whole bank: '+deck+' rounds');


  if(probs.length){console.log('FAIL:');probs.forEach(p=>console.log('  x '+p));process.exit(1)}
  console.log('ok - no topic is offered that cannot be played, and no setting deals nothing');
  process.exit(0);
},600);
