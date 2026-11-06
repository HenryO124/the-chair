// paths come from the environment so this runs anywhere the repo is cloned
const path=require("path");
const ROOT=process.env.CHAIR_ROOT||path.resolve(__dirname,"..");
const SRC=process.env.CHAIR_SRC||path.join(ROOT,"src","index.html");
const BUNDLE=process.env.CHAIR_BUNDLE||path.join(ROOT,"index.html");
const {chromium,devices}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [name,dev] of [['iPhone SE',{viewport:{width:375,height:568},deviceScaleFactor:2,isMobile:true,hasTouch:true}],
                         ['iPhone 13',devices['iPhone 13']]]){
  const p=await b.newPage(dev);
  await p.goto('file://'+BUNDLE+'');
  await p.waitForTimeout(700);
  await p.evaluate(()=>{
    document.getElementById('intro').hidden=true;
    PARTY.role='chair';PARTY.pid='p1';PARTY.code='ABCD';
    show('s-chair');document.getElementById('chair-join').hidden=true;
    document.getElementById('chair-pad').hidden=false;
    const seats=[];for(let i=0;i<6;i++)seats.push({id:i,pid:'p'+(i+1),name:'Player '+(i+1),icon:i,photo:'',
      said:false,pick:-1,score:0,run:0,team:[],passed:false,full:false,blockUsed:false,total:0,reserved:false});
    PARTY.stage={v:1,game:'picture',phase:'live',round:1,of:10,revealed:false,correct:-1,vote:null,
      setup:'',remote:false,vid:'',ask:'Mikä tämä on?',cat:'Maamerkit',
      pic:'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600"><rect width="800" height="600" fill="%23334"/></svg>',
      options:['Oslo','Bergen','Tromssa','Turku'],seats:seats};
    drawPad();
  });
  await p.waitForTimeout(300);
  const m=await p.evaluate(()=>{
    const g=document.getElementById('pad-quiz').getBoundingClientRect();
    return {top:Math.round(g.top),bottom:Math.round(g.bottom),vh:window.innerHeight};
  });
  console.log(name,'answers',m.top+'-'+m.bottom,'of',m.vh, m.bottom<=m.vh?'ok - all four fit':'BELOW THE FOLD by '+(m.bottom-m.vh));
  await p.screenshot({path:'/tmp/fold-'+name.replace(/ /g,'')+'.png'});
  await p.close();
}
await b.close();})();
