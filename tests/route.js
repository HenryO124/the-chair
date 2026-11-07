// every game must land on the screen it is played on
const fs=require('fs'),{JSDOM}=require('jsdom');
const path=require('path');
const SRC=process.env.CHAIR_SRC||path.resolve(__dirname,'..','src','index.html');
const dom=new JSDOM(fs.readFileSync(SRC,'utf8'),
 {runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const probs=[];const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
const at=()=>[...d.querySelectorAll('.screen')].filter(s=>s.classList.contains('on')).map(s=>s.id).join('+');
setTimeout(()=>{
  // Derived from the game list, not written down here: this fault has now
  // happened three times — Smart Ten, Point the Finger and Closest Wins each
  // fell through to the chair game — and every time it was because a new id
  // was added to the menu and not to the routing. A hand-kept list here would
  // miss the fourth one the same way.
  const want={};
  JSON.parse(w.eval('JSON.stringify(Object.keys(GAMELABEL))'))
    .forEach(g=>{want[g]=(g==='chair')?'s-listen':'s-quiz'});
  Object.keys(want).forEach(g=>{
    w.eval("SOLO=true;S.players=[mkPlayer('A',0,0,'')];S.game='"+g+"';S.len=5;S.cats=[];"
      +"S.era=0;S.genre='Random';Q.on=false;show('s-lobby')");
    click($('lobby-start'));
    const got=at();
    if(got!==want[g])probs.push(g+' started on '+got+', expected '+want[g]);
    if(g!=='chair'&&!w.eval('Q.current'))probs.push(g+' started with no question');
    if(g==='s10'&&!w.eval('Q.cands&&Q.cands.length===10'))probs.push('Smart Ten dealt no candidates');
    if(g==='finger'&&!w.eval('Q.votes'))probs.push('Point the Finger opened with no votes to take');
    if(g==='near'&&!w.eval('Q.guesses'))probs.push('Closest Wins opened with no guesses to take');
    w.eval('Q.on=false');
  });
  console.log(probs.length?'FAIL:':'ok - every game starts on its own screen');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
