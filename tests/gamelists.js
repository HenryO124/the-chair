// Nothing in this page may decide how a game behaves by keeping a list of the
// games that behave that way. Twice in one day a new game was left out of such
// a list: Closest Wins told a room it was choosing a decade and a genre, and
// its phones showed the chair game's team sheet instead of a box to type a
// guess into. Every check here derives what it wants from GAMELABEL, so the
// ninth game fails these tests instead of failing in front of a room.
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
const q=x=>JSON.parse(ev('JSON.stringify('+x+')'));
const shown=id=>{const e=d.getElementById(id);return !!e&&!e.hidden};
const txt=id=>{const e=d.getElementById(id);return e?e.textContent:''};
const J=JSON.stringify;

setTimeout(()=>{
  const games=q('Object.keys(GAMELABEL)');
  if(games.length<7){
    console.log('FAIL:');console.log('  x only '+games.length+' games to check');process.exit(1);
  }
  // The two closed sets this page really turns on. Neither will grow: a record
  // needs a catalogue and a video, and the chair game is the only one that
  // builds teams. Everything else is "one of the games that asks a question",
  // which is the list that keeps being forgotten.
  const RECORDS={artist:1,chair:1};
  const CHAIRGAME={chair:1};
  const NOTOPICS={finger:1};            // its questions are about the room
  games.forEach(g=>{if(!(g in RECORDS)&&ev('playsRecords.toString()').indexOf(J(g))>=0)
    probs.push(g+' plays records but this test did not expect it to')});

  // ---- 1. the phone gets the pad its game needs ----------------------------
  // the chair game's team sheet belongs to the chair game. Any other game that
  // reaches it has fallen through a list it was left out of.
  const CHAIRSHEET=['pad-sign','pad-skip','pad-team','pad-teamhead','pad-myteam'];
  games.forEach(g=>{
    ev(`S.lang='en';PARTY.role='chair';PARTY.code='ABCDEF';PARTY.pid='p2';
      padNear=null;padFinger=null;padNearRound=-1;padFingerRound=-1;
      PARTY.stage={v:1,b:(typeof BUILD==='undefined'?'':BUILD),game:${J(g)},phase:'live',
        round:1,of:5,revealed:false,correct:-1,nextIn:0,right:null,vote:null,setup:'',
        remote:false,vid:'',prev:'',pic:'',ask:'How many?',cat:'History',
        options:['a','b','c','d'],cands:[],turn:null,turnName:'',
        seats:[{id:1,pid:'p2',name:'Mia',icon:1,score:0,said:false,pick:-1,run:0,
                pot:0,picks:0,st:'in',team:[],passed:false,full:false,
                blockUsed:false,total:0,reserved:false}]};
      show('s-chair');
      document.getElementById('chair-join').hidden=true;
      document.getElementById('chair-pad').hidden=false;`);
    try{ev('drawPad()')}catch(e){probs.push(g+': drawPad threw on a phone: '+e.message);return}
    const sheet=CHAIRSHEET.filter(shown);
    if(g in CHAIRGAME){
      if(!sheet.length)probs.push(g+': the phone lost the team sheet');
    }else{
      if(sheet.length)
        probs.push(g+": the phone was shown the chair game's "+sheet.join(', ')
          +' — it fell through to the chair game');
      if(!shown('pad-quiz')&&!shown('pad-nearbox'))
        probs.push(g+': the phone has nothing to answer with');
      if(/audition|record/i.test(txt('pad-round')))
        probs.push(g+': the phone counts records: "'+txt('pad-round')+'"');
    }
  });

  // ---- 2. the final screen counts what was actually played ----------------
  games.forEach(g=>{
    ev(`S.game=${J(g)};S.lang='en';S.games=1;S.banked=false;
      S.players=[{id:0,name:'Henkka',icon:0,score:30}];
      Q.on=true;Q.round=3;Q.revealed=true;Q.deck=[1,2,3];Q.answers={};`);
    try{ev('quizFinish()')}catch(e){probs.push(g+': quizFinish threw: '+e.message);return}
    const rec=!!RECORDS[g];
    const sub=txt('champ-sub'), eye=txt('final-eyebrow');
    if(/record/i.test(sub)!==rec)
      probs.push(g+': the final line says "'+sub+'" — only a record game counts records');
    if(/sharpest ear/i.test(eye)!==rec)
      probs.push(g+': the final eyebrow is "'+eye+'" — a sharp ear is for the records');
    if(!eye.trim())probs.push(g+': the final screen has no eyebrow');
  });

  // ---- 3. what the room is told is on the table ---------------------------
  // this is the line every phone reads while the host is still deciding
  games.forEach(g=>{
    ev(`S.game=${J(g)};S.lang='en';S.cats=[];S.len=5;S.era=0;S.genre='Random';S.remote=false;`);
    const line=ev('setupLine()');
    const rec=!!RECORDS[g];
    ['year','genre','audition','record'].forEach(word=>{
      if(!rec&&new RegExp(word,'i').test(line))
        probs.push(g+' is offered "'+word+'" in "'+line+'" — that belongs to the records');
    });
    if(rec&&!(/year/i.test(line)&&/genre/i.test(line)))
      probs.push(g+': a record game is not offered a decade and a genre: "'+line+'"');
    if(!rec&&!/in English/.test(line))
      probs.push(g+': the room is not told what language it is being asked in: "'+line+'"');
    if(line.indexOf(ev('GAMELABEL['+J(g)+']'))!==0)
      probs.push(g+': the line does not start with the game: "'+line+'"');
  });

  // ---- 4. the topics on the ballot and the topics on the screen agree -----
  // two lists, kept by hand in two places, is how one of them goes stale
  games.forEach(g=>{
    ev(`S.lang='en';S.game=${J(g)};PARTY.role='host';PARTY.code='TESTAA';
      S.players=[{id:0,name:'Henkka',icon:0,score:0}];dressRules();`);
    const keys=q('ballot()');
    const box=shown('cats');
    if(!!keys.length!==box)
      probs.push(g+': the topics box is '+(box?'offered':'hidden')+' but the ballot has '
        +keys.length+' topics');
    const wantTopics=!RECORDS[g]&&!NOTOPICS[g];
    if(!!keys.length!==wantTopics)
      probs.push(g+': the ballot has '+keys.length+' topics, expected '+(wantTopics?'some':'none'));
  });

  // ---- 5. a game deals from its own bank ---------------------------------
  // catBank() is what the settings screen counts to decide whether there is a
  // game to start. A game left out of it is counted against somebody else's
  // questions, and a game added tomorrow would be counted against the quiz's.
  games.filter(g=>!RECORDS[g]).forEach(g=>{
    ev(`S.game=${J(g)};S.lang='en';S.cats=[];S.len=5;SOLO=true;
      S.players=[mkPlayer('A',0,0,'')];Q.on=false;`);
    let ids;
    try{ids=q('catBank().map(rowId)')}catch(e){probs.push(g+': catBank() threw: '+e.message);return}
    if(!ids.length){probs.push(g+': catBank() has nothing in it');return}
    try{ev("show('s-quiz');quizStart()")}catch(e){probs.push(g+': quizStart threw: '+e.message);return}
    const deck=q('Q.deck.map(rowId)');
    if(!deck.length){probs.push(g+': no deck was dealt');ev('Q.on=false');return}
    const stray=deck.filter(x=>ids.indexOf(x)<0);
    if(stray.length)
      probs.push(g+': '+stray.length+' of '+deck.length
        +' rows it deals are not in catBank() — it deals from a bank catBank() does not know');
    ev('Q.on=false');
  });

  // ---- 6. the big screen names what it is counting ------------------------
  // the chair game is the only one the chair engine runs, and that is a closed
  // list of one; every other game comes up on the quiz screen
  games.filter(g=>!CHAIRGAME[g]).forEach(g=>{
    ev(`S.game=${J(g)};S.lang='en';S.cats=[];S.len=5;SOLO=true;S.remote=false;
      S.era=0;S.genre='Random';
      S.players=[mkPlayer('A',0,0,''),mkPlayer('B',1,1,''),mkPlayer('C',2,2,'')];
      S.players.forEach((p,i)=>{p.id=i});Q.on=false;`);
    try{ev("show('s-quiz');quizStart()")}catch(e){probs.push(g+': quizStart threw: '+e.message);return}
    if(!ev('Q.current')){probs.push(g+': no question came up');ev('Q.on=false');return}
    const rec=!!RECORDS[g];
    const count=txt('q-count'), ask=txt('q-ask');
    if(/record|audition/i.test(count)!==rec)
      probs.push(g+': the round line says "'+count+'" — only a record game counts records');
    if(!rec&&/who is this/i.test(ask))
      probs.push(g+': the screen asks "'+ask+'", which is what you ask of a record');

    // ---- 7. and the phones are sent what this game actually has ----------
    let st;
    try{st=q('stageState()')}catch(e){probs.push(g+': stageState threw: '+e.message);ev('Q.on=false');return}
    if(!!String(st.ask||'').trim()===rec)
      probs.push(g+': the stage sent to the phones has ask='+J(st.ask)
        +' — a record game sends no written question and every other game does');
    if(!rec&&String(st.vid||st.prev||'').trim())
      probs.push(g+': the stage carries a record, and this game plays none');
    if(st.game!==g)
      probs.push(g+': the stage sent to the phones calls the game '+J(st.game));
    const mine=q('Q.options');
    // a written question's answers are words. A game dealt from the record
    // catalogue instead would put whole catalogue rows on the buttons.
    if(!rec&&!mine.every(o=>typeof o==='string'))
      probs.push(g+': the answers on the screen are not words: '+J(mine[0]));
    (st.options||[]).forEach((o,i)=>{
      if(!rec&&J(o)!==J(mine[i]))
        probs.push(g+': the phones were sent the option '+J(o)
          +' where the screen shows '+J(mine[i]));
    });
    // on the reveal, a written answer is a name and nothing else
    try{ev('quizReveal()')}catch(e){}
    try{
      const st2=q('stageState()');
      if(!rec&&st2.act&&String(st2.act.track||'').trim())
        probs.push(g+': the reveal sent the phones a record track: '+J(st2.act.track));
    }catch(e){}
    ev('Q.on=false');
  });

  // ---- 8. the start button is not held shut by the record collection ------
  // 2000s dance has no records in the catalogue. A room that played Name the
  // Artist and then picked another game used to find Start dead, because the
  // other game was still being asked whether the record pool was empty.
  // Find an empty era-and-genre combination rather than naming one: the
  // catalogue grows, and the pair that was empty this morning has records in
  // it tonight. The test is about the Start button, not about which corner of
  // the collection happens to be bare.
  let DEADPOOL=null;
  outer:
  for(const era of JSON.parse(ev('JSON.stringify(ERAS)')).concat([2010,2020])){
    for(const genre of JSON.parse(ev('JSON.stringify(Object.keys(FAMILIES))'))){
      if(ev(`poolFor(${era},${J(genre)}).length`)===0){DEADPOOL={era,genre};break outer}
    }
  }
  if(!DEADPOOL)
    probs.push('every era and genre now has records — this test needs an empty one, '
      +'so give it a genre the catalogue does not cover');
  DEADPOOL=DEADPOOL||{era:2000,genre:'Dance'};
  games.filter(g=>!RECORDS[g]).forEach(g=>{
    ev(`S.game=${J(g)};S.lang='en';S.cats=[];S.len=5;
      S.era=${DEADPOOL.era};S.genre=${J(DEADPOOL.genre)};
      S.players=[{id:0,name:'Henkka',icon:0,score:0}];
      try{updateStartState()}catch(e){}`);
    const b=d.getElementById('lobby-start');
    if(b&&b.disabled)
      probs.push(g+': Start is dead because the record pool is empty, and this game plays no records');
  });
  ev("S.era=0;S.genre='Random'");

  console.log(probs.length?'FAIL:':'ok - no game is handled by being named in a list of the others');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1400);
