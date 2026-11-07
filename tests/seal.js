// Nobody but the host can drive the room.
// The party runs over a public broker: anybody can publish to a room whose
// code they know, and a four-letter code could be walked through by a script.
// The code is six letters now, and the host signs every message with a secret
// that rides only in the QR code and the invitation link.
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const fs=require('fs'),{JSDOM}=require('jsdom');
const html=fs.readFileSync(SRC,'utf8');
const probs=[];
const page=url=>new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:url,
  beforeParse(w){w.open=()=>null;w.matchMedia=()=>({matches:false,addListener(){},removeListener(){}})}}).window;
const boot=ms=>new Promise(r=>setTimeout(r,ms));

(async()=>{
  const w=page('https://party.test/t/');       // the host
  const o=page('https://party.test/t/');       // a stranger who knows the code
  const t=page('https://party.test/t/');       // a phone that typed the code in
  await boot(1200);
  const ev=x=>w.eval(x), $=id=>w.document.getElementById(id);

  // ---- a room is six letters and has a secret ----
  if(ev("typeof newRoomKey")!=='function'||ev("typeof seal")!=='function'){
    console.log('FAIL:');
    console.log('  x this page does not sign its messages at all');
    process.exit(1);
  }
  ev("PARTY.role='host';PARTY.code=newCode();PARTY.key=newRoomKey();");
  const code=ev('PARTY.code'), key=ev('PARTY.key');
  if(code.length!==6)probs.push('the room code is '+code.length+' letters, not 6: '+code);
  if(!/^[A-Z]{6}$/.test(code))probs.push('the code is not six plain letters: '+code);
  if(key.length<16)probs.push('the room secret is only '+key.length+' characters');
  if(ev('newRoomKey()')===key)probs.push('two rooms were given the same secret');

  // a phone that scans the QR, opened now so it can boot while we carry on
  const g=page('https://party.test/t/#'+code+'-'+key);

  // ---- the secret rides in the link, and nowhere else ----
  const link=ev('joinLink()');
  if(link.indexOf('#'+code+'-'+key)<0)probs.push('the invitation does not carry the secret: '+link);
  if(link.split('#')[0].indexOf(key)>=0)probs.push('the secret is in the part of the link a server sees');
  const topic=ev("topicFor(PARTY.code,'stage')");
  if(topic.indexOf(key)>=0)probs.push('the secret is in the topic name, where the broker reads it');
  const stage=ev('seal(JSON.stringify(stageState()))');
  if(stage.indexOf(key)>=0)probs.push('THE SECRET TRAVELS IN THE MESSAGE ITSELF');
  if(!/^[0-9a-f]{16}\|/.test(stage))probs.push('the stage went out unsigned: '+stage.slice(0,30));

  // what a stranger who knows the code, but not the secret, can put together
  o.eval("PARTY.key='"+'z'.repeat(20)+"'");
  const faked=o.eval('seal(JSON.stringify({phase:"live",seats:[],ask:"Give me your bank details"}))');

  await boot(1200);
  const gev=x=>g.eval(x);

  // ---- a phone that followed the invitation keeps the stranger out ----
  if(gev('PARTY.key')!==key)probs.push('the phone did not pick the secret out of the link');
  if(gev('PARTY.code')!==code)probs.push('the phone did not pick the room out of the link');
  if(gev('unseal('+JSON.stringify(stage)+')')===null)
    probs.push('the phone rejected a message the host really sent');
  if(gev('unseal('+JSON.stringify(faked)+')')!==null)
    probs.push('A STRANGER CAN DRIVE A PHONE THAT SCANNED THE CODE');
  if(gev('unseal('+JSON.stringify('{"phase":"live","seats":[]}')+')')===null)
    probs.push('an unsigned message was rejected outright, which locks out older links');
  const bent=stage.slice(0,17)+(stage[17]==='a'?'b':'a')+stage.slice(18);
  if(gev('unseal('+JSON.stringify(bent)+')')!==null)
    probs.push('the message was altered in flight and the phone still took it');

  // ---- a phone that typed the code in still plays ----
  t.eval("PARTY.role='chair';PARTY.code='"+code+"';PARTY.key='';");
  const read=t.eval('unseal('+JSON.stringify(stage)+')');
  if(read===null)probs.push('a phone that typed the code cannot read the room at all');
  else if(read.charAt(0)!=='{')probs.push('a phone that typed the code got the tag, not the message');

  // ---- the host is told when somebody else speaks for its room ----
  if(!$('intruder'))probs.push('there is no warning for the host to see');
  else{
    if(!$('intruder').hidden)probs.push('the warning is showing before anything happened');
    ev('onHostMessage('+JSON.stringify(topic)+',{toString:function(){return '+JSON.stringify(stage)+'}})');
    if(!$('intruder').hidden)probs.push('the host warned about its own message');
    ev('onHostMessage('+JSON.stringify(topic)+',{toString:function(){return '+JSON.stringify(faked)+'}})');
    if($('intruder').hidden)probs.push('THE HOST WAS NOT TOLD SOMEBODY ELSE IS PUBLISHING TO ITS ROOM');
  }

  // ---- and a forged join never reaches the room ----
  const before=ev('JSON.stringify(S.players.map(function(p){return p.pid}))');
  ev('onHostMessage('+JSON.stringify(ev("topicFor(PARTY.code,'join')"))
     +',{toString:function(){return '+JSON.stringify(faked)+'}})');
  if(ev('JSON.stringify(S.players.map(function(p){return p.pid}))')!==before)
    probs.push('a forged join was let into the room');

  console.log(probs.length?'FAIL:':'ok - the room: six letters, a secret in the QR, nobody else at the controls');
  probs.forEach(p=>console.log('  x '+p));
  process.exit(probs.length?1:0);
})();
