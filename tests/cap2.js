// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// the room must hold as many people as the host said, and Back must not kill it
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
  const H=page('host');const hw=H.window,hd=hw.document,h$=id=>hd.getElementById(id);
  const click=(w,el)=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
  const type=(w,el,v)=>{el.value=v;el.dispatchEvent(new w.Event('input',{bubbles:true}))};
  const at=()=>[...hd.querySelectorAll('.screen')].filter(s=>s.classList.contains('on')).map(s=>s.id).join('+');
  await tick(250);
  click(hw,h$('m-create'));await tick(200);
  const code=h$('rb-code').textContent.trim();

  // the stepper actually moves
  const before=hw.eval('MAX_CHAIRS');
  click(hw,h$('mp-down'));click(hw,h$('mp-down'));
  const after=hw.eval('MAX_CHAIRS');
  if(after!==before-2)probs.push('the max-players stepper did not move: '+before+' -> '+after);
  if(h$('mp-n').textContent.trim()!==String(after))probs.push('the stepper shows the wrong number');
  click(hw,h$('mp-up'));click(hw,h$('mp-up'));

  // eight phones fill a room of eight, even though the host holds an empty row
  const phones=[];
  for(let i=0;i<8;i++){
    const P=page('phone'+i),pw=P.window,p$=id=>P.window.document.getElementById(id);
    click(pw,p$('m-code'));type(pw,p$('join-code'),code);type(pw,p$('join-name'),'Guest'+(i+1));
    click(pw,p$('join-go'));phones.push({P:P,w:pw,$:p$});
    await tick(220);
  }
  const seated=hw.eval('S.players.filter(function(p){return p.pid}).length');
  if(seated!==8)probs.push('only '+seated+' of 8 phones got a chair');
  if(hw.eval('Object.keys(KNOCKS).length'))probs.push('somebody was left knocking: '
    +hw.eval('JSON.stringify(Object.keys(KNOCKS))'));

  // Back goes back a screen and leaves the room standing
  click(hw,h$('rb-next'));await tick(150);
  click(hw,h$('lobby-back'));await tick(200);
  if(at()!=='s-setup')probs.push('Back from the lobby went to '+at());
  if(hw.eval('PARTY.code')!==code)probs.push('BACK SHUT THE ROOM DOWN');
  if(hw.eval('S.players.filter(function(p){return p.pid}).length')!==8)
    probs.push('Back dropped the players');

  // and when the host really does close it, the phones are told
  click(hw,h$('modes-back'));await tick(350);
  const said=phones[0].$('pad-state').textContent;
  if(!/closed the room/i.test(said))probs.push('a phone was left hanging after the room closed: '+said.slice(0,70));
  if(!phones[0].$('pad-quiz').hidden)probs.push('the answers stayed on screen after the room closed');

  console.log(probs.length?'FAIL:':'ok - eight phones fit, Back keeps the room, closing it tells everyone');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
})();
