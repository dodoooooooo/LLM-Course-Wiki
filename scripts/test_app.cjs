// 程式層級回歸測試：DOM 替身不代表瀏覽器版面實測。
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const data=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const code=fs.readFileSync(process.argv[3],'utf8');
function boot(stored=null){
 const nodes=new Map(),node=()=>({classList:{remove(){},add(){},toggle(){}},dataset:{},value:'',innerHTML:'',textContent:''});
 const doc={documentElement:{style:{values:{},setProperty(key,value){this.values[key]=value},getPropertyValue(key){return this.values[key]}}},getElementById:id=>id==='wiki-data'?{textContent:JSON.stringify(data)}:node(),querySelector:s=>{if(!nodes.has(s))nodes.set(s,node());return nodes.get(s)},querySelectorAll:()=>[],addEventListener(){}};
 const storage={value:stored,getItem(){return this.value},setItem(key,value){assert.equal(key,'course-wiki-v1');this.value=value}};
 const context=vm.createContext({document:doc,localStorage:storage,window:{addEventListener(){},scrollTo(){}},location:{hash:''},structuredClone,setTimeout,clearTimeout,console,assert,URLSearchParams,confirm:()=>true});
 vm.runInContext(code,context);
 return {context,doc,storage};
}
const {context,doc}=boot();
context.assert=assert;
vm.runInContext(`
// 配色必須在每次導覽重算為所屬課程的穩定值，工具頁回到亮黃。
assert.equal(document.documentElement.style.getPropertyValue('--accent'),DEFAULT_ACCENT);
applyTheme({id:'configured-color-test',accent:'#52a9ff'});assert.equal(document.documentElement.style.getPropertyValue('--accent'),'#52a9ff');
const accents=new Map(DATA.courses.map(c=>[c.id,courseAccent(c)]));
DATA.courses.reverse();
for(const c of DATA.courses){
 const paths=[c.path,...c.sections.map(s=>s.path),...DATA.pages.filter(p=>p.courseId===c.id).map(p=>p.path)];
 for(const path of paths){location.hash='#'+path;render();assert.equal(document.documentElement.style.getPropertyValue('--accent'),accents.get(c.id),path)}
 applyTheme({...c,title:'更改名稱的測試'});assert.equal(document.documentElement.style.getPropertyValue('--accent'),accents.get(c.id));
}
DATA.courses.reverse();
for(const path of ['/','/search','/sources','/records','/wrong']){location.hash='#'+path;render();assert.equal(document.documentElement.style.getPropertyValue('--accent'),DEFAULT_ACCENT)}
// 實際點綴色的黑字對比須達一般文字門檻，非只檢查色碼格式。
const luminance=hex=>{const rgb=hex.slice(1).match(/../g).map(x=>parseInt(x,16)/255).map(x=>x<=0.04045?x/12.92:((x+0.055)/1.055)**2.4);return rgb[0]*0.2126+rgb[1]*0.7152+rgb[2]*0.0722};
for(const color of [DEFAULT_ACCENT,...ACCENT_PALETTE])assert.ok((luminance(color)+0.05)/(luminance('#111111')+0.05)>=4.5,color);
assert.ok((luminance('#ffffff')+0.05)/(luminance('#494949')+0.05)>=4.5);
assert.ok(home().includes(DATA.courses.length+' 門課程'));
for(const c of DATA.courses){
 assert.ok(home().includes(esc(c.title)));assert.ok(records().includes(esc(c.title)));
 for(const s of c.sections){
  location.hash='#'+s.path;render();assert.ok(document.querySelector('#courseNav').innerHTML.includes(esc(s.label)));
  const html=sectionPage(c,s);assert.ok(html.includes(s.pageIds.length+' 篇')||!s.pageIds.length);
 }
}
for(const path of Object.keys(DATA.routes)){location.hash='#'+path;assert.doesNotThrow(()=>render(),path)}
for(const source of DATA.pages.filter(p=>p.kind==='source'))assert.ok(sources().includes('#'+source.path));
for(const page of DATA.pages.filter(p=>p.kind==='source'||p.trackReading)){
 query=page.short;assert.ok(searchPage().includes('#'+page.path),page.path);
}
for(const word of ['V&V','A+B','SNR? test','100%','中文/#']){location.hash='#/search?q='+encodeURIComponent(word);render();assert.equal(query,word)}
location.hash='#/search?q=%';assert.doesNotThrow(()=>render());location.hash='#/search?q=';render();assert.equal(query,'');
assert.equal(norm('  SWIMLANES  '),'swimlanes');assert.equal(norm('#'),'#');assert.equal(norm('-'),'-');
state={version:1,read:{},outcomes:{},history:[],drafts:{}};session=null;
for(const c of DATA.courses){
 const reading=DATA.pages.filter(p=>p.courseId===c.id&&p.trackReading);
 for(const p of reading)state.read[p.readKey]=true;
 const stats=stat().find(s=>s.course.id===c.id);assert.equal(stats.read,reading.length);assert.equal(stats.total,reading.length);
 for(const other of stat().filter(s=>s.course.id!==c.id))assert.equal(other.read,0);
 for(const p of reading)delete state.read[p.readKey];
 if(reading.length){const p=reading[0];location.hash='#'+p.path;render();document.querySelector('#readToggle').dataset.key=p.readKey;document.querySelector('#readToggle').onclick();assert.equal(state.read[p.readKey],true);assert.ok(document.querySelector('#app').innerHTML.includes('已閱讀，取消標記'));document.querySelector('#readToggle').onclick();assert.equal(state.read[p.readKey],false)}
}
for(const c of quizzes){
 session=fresh(c);
 for(const q of c.questions){
  if(q.type==='choice'){session.answers[q.id]=q.answer;assert.equal(correct(q),true);session.answers[q.id]=(q.answer+1)%q.options.length;assert.equal(correct(q),false)}
  else if(q.type==='fill'){session.answers[q.id]=' '+q.answers[0].toUpperCase()+' ';assert.equal(correct(q),true);session.answers[q.id]='not-a-valid-answer';assert.equal(correct(q),false)}
 }
 session=fresh(c,'exam');
 for(const q of c.questions.filter(q=>q.type!=='written'))assert.ok(!quiz(c).includes(esc(q.explanation)));
 const first=c.questions.find(q=>q.type==='choice');
 if(first){session.answers[first.id]=first.answer;record(first);assert.equal(state.outcomes[first.id].correct,true);session.answers[first.id]=(first.answer+1)%first.options.length;record(first);assert.equal(state.outcomes[first.id].correct,false);assert.ok(wrongPage().includes('#'+c.path))}
 session=fresh(c,'practice','written');assert.equal(session.ids.length,c.questions.filter(q=>q.type==='written').length);
 session=fresh(c);saveDraft();assert.equal(String(session.chapter),c.quizKey);
 if(c.questions.length){session=fresh(c,'exam');for(const q of c.questions){if(q.type==='choice')session.answers[q.id]=q.answer;else if(q.type==='fill')session.answers[q.id]=q.answers[0]}location.hash='#'+c.path;submit();assert.equal(state.history.at(-1).chapter,c.recordChapter);assert.equal(state.history.at(-1).right,c.questions.filter(q=>q.type!=='written').length);assert.ok(session.submitted);assert.ok(quiz(c).includes('本次自動題'));assert.ok(records().includes(esc(courseFor(c).title)))}
}
// 舊版 version 1 識別碼保持原值；所有課程草稿與歷史紀錄可往返。
state={version:1,read:{},outcomes:{},history:[],drafts:{}};
for(const p of DATA.pages.filter(p=>p.trackReading))state.read[p.readKey]=true;
for(const c of quizzes){
 session=fresh(c,'exam');
 for(const q of c.questions){
  if(q.type==='choice')session.answers[q.id]=q.answer;
  if(q.type==='fill')session.answers[q.id]=q.answers[0];
  if(q.type!=='written')record(q);
 }
 saveDraft();
 state.history.push({chapter:c.recordChapter,time:new Date().toISOString(),right:c.questions.filter(q=>q.type!=='written').length,total:c.questions.filter(q=>q.type!=='written').length,written:c.questions.filter(q=>q.type==='written').length,unanswered:0,mode:'exam'});
}
const backup=JSON.parse(JSON.stringify(state));assert.equal(JSON.stringify(validateState(backup)),JSON.stringify(backup));
for(const c of quizzes){session=null;startQuiz(c);assert.equal(JSON.stringify(session),JSON.stringify(backup.drafts[c.quizKey]))}
const c=quizzes.find(c=>c.questions.some(q=>q.type==='choice'));
if(c){
 const first=c.questions.find(q=>q.type==='choice'),key=c.quizKey;
 for(const mutate of [x=>x.read=[],x=>x.drafts[key].answers=[],x=>x.drafts[key].answers[first.id]='錯誤型別',x=>x.drafts[key].chapter='錯誤章節',x=>x.drafts[key].mode='invalid',x=>x.drafts[key].pos=999999,x=>x.drafts[key].ids.push(first.id)]){const bad=JSON.parse(JSON.stringify(backup));mutate(bad);assert.throws(()=>validateState(bad))}
}
const archived=JSON.parse(JSON.stringify(backup));archived.read['archived/lesson']=true;archived.outcomes['archived-question']={correct:false,attempts:1,last:new Date().toISOString()};archived.history.push({chapter:'archived/quiz',time:new Date().toISOString(),right:0,total:1,unanswered:0,written:0,mode:'practice'});archived.drafts['archived/quiz']={chapter:'archived/quiz',mode:'practice',filter:'all',onlyWrong:false,shuffle:false,ids:['archived-question'],pos:0,answers:{'archived-question':'歷史文字'},graded:{},self:{},drawings:{},submitted:false,started:new Date().toISOString()};assert.equal(JSON.stringify(validateState(archived)),JSON.stringify(archived));
state=backup;
`,context);
// 重新載入 localStorage 亦保留舊版紀錄，不能只驗證手動匯入。
const backup=vm.runInContext('JSON.stringify(state)',context);
const reloaded=boot(backup);
assert.equal(vm.runInContext('JSON.stringify(state)',reloaded.context),backup);
assert.equal(vm.runInContext('accentFor("new-course-stable-id")',context),vm.runInContext('accentFor("new-course-stable-id")',reloaded.context));
console.log(`前端程式檢查通過：${data.courses.length} 門課程的路由、來源、搜尋、閱讀、判分與紀錄相容性。`);
