const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://a.test/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const click=el=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
setTimeout(()=>{
// This suite was written against the English page and checks wording. The
// interface now speaks Finnish by default, so it asks for English first;
// the Finnish and Swedish wording is covered by words.js and uilang.js.
  try{w.eval("S.lang='en';typeof dressUI==='function'&&dressUI()")}catch(e){}

  w.eval("S.game='picture';S.lang='fi';S.cats=[];S.len=5;S.players=[mkPlayer('A',0,0,'p1')];quizStart()");
  w.eval('quizReveal()');
  if(!/\d/.test($('q-next').textContent))probs.push('the button shows no clock: '+$('q-next').textContent);
  if($('q-hold').hidden)probs.push('there is no way to hold it');
  if(!w.eval('Q.nextIn'))probs.push('the clock did not start');
  // Henry asked for five seconds; three call sites used to carry three
  // different numbers and it drifted back to nine twice
  if(w.eval('NEXT_IN')!==5)probs.push('the countdown is '+w.eval('NEXT_IN')+' seconds, not 5');
  if(w.eval('Q.nextIn')!==5)probs.push('the clock started at '+w.eval('Q.nextIn')+', not 5');
  if(!w.eval('stageState().nextIn'))probs.push('the phones were not told');
  const r1=w.eval('Q.round');
  click($('q-hold'));
  if(w.eval('Q.nextIn'))probs.push('Hold did not stop it');
  if(!$('q-hold').hidden)probs.push('Hold stayed on screen after stopping');
  if(/\d/.test($('q-next').textContent))probs.push('the button still counts: '+$('q-next').textContent);
  // pressing next goes straight on
  click($('q-next'));
  if(w.eval('Q.round')!==r1+1)probs.push('pressing Next did not advance');
  if(w.eval('Q.nextIn'))probs.push('the new question opened with a clock running');
  // the last question waits to be pressed
  w.eval('Q.round=Q.deck.length;quizReveal()');
  if(w.eval('Q.nextIn'))probs.push('the last question started a countdown');
  // and the phone counts along from one message
  w.eval("S.game='trivia';quizStart();quizReveal()");
  const st=JSON.parse(w.eval('JSON.stringify(stageState())'));
  w.eval("PARTY.role='chair';PARTY.pid='p1';PARTY.stage="+JSON.stringify(st)+";drawPad()");
  if($('pad-next').hidden)probs.push('the phone shows no countdown');
  else{
    // The phone follows the language the questions are in, not its own, so ask
    // the page what this line should say rather than spelling it in English.
    const said=$('pad-next').textContent.trim();
    const n=(said.match(/\d+/)||[])[0];
    if(!n)probs.push('the phone countdown shows no number: '+said);
    else{
      const want=w.eval('T("next_in",{n:'+n+'})');
      if(said!==String(want).trim())
        probs.push('the phone countdown reads "'+said+'", the page says it should read "'+want+'"');
    }
  }
  console.log(probs.length?'FAIL:':'ok - the clock to the next question is visible, and can be held');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},900);
