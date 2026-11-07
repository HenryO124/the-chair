// The same people come back on Monday. A memory that lasts one evening would
// send them Saturday's questions again, which is the thing it was written to
// stop — so it lives on the screen, not in the party.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
// one browser, kept between the two parties, exactly like a television
const store={};
const localStorage={getItem:k=>(k in store?store[k]:null),
                    setItem:(k,v)=>{store[k]=String(v)},
                    removeItem:k=>{delete store[k]},clear:()=>{for(const k in store)delete store[k]}};
function party(tag){
  const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
    beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}});
      Object.defineProperty(w,'localStorage',{value:localStorage,configurable:true});}});
  dom.window.addEventListener('error',e=>probs.push(tag+' JS error: '+e.message));
  return dom;
}
const ids=(w,n)=>JSON.parse(w.eval('JSON.stringify(evenDeck(catBank(),'+n+').map(r=>String(r[r.length-1])))'));
const sat=party('saturday');
setTimeout(()=>{
  const w=sat.window;
  if(w.eval('typeof forgetSeen')!=='function')
    probs.push('there is no way to forget what the screen has been asked');
  // one topic, so the pool is small enough for every claim below to be certain
  w.eval("S.lang='fi';S.cats=['History'];S.game='trivia';");
  const pool=w.eval('catBank().length');
  if(pool<100)probs.push('only '+pool+' questions in the topic — the test cannot be sure of anything');
  const night1=ids(w,40).concat(ids(w,40));
  if(night1.length-new Set(night1).size)probs.push('Saturday repeated itself');
  if(!store['thechair.seen'])probs.push('Saturday remembered nothing to the screen');

  // Monday: a brand new page, a brand new party, the same television
  const mon=party('monday');
  setTimeout(()=>{
    const m=mon.window;
    m.eval("S.lang='fi';S.cats=['History'];S.game='trivia';");
    // a new party resets the evening, and must NOT reset the memory
    try{m.eval('newParty&&newParty()')}catch(e){}
    m.eval("S.game='trivia';");
    const night2=ids(m,40);
    const again=night2.filter(x=>night1.indexOf(x)>=0);
    if(again.length)probs.push('Monday asked '+again.length+' of Saturday\'s questions again');
    // a second game on Monday keeps its own memory
    m.eval("S.game='tf';");
    const tf=ids(m,20);
    if(!tf.length)probs.push('a game with no history of its own dealt nothing');
    // and the screen can be told to forget
    m.eval("S.game='trivia';forgetSeen()");   // back to the game we were measuring
    if(Object.keys(JSON.parse(store['thechair.seen']||'{}')).length)
      probs.push('forgetting did not clear the screen');
    // the topic holds about 134, and Saturday saw 80 of them, so a fresh deal
    // of 100 after forgetting must bring some of them back
    const after=ids(m,100);
    const back=after.filter(x=>night1.indexOf(x)>=0).length;
    if(!back)probs.push('after forgetting, not one of the old questions came back');

    console.log(probs.length?'FAIL:':'ok - Monday does not ask what Saturday already asked');
    probs.forEach(p=>console.log('  x '+p));
    process.exit(probs.length?1:0);
  },1300);
},1300);
