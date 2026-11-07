// Items 1-10: what a room sees from the sofa.
// Sizes are proven by a real browser; what jsdom can hold on to is the
// structure that makes those sizes apply, so that is what is nailed down here.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
// a missing element is a finding, not a crash
const MISS={className:'',textContent:'',hidden:true,missing:true};
const $=id=>d.getElementById(id)||(probs.push('there is no '+id+' on the page'),MISS);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const css=html.slice(html.indexOf('<style'),html.indexOf('</style>'));
setTimeout(()=>{
  // ---- 5. Hold is a pill in the row, not a full-width band under it ----
  if(!/#q-hold\{[^}]*width:auto/.test(css))
    probs.push('Hold still inherits the full-width button, so the row breaks in two');

  // ---- 1-3. the sofa sizes exist at all ----
  [['#s-quiz .qa-note','the explanation'],
   ['#s-quiz .qsc b','the score'],
   ['#q-options .qbtn.s10 .tookby','the name on a taken answer']].forEach(([sel,what])=>{
    const m=css.match(new RegExp(sel.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\{[^}]*font-size:clamp\\(([^,]+),[^,]+,([^)]+)\\)'));
    if(!m){probs.push(what+' has no television size');return}
    const top=parseFloat(m[2]);
    if(top<22)probs.push(what+' tops out at '+m[2]+', still print size');
  });

  // ---- 4. a trivia heading is the category, and says so ----
  w.eval(`S.game='trivia';S.lang='en';
    S.players=[{id:'a',name:'Henry',score:3}];
    Q.deck=new Array(10);Q.round=1;Q.current=TRIVIA[0];Q.qid='';
    Q.options=[TRIVIA[0][3],TRIVIA[0][2],TRIVIA[0][4],TRIVIA[0][5]];Q.correct=1;
    Q.answers={};Q.revealed=false;drawQuiz();`);
  if(!$('q-ask').className.includes('cat'))
    probs.push('the category is still dressed as the headline, above the question');
  if($('q-ask').textContent!==w.eval('TRIVIA[0][0]'))
    probs.push('the heading is not the category');
  if(!$('s10-rules').hidden)probs.push('the Short List strip is showing in a quiz');
  if($('q-next').className.includes('calm'))probs.push('Reveal was quietened in a quiz');

  // ---- 6-10. the Short List ----
  w.eval(`S.game='s10';
    S.players=[{id:'a',name:'Henry',score:12},{id:'b',name:'Mia',score:8},
               {id:'c',name:'Jussi',score:20},{id:'d',name:'Anna',score:5}];
    const bank=s10Bank();Q.deck=new Array(10);Q.round=3;Q.current=bank[0];
    Q.cands=Q.current[3].map(c=>({t:c.t,ok:c.ok,by:null}));
    Q.cands[0].by='a';Q.cands[0].ok=true;Q.cands[1].by='b';Q.cands[1].ok=false;
    Q.state={a:'in',b:'out',c:'banked',d:'in'};
    Q.pot={a:3,b:0,c:0,d:0};Q.picks={a:1,b:1,c:2,d:0};
    Q.revealed=false;drawQuiz();`);
  // 6
  if($('s10-rules').hidden)probs.push('the rules are not on screen');
  else{
    const t=$('s10-rules').textContent;
    ['true','pot','gone','Bank'].forEach(word=>{
      if(t.indexOf(word)<0)probs.push('the rules never say "'+word+'"');
    });
  }
  if(!/#s-quiz:has\(#s10-rules:not\(\[hidden\]\)\) \.videowall\{display:none/.test(css))
    probs.push('the Short List still carries an empty curtain above the question');
  // 7, 10
  const chip=n=>[...d.querySelectorAll('#q-scores .qsc')]
    .find(c=>c.textContent.indexOf(n)>=0);
  const henry=chip('Henry'),anna=chip('Anna'),jussi=chip('Jussi'),mia=chip('Mia');
  if(!henry||!/at risk/.test(henry.textContent))probs.push('the pot is not marked at risk');
  if(!henry||!henry.className.includes('atrisk'))probs.push('the pot chip is not dressed as at risk');
  if(!anna||anna.textContent.indexOf('✓')>=0)
    probs.push('a player who has done nothing is given a tick');
  if(!anna||anna.className.trim()!=='qsc')
    probs.push('an idle player is lit up as if they had acted: '+(anna&&anna.className));
  if(!jussi||jussi.textContent.indexOf('✓')<0)probs.push('banking does not show a tick');
  if(!mia||mia.textContent.indexOf('✗')<0)probs.push('being out does not show');
  // 8
  if(!/#q-options \.qbtn\.s10\.missed\{[^}]*border-width:2px/.test(css))
    probs.push('a wrong pick is still a faint tint');
  // 9
  if(!$('q-next').className.includes('calm'))
    probs.push('End the round is still the loudest thing on the screen');
  w.eval('Q.revealed=true;drawQuiz();');
  if($('q-next').className.includes('calm'))
    probs.push('the next-question button stayed quiet after the reveal');

  console.log(probs.length?'FAIL:':'ok - the sofa: category, explanation, scores, Hold, and the Short List');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1100);
