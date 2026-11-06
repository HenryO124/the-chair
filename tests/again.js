// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// one party, several games: the room, the code and the phones survive a finish
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
function fakeMqtt(){const subs=[],retained={};
  const match=(pat,t)=>{const a=pat.split('/'),b=t.split('/');
    if(a.length!==b.length&&a[a.length-1]!=='#')return false;
    return a.every((x,i)=>x==='+'||x==='#'||x===b[i])};
  return w=>({connect(){const c={connected:true,handlers:{},options:{},
    on(ev,fn){(this.handlers[ev]=this.handlers[ev]||[]).push(fn);if(ev==='connect')setTimeout(()=>fn(),0);return this},
    subscribe(t,o,cb){(Array.isArray(t)?t:[t]).forEach(topic=>{subs.push({c:this,topic});
      Object.keys(retained).forEach(rt=>{if(match(topic,rt))setTimeout(()=>this.fire(rt,retained[rt]),0)})});
      if(cb)cb(null);return this},
    publish(t,p,o){if(o&&o.retain)retained[t]=p;
      setTimeout(()=>subs.forEach(s=>{if(match(s.topic,t))s.c.fire(t,p)}),0);return this},
    fire(t,p){(this.handlers.message||[]).forEach(fn=>fn(t,Buffer.from(String(p))))},
    end(){this.connected=false}};return c}})}
const broker=fakeMqtt();
function page(tag){const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,
  url:'https://party.test/t/',beforeParse(w){w.open=()=>null;
    w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}});w.mqtt=broker(w);
    Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async()=>{}}})}});
  dom.window.addEventListener('error',e=>probs.push(tag+' JS error: '+e.message));return dom}
const tick=(ms=90)=>new Promise(r=>setTimeout(r,ms));
(async()=>{
  const H=page('host'),P=page('phone');
  const hw=H.window,hd=hw.document,h$=id=>hd.getElementById(id);
  const pw=P.window,pd=pw.document,p$=id=>pd.getElementById(id);
  const click=(w,el)=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
  const type=(w,el,v)=>{el.value=v;el.dispatchEvent(new w.Event('input',{bubbles:true}))};
  const at=()=>[...hd.querySelectorAll('.screen')].filter(s=>s.classList.contains('on')).map(s=>s.id).join('+');
  await tick(200);

  click(hw,h$('m-create'));await tick(150);
  click(hw,hd.querySelector('#s-setup [data-game="trivia"]'));await tick(60);
  const code=h$('rb-code').textContent.trim();
  click(pw,p$('m-code'));type(pw,p$('join-code'),code);type(pw,p$('join-name'),'Sanna');
  click(pw,p$('join-go'));await tick(500);
  if(!hw.eval('S.players.filter(function(p){return p.pid}).length'))probs.push('the phone never got a chair');

  // play the quiz to the end
  click(hw,h$('rb-next'));await tick(120);
  click(hw,h$('to-rules'));await tick(80);
  click(hw,h$('lobby-start'));await tick(300);
  hw.eval('S.len=2;Q.deck=Q.deck.slice(0,1);quizFinish()');await tick(250);
  if(at()!=='s-final')probs.push('the game did not finish: '+at());
  if(!/stays open/i.test(h$('final-room').textContent))probs.push('the final screen does not say the room stays open');
  if(!/stay seated/i.test(pd.getElementById('pad-quiz').textContent))
    probs.push('the phone was not told to stay: '+pd.getElementById('pad-quiz').textContent.slice(0,80));

  // same party, another game
  click(hw,h$('restart'));await tick(200);
  if(at()!=='s-setup')probs.push('"Next game" went to '+at());
  if(h$('rb-code').textContent.trim()!==code)probs.push('THE ROOM CODE CHANGED: '+h$('rb-code').textContent);
  if(h$('roombar').hidden)probs.push('the room bar vanished');
  if(!hw.eval('S.players.filter(function(p){return p.pid}).length'))probs.push('THE PHONE LOST ITS CHAIR');
  if(!pw.eval('(PARTY.stage||{}).phase')||pw.eval("(PARTY.stage||{}).phase")!=='lobby')
    probs.push('the phone did not follow back to the lobby: '+pw.eval("JSON.stringify((PARTY.stage||{}).phase)"));

  // and a different mode plays through
  click(hw,hd.querySelector('#s-setup [data-game="picture"]'));await tick(80);
  click(hw,h$('rb-next'));await tick(120);
  click(hw,h$('to-rules'));await tick(80);
  click(hw,h$('lobby-start'));await tick(400);
  if(hw.eval('S.game')!=='picture')probs.push('the second game is not Picture Guess');
  if(!pw.eval('(PARTY.stage||{}).pic'))probs.push('no picture in the second game');
  const pp=p$('pad-pic');
  if(!pp||pp.hidden)probs.push('the phone shows no picture in the second game');
  if(p$('pad-quiz').querySelectorAll('button').length!==4)probs.push('the phone has no answers in the second game');

  console.log(probs.length?'FAIL:':'ok - one party, two games, same code, same phones');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
})();
