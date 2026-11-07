// The whole interface in the language the questions are in — not just the
// strings the game writes during a round, but the menus a player stares at
// while deciding what to play.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://party.test/t/',
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}});
const w=dom.window,d=w.document;
const $=id=>d.getElementById(id)||{textContent:'',innerHTML:''};
w.addEventListener('error',e=>probs.push('JS error: '+e.message));
const ev=x=>w.eval(x);
// what a person can actually read on the screens that are in the markup
const visible=()=>{
  const clone=d.body.cloneNode(true);
  clone.querySelectorAll('script,style,svg,template').forEach(e=>e.remove());
  return clone.textContent.replace(/\s+/g,' ');
};
setTimeout(()=>{
  if(ev('typeof dressUI')!=='function'){
    console.log('FAIL:');console.log('  x this page has no interface language at all');process.exit(1);
  }
  // ---- the two tables agree with each other ----
  const fi=JSON.parse(ev('JSON.stringify(Object.keys(UITEXT.fi))'));
  const sv=JSON.parse(ev('JSON.stringify(Object.keys(UITEXT.sv))'));
  if(fi.length<120)probs.push('only '+fi.length+' Finnish strings');
  if(sv.length<120)probs.push('only '+sv.length+' Swedish strings');
  const onlyFi=fi.filter(k=>sv.indexOf(k)<0);
  if(onlyFi.length>6)probs.push(onlyFi.length+' strings have Finnish but no Swedish: '+onlyFi.slice(0,4).join(' | '));
  fi.forEach(k=>{
    const t=ev('UITEXT.fi['+JSON.stringify(k)+']');
    if(!String(t).trim())probs.push('fi: '+k+' is empty');
    if(t===k)probs.push('fi: '+JSON.stringify(k)+' is still English');
  });

  // ---- English stays English ----
  ev("S.lang='en';dressUI();");
  const en=visible();
  ['Create a party','Game modes','How we play','Settings'].forEach(t=>{
    if(en.indexOf(t)<0)probs.push('English is missing "'+t+'"');
  });

  // ---- Finnish really replaces it, on the screens as well as in the nav ----
  ev("S.lang='fi';dressUI();");
  const sfi=visible();
  [['Create a party','Luo bileet'],['Game modes','Pelit'],['Settings','Asetukset'],
   ['How we play','Miten pelataan'],['Your name','Nimesi'],['Room code','Huonekoodi'],
   ['Friends','Kaverit'],['Paused','Tauolla']].forEach(([was,want])=>{
    if(sfi.indexOf(want)<0)probs.push('Finnish is missing "'+want+'"');
    if(sfi.indexOf(was)>=0)probs.push('Finnish still shows the English "'+was+'"');
  });
  // the product's own name is not translated, and neither are the games
  ['The Chair','Picture Guess','The Short List','Point the Finger'].forEach(t=>{
    if(sfi.indexOf(t)<0)probs.push('the name "'+t+'" was translated away');
  });

  // ---- Swedish too ----
  ev("S.lang='sv';dressUI();");
  const ssv=visible();
  [['Settings','Inställningar'],['Room code','Rumskod'],['Friends','Vänner']].forEach(([was,want])=>{
    if(ssv.indexOf(want)<0)probs.push('Swedish is missing "'+want+'"');
  });

  // ---- and back to English, exactly ----
  ev("S.lang='en';dressUI();");
  if(visible()!==en)probs.push('switching away and back did not restore the English exactly');

  // ---- the code's own strings follow too ----
  ev("S.lang='fi';PARTY.role='host';PARTY.code='TESTAA';S.public=false;drawVis();drawRoomBar();");
  if(/Private room/.test($('rb-vis').textContent))probs.push('the room chip is still English');
  ev("openModes&&openModes('create');");
  if(/Create a game/.test($('modes-eyebrow').textContent))probs.push('the modes heading is still English');

  // ---- a string with no translation is left alone rather than blanked ----
  ev("S.lang='fi';UITEXT.fi['Game modes']=undefined;dressUI();");
  if(!/Game modes/.test(visible()))probs.push('a string with no translation vanished instead of staying English');

  console.log(probs.length?'FAIL:':'ok - the whole interface speaks the language the questions are in');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
},1200);
