// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
// menu 2 calls the room in: QR + invitation, a visible way back, the settings
// where everyone waits, and the picture on the phone.
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(''+SRC+'','utf8');
const probs=[];
function fakeMqtt(){
  const subs=[],retained={};
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
function page(tag){
  const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,
    url:'https://party.test/thechair/',
    beforeParse(w){w.open=()=>null;
      w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}});
      w.mqtt=broker(w);
      Object.defineProperty(w.navigator,'clipboard',{value:{writeText:async()=>{}}});
    }});
  dom.window.addEventListener('error',e=>probs.push(tag+' JS error: '+e.message));
  return dom;
}
const tick=(ms=80)=>new Promise(r=>setTimeout(r,ms));
(async()=>{
  const H=page('host'),P=page('phone');
  const hw=H.window,hd=hw.document,h$=id=>hd.getElementById(id);
  const pw=P.window,pd=pw.document,p$=id=>pd.getElementById(id);
  const click=(w,el)=>{if(el&&!el.disabled)el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}))};
  const type=(w,el,v)=>{el.value=v;el.dispatchEvent(new w.Event('input',{bubbles:true}))};
  const at=()=>[...hd.querySelectorAll('.screen')].filter(s=>s.classList.contains('on')).map(s=>s.id).join('+');
  await tick(150);

  click(hw,h$('m-create'));await tick(150);
  if(at()!=='s-setup')probs.push('menu 2 did not open: '+at());
  if(h$('roombar').hidden)probs.push('the room bar is hidden on menu 2');

  // a visible way back to menu 1
  const back=h$('modes-back');
  if(!back||back.offsetParent===null&&!back.className.includes('backlink'))probs.push('no way back to the main menu');
  if(!/Main menu/i.test(back.textContent))probs.push('the back button does not say where it goes');
  if(!/party/i.test(h$('rb-next').textContent))probs.push("the forward button still says: "+h$('rb-next').textContent);

  // the QR in the bar, and the big one over everything
  if(!h$('rb-qr'))probs.push('NO QR BUTTON ON MENU 2');
  const HASQR=hw.eval("typeof qrcode")==='function';   // the bundle inlines the generator
  if(HASQR&&!h$('rb-qr').querySelector('svg'))probs.push('the QR thumbnail drew nothing');
  click(hw,h$('rb-qr'));await tick(60);
  if(h$('joinover').hidden)probs.push('THE BIG JOIN CARD DID NOT OPEN');
  const code=h$('rb-code').textContent.trim();
  if(h$('jo-code').textContent.trim()!==code)probs.push('the big card shows the wrong code');
  if(HASQR?!h$('jo-qr').querySelector('svg'):!/party\.test/.test(h$('jo-qr').textContent))
    probs.push('the big QR drew nothing and gave no fallback: '+h$('jo-qr').textContent);
  if(!/party\.test/.test(h$('jo-link').textContent))probs.push('no join link on the big card: '+h$('jo-link').textContent);
  click(hw,h$('jo-close'));await tick(40);
  if(!h$('joinover').hidden)probs.push('the big card would not close');

  // the settings now live where everyone waits
  click(hw,hd.querySelector('#s-setup [data-game="picture"]'));await tick(60);
  click(hw,h$('rb-next'));await tick(100);
  if(at()!=='s-lobby')probs.push('"Let\'s party" went to '+at());
  const lob=h$('s-lobby');
  ['cats','length','lang','where','eras'].forEach(id=>{
    if(!lob.contains(h$(id)))probs.push('#'+id+' is not on the page where we wait for players');
  });
  if(!h$('cats').children.length)probs.push('the topics were not drawn in the lobby');
  if(!lob.contains(h$('lobby-home')))probs.push('no main-menu link on the lobby');

  // a phone joins and plays Picture Guess: it must see the picture
  click(pw,p$('m-code'));
  type(pw,p$('join-code'),code);type(pw,p$('join-name'),'Sanna');
  click(pw,p$('join-go'));await tick(900);
  if(!hw.eval('S.players.filter(function(p){return p.pid}).length'))
    probs.push('the phone never got a chair [role='+pw.eval('JSON.stringify(PARTY.role)')
      +' code='+pw.eval('JSON.stringify(PARTY.code)')+' st='+pd.getElementById('join-status').textContent+']');
  click(hw,h$('to-rules'));await tick(80);
  if(at()!=='s-go')probs.push('ready went to '+at());
  click(hw,h$('lobby-start'));await tick(700);
  const pic=pw.eval('(PARTY.stage||{}).pic||""');
  if(!pic)probs.push('THE HOST NEVER SENT THE PICTURE [hostpic='+hw.eval('JSON.stringify(stageState().pic)')
    +' phonephase='+hw.eval('JSON.stringify(S.game)')+'/'+pw.eval('JSON.stringify((PARTY.stage||{}).phase)')
    +' round='+pw.eval('JSON.stringify((PARTY.stage||{}).round)')+']');
  await tick(150);
  const pp=p$('pad-pic');
  if(!pp)probs.push('the phone has no place for the picture');
  else if(pp.hidden)probs.push('THE PHONE IS NOT SHOWING THE PICTURE');
  else if(!/url\(/.test(pp.style.backgroundImage))probs.push('the picture element is empty on the phone');

  console.log(probs.length?'FAIL:':'ok - QR, back, settings in the lobby, picture on the phone');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
})();
