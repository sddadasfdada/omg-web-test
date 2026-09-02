# panel_js1.py — جاوااسکریپت پنل (قسمت ۱: helpers، ناوبری، داشبورد)
PANEL_JS1 = r"""
/* ═══ Helpers ═══ */
const $=id=>document.getElementById(id);
const FA_D='۰۱۲۳۴۵۶۷۸۹';
const fa=n=>String(n).replace(/\d/g,d=>FA_D[d]);
function fmtB(b){if(b<1024)return fa(b)+' B';if(b<1048576)return fa((b/1024).toFixed(1))+' KB';if(b<1073741824)return fa((b/1048576).toFixed(2))+' MB';return fa((b/1073741824).toFixed(2))+' GB'}
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function toast(msg,type='ok'){const t=document.createElement('div');t.className='toast '+type;
t.innerHTML=`<i class="ti ${type==='err'?'ti-circle-x':'ti-circle-check'}"></i> ${esc(msg)}`;
$('toasts').appendChild(t);setTimeout(()=>{t.style.opacity='0';t.style.transition='.3s';setTimeout(()=>t.remove(),320)},3200)}
async function copyTxt(txt){try{await navigator.clipboard.writeText(txt);toast('کپی شد ✅')}catch(e){
const ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();
try{document.execCommand('copy');toast('کپی شد ✅')}catch(_){toast('کپی نشد — دستی کپی کن','err')}ta.remove()}}
async function api(url,opts={}){const r=await fetch(url,opts);
if(r.status===401){location.href='/login';throw new Error('unauthorized')}
if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||('HTTP '+r.status))}
return r.json()}
function timeFa(iso){if(!iso)return '—';try{const d=new Date(iso);
return fa(d.toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit'}))}catch(e){return '—'}}
function dateFa(iso){if(!iso)return '∞';try{const d=new Date(iso);
return fa(d.toLocaleDateString('fa-IR',{year:'numeric',month:'2-digit',day:'2-digit'}))}catch(e){return '—'}}

/* ═══ Navigation ═══ */
const PG_TITLES={overview:['داشبورد','نمای کلی وضعیت سرور'],links:['کانفیگ‌ها','مدیریت لینک‌های VLESS و XHTTP'],
subs:['گروه‌های ساب','ساخت و مدیریت اشتراک‌ها'],conns:['اتصال‌های زنده','کاربران متصل در همین لحظه'],logs:['لاگ رویدادها','تاریخچه‌ی فعالیت‌ها']};
let curPg='overview';
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>{
document.querySelectorAll('.nav-it').forEach(x=>x.classList.remove('on'));el.classList.add('on');
document.querySelectorAll('.pg').forEach(p=>p.classList.remove('on'));
curPg=el.dataset.pg;$('pg-'+curPg).classList.add('on');
const t=PG_TITLES[curPg];$('tb-title').textContent=t[0];$('tb-sub').textContent=t[1];refreshPg()}));
function refreshPg(){if(curPg==='overview')loadOverview();else if(curPg==='links')loadLinks();
else if(curPg==='subs')loadSubs();else if(curPg==='conns')loadConns();else if(curPg==='logs')loadLogs()}
async function refreshAll(){await refreshPg();toast('بروزرسانی شد')}

/* ═══ Modal ═══ */
function openModal(html){$('modal').innerHTML=html;$('ovl').classList.add('on')}
function closeModal(){$('ovl').classList.remove('on')}
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal()});

/* ═══ Overview / Dashboard ═══ */
let cachedLinks=[];
async function loadOverview(){
try{
const [st,links,conns]=await Promise.all([api('/stats'),api('/api/links'),api('/api/connections')]);
cachedLinks=links.links;
$('uptime').textContent=st.uptime;
$('st-conns').textContent=fa(conns.count);
$('st-ips').textContent=fa(conns.raw_count)+' سشن خام';
$('st-links').textContent=fa(st.links_count);
$('st-links-sub').textContent=fa(st.active_links)+' فعال · '+fa(st.expired_links)+' منقضی';
$('st-traffic').textContent=fmtB(st.total_traffic_mb*1048576);
$('st-subs').textContent=fa(st.subs_count);
$('st-req').textContent=fa(st.total_requests)+' درخواست پردازش‌شده';
$('nb-links').textContent=fa(st.links_count);
$('nb-subs').textContent=fa(st.subs_count);
$('nb-conns').textContent=fa(conns.count);
/* chart — آخرین ۲۴ ساعت از hourly */
const ch=$('chart');ch.innerHTML='';
const hours={};const now=new Date();
for(let i=23;i>=0;i--){const d=new Date(now-i*3600000);
const k=String(d.getHours()).padStart(2,'0')+':00';hours[k]=0}
let max=1;for(const[k,v]of Object.entries(st.hourly||{})){if(k in hours){hours[k]=v;max=Math.max(max,v)}}
const entries=Object.entries(hours);
for(const[k,v]of entries){const bar=document.createElement('div');bar.className='cbar';
const h=Math.max(3,Math.round(v/max*100));
bar.innerHTML=`<div class="bar" style="height:${h}%" title="${k}: ${fmtB(v)}"></div><div class="h">${k.split(':')[0]}</div>`;
ch.appendChild(bar)}
/* errors */
const el=$('err-list');
if(!st.recent_errors||!st.recent_errors.length){el.innerHTML='<div class="empty"><i class="ti ti-check"></i>خطایی ثبت نشده — همه‌چیز سالمه ✨</div>'}
else{el.innerHTML=st.recent_errors.slice(-8).reverse().map(e=>
`<div class="log-it"><i class="ti ti-bug log-err"></i><div style="flex:1"><div style="font-size:12px">${esc(e.error||e)}</div><div class="log-t">${esc(e.url||'')} · ${timeFa(e.time)}</div></div></div>`).join('')}
/* sub-all url */
$('sub-all-url').textContent=location.origin+'/sub-all';
}catch(e){toast('خطا در دریافت داده‌ها: '+e.message,'err')}}
"""
