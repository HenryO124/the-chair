// Every game needs a row in each of the tables that are kept by game id: a
// name, an icon, a blurb on each of the two menus, a label for the top bar in
// three languages, a card on the shelf and a chip on the front page's filter.
// All of those are hand-kept lists, and a game added to GAMELABEL and left out
// of one of them is a game with no card, no icon or a blank top bar. This asks
// the page for its games rather than keeping a list.
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
const J=JSON.stringify;

setTimeout(()=>{
  const games=q('Object.keys(GAMELABEL)');
  if(games.length<7){
    console.log('FAIL:');console.log('  x only '+games.length+' games to check');process.exit(1);
  }
  const shelved=q('SHELVED');

  // ---- the tables the page looks a game up in ----
  // name -> what a missing row costs the room
  const TABLES={
    GAMELABEL:'the room list and the line every phone reads would call it "A game"',
    GAMEICON:'the front page would draw it with the chair game’s icon',
    GAMEBLURB:'its card on the shelf would be unpickable — pickGame() refuses a game that is not in it',
    SOLOBLURB:'the one-screen menu would say nothing about it',
    METALABEL:'the top bar would be blank'
  };
  const gone=[];
  Object.keys(TABLES).forEach(t=>{
    // these get reorganised; one that has gone is not this test's business,
    // but say so, so nobody reads a pass as cover it no longer gives
    if(ev('typeof '+t)==='undefined'){gone.push(t);return}
    const have=q('Object.keys('+t+')');
    games.forEach(g=>{
      if(have.indexOf(g)<0)probs.push(g+' has no row in '+t+': '+TABLES[t]);
    });
    have.forEach(k=>{
      if(games.indexOf(k)<0)probs.push(t+' has a row for "'+k+'", which is not a game');
    });
  });

  // ---- the words a game needs, in all three languages ----
  // meta_<game>  the top bar, which the phone falls back to METALABEL for
  // blurb_<game> its card on the menu for a room full of phones
  // solo_<game>  its card on the one-screen menu
  const WORDKEYS={meta:'words for the top bar',blurb:'a blurb for its card on the menu',
    solo:'a blurb for its card on the one-screen menu'};
  ['en','fi','sv'].forEach(L=>{
    games.forEach(g=>{
      Object.keys(WORDKEYS).forEach(pre=>{
        const own=ev('(function(){S.lang='+J(L)+';return T('+J(pre+'_')+'+'+J(g)+')||""})()');
        if(String(own).trim())return;
        // the top bar has a second place to look; nothing else does
        if(pre==='meta'&&String(ev('METALABEL&&METALABEL['+J(g)+']||""')).trim()){
          if(!shelved[g])
            probs.push(g+' is missing '+WORDKEYS[pre]+' in '+L+' ('+pre+'_'+g
              +'), only the English METALABEL fallback');
          return;
        }
        probs.push(g+' is missing '+WORDKEYS[pre]+' in '+L+' ('+pre+'_'+g+')');
      });
    });
  });
  ev("S.lang='en'");

  // ---- a card on the shelf, and a chip on the front page's filter ----
  games.forEach(g=>{
    const card=d.querySelector('#s-setup .gamecard[data-game="'+g+'"]');
    if(!card){probs.push(g+' has no card on the shelf (#s-setup .gamecard[data-game="'+g+'"])');}
    else if(!!shelved[g]!==!!card.hidden)
      probs.push(g+': its card is '+(card.hidden?'hidden':'on the shelf')
        +' and SHELVED says the other');
    const chip=d.querySelector('#mode-filter [data-g="'+g+'"]');
    if(!chip)probs.push(g+' has no chip on the front page filter (#mode-filter [data-g="'+g+'"])');
    else if(!!shelved[g]!==!!chip.hidden)
      probs.push(g+': its filter chip is '+(chip.hidden?'hidden':'shown')
        +' and SHELVED says the other');
  });

  // ---- and a game the host can actually pick ----
  // seated first: a game with a minimum refuses to be picked by an empty room,
  // and that is the point of the minimum rather than a fault
  const need=g=>{try{return ev('(typeof MINPLAYERS==="undefined"?0:(MINPLAYERS['+J(g)+']||0))')}catch(e){return 0}};
  games.filter(g=>!shelved[g]).forEach(g=>{
    const n=Math.max(need(g),1);
    ev("S.players=[];for(let i=0;i<"+n+";i++)S.players.push({id:i,name:'P'+i,icon:i,score:0,"
      +"team:[],passed:false,blockUsed:false});S.game='trivia';LEARNING=false;SOLO=false;"
      +"pickGame("+J(g)+")");
    if(ev('S.game')!==g)
      probs.push(g+' cannot be picked with '+n+' in the room: pickGame() left the game on '+ev('S.game'));
  });

  console.log(probs.length?'FAIL:':'ok - every game has a row in every table that is keyed by game'
    +(gone.length?' (no '+gone.join(', ')+' in this page any more)':''));
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1200);
