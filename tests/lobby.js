// The settings screen must offer what the chosen game actually has. Five times
// in one day a new game was left out of a hand-kept list of game ids, and the
// last of them put a choice of decade and musical genre in front of a room
// playing Closest Wins. Ask the page for its games rather than keeping a list.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const probs=[];
const dom=new JSDOM(fs.readFileSync(SRC,'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const ev=x=>w.eval(x);
const shown=id=>{const e=d.getElementById(id);return !!e&&!e.hidden};
setTimeout(()=>{
  const games=JSON.parse(ev('JSON.stringify(Object.keys(GAMELABEL))'));
  if(games.length<7)probs.push('only '+games.length+' games to check');
  const RECORDS={artist:1,chair:1};        // the only two that play a record
  // Point the Finger asks about the room; Picture Guess deliberately has no
  // topics at all, so its settings screen must not offer an empty box.
  const NOTOPICS={finger:1,picture:1};
  games.forEach(g=>{
    ev("S.lang='fi';S.game="+JSON.stringify(g)+";PARTY.role='host';PARTY.code='TESTAA';"+
       "S.players=[{id:0,name:'Henkka',icon:0,score:0}];dressRules();");
    const rec=!!RECORDS[g];
    // decades and genres belong to the record collection and nothing else
    ['eras','genres','pool'].forEach(id=>{
      if(shown(id)!==rec)
        probs.push(g+': "'+id+'" is '+(shown(id)?'offered':'hidden')+' and should be the other way round');
    });
    // topics belong to every game whose questions are written, bar Point the Finger
    const wantTopics=!rec&&!NOTOPICS[g];
    if(shown('cats')!==wantTopics)
      probs.push(g+': topics are '+(shown('cats')?'offered':'hidden')+', expected the other');
    // and every one of them is asked in a language
    if(shown('lang')===rec)
      probs.push(g+': the question language is '+(shown('lang')?'offered':'hidden')+', expected the other');
    // the length label must name what is being counted
    const lab=d.getElementById('length')&&d.getElementById('length').previousElementSibling;
    const t=lab?lab.textContent:'';
    if(!rec&&/record|audition/i.test(t))
      probs.push(g+': the length question still counts records: "'+t+'"');
    if(!t.trim())probs.push(g+': the length question has no label');
  });
  console.log(probs.length?'FAIL:':'ok - the settings screen offers what the chosen game has');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1300);
