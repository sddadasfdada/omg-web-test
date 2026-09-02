# panel_js2.py — جاوااسکریپت پنل (قسمت ۲: کانفیگ‌ها، گروه‌ها، اتصال‌ها، لاگ‌ها)
PANEL_JS2 = r"""
/* ═══ Links page ═══ */
const PROTO_NAME={'vless-ws':'VLESS · WS','xhttp-packet-up':'XHTTP · Packet','xhttp-stream-up':'XHTTP · Stream','xhttp-stream-one':'XHTTP · One'};
function protoChip(p){const n=PROTO_NAME[p]||p;return `<span class="chip ${p==='vless-ws'?'ws':'xh'}">${n}</span>`}
function statusChip(l){if(l.expired)return '<span class="chip rd">منقضی</span>';
if(!l.active)return '<span class="chip def">غیرفعال</span>';
const lb=l.limit_bytes;if(lb>0&&l.used_bytes>=lb)return '<span class="chip am">پر شده</span>';
return '<span class="chip gr">فعال</span>'}
function usageBar(l){const lb=l.limit_bytes||0,ub=l.used_bytes||0;
const pct=lb>0?Math.min(100,ub/lb*100):0;
const inner=lb>0?`${fmtB(ub)} / ${fmtB(lb)} · ${fa(Math.round(pct))}٪`:`${fmtB(ub)} · نامحدود`;
return `<div class="usage"><div class="u-lbl"><span>مصرف</span><span>${inner}</span></div>
<div class="u-bar"><div class="u-fill ${pct>=80?'warn':''}" style="width:${lb>0?pct:100}%"></div></div></div>`}
async function loadLinks(){try{const d=await api('/api/links');cachedLinks=d.links;renderLinks()}
catch(e){toast('خطا در دریافت کانفیگ‌ها: '+e.message,'err')}}
function renderLinks(){
const q=($('link-search')?.value||'').trim().toLowerCase();
const list=cachedLinks.filter(l=>!q||(l.label||'').toLowerCase().includes(q)||(l.note||'').toLowerCase().includes(q));
const el=$('links-list');
if(!list.length){el.innerHTML='<div class="empty"><i class="ti ti-link-off"></i>کانفیگی پیدا نشد — از دکمه‌ی «کانفیگ جدید» بساز.</div>';return}
el.innerHTML=list.map(l=>`
<div class="row">
  <span class="st-dot ${l.expired?'exp':!l.active?'off':(l.limit_bytes>0&&l.used_bytes>=l.limit_bytes)?'full':'ok'}"></span>
  <div class="r-main">
    <div class="r-title">${esc(l.label)} ${statusChip(l)} ${l.is_default?'<span class="chip def">پیش‌فرض</span>':''}</div>
    <div class="r-meta"><span>${protoChip(l.protocol)}</span><span><i class="ti ti-device-sim"></i> IP: ${l.ip_limit>0?fa(l.ip_limit)+' کاربر':'∞'}</span>
    <span><i class="ti ti-gauge"></i> ${l.speed_limit_bytes>0?fa(Math.round(l.speed_limit_bytes*8/1048576))+' Mbps':'∞'}</span>
    <span><i class="ti ti-calendar-x"></i> انقضا: ${dateFa(l.expires_at)}</span>
    <span><i class="ti ti-users"></i> ${fa(l.connected_ips||0)} متصل</span>
    ${l.note?`<span><i class="ti ti-note"></i> ${esc(l.note)}</span>`:''}</div>
  </div>
  ${usageBar(l)}
  <div class="acts">
    <button class="btn sm" title="لینک" onclick="copyTxt('${esc(l.vless_link)}')"><i class="ti ti-copy"></i></button>
    <button class="btn sm" title="QR" onclick="showQR('${esc(l.vless_link)}','${esc(l.label)}')"><i class="ti ti-qrcode"></i></button>
    <button class="btn sm" title="ساب URL" onclick="copyTxt('${esc(l.sub_url)}')"><i class="ti ti-rss"></i></button>
    <button class="btn sm ${l.active?'dgr':'ok'}" title="${l.active?'غیرفعال':'فعال'}" onclick="toggleLink('${l.uuid}',${!l.active})"><i class="ti ti-${l.active?'pause':'player-play'}"></i></button>
    <button class="btn sm" title="ویرایش" onclick="openEditLink('${l.uuid}')"><i class="ti ti-settings"></i></button>
    <button class="btn sm dgr" title="حذف" onclick="delLink('${l.uuid}','${esc(l.label)}')"><i class="ti ti-trash"></i></button>
  </div>
</div>`).join('')}

/* ═══ New / Edit link modals ═══ */
function openNewLink(){openModal(`
<h3><i class="ti ti-link-plus"></i> ساخت کانفیگ جدید</h3>
<label class="fl">نام کانفیگ</label><input class="inp" id="f-label" placeholder="مثلاً: کانفیگ موبایل من">
<div class="frow" style="margin-top:12px">
  <div><label class="fl">حجم (خالی = نامحدود)</label><input class="inp" id="f-limit" type="number" min="0" step="any" placeholder="0"></div>
  <div><label class="fl">واحد</label><select class="inp" id="f-limit-unit"><option>GB</option><option>MB</option><option>KB</option></select></div>
</div>
<div class="frow" style="margin-top:12px">
  <div><label class="fl">انقضا (روز — خالی = بی‌نهایت)</label><input class="inp" id="f-exp" type="number" min="0" placeholder="0"></div>
  <div><label class="fl">محدودیت IP (خالی = نامحدود)</label><input class="inp" id="f-ip" type="number" min="0" placeholder="0"></div>
</div>
<div class="frow" style="margin-top:12px">
  <div><label class="fl">سرعت (خالی = نامحدود)</label><input class="inp" id="f-speed" type="number" min="0" step="any" placeholder="0"></div>
  <div><label class="fl">واحد سرعت</label><select class="inp" id="f-speed-unit"><option value="MBIT">Mbps</option><option value="MB">MB/s</option><option value="KB">KB/s</option></select></div>
</div>
<label class="fl" style="margin-top:12px">پروتکل</label>
<select class="inp" id="f-proto">
  <option value="vless-ws">VLESS + WebSocket (سازگارترین)</option>
  <option value="xhttp-packet-up">XHTTP · Packet-UP</option>
  <option value="xhttp-stream-up">XHTTP · Stream-UP</option>
  <option value="xhttp-stream-one">XHTTP · Stream-One</option>
</select>
<div class="frow" style="margin-top:12px">
  <div><label class="fl">Fingerprint</label><select class="inp" id="f-fp"><option>chrome</option><option>firefox</option><option>safari</option><option>ios</option><option>android</option><option>edge</option><option>random</option></select></div>
  <div><label class="fl">پورت (پیش‌فرض ۴۴۳)</label><input class="inp" id="f-port" type="number" min="1" max="65535" value="443"></div>
</div>
<label class="fl" style="margin-top:12px">یادداشت (اختیاری)</label><input class="inp" id="f-note" placeholder="برای خودت...">
<div class="m-acts"><button class="btn pri" onclick="doNewLink()"><i class="ti ti-plus"></i> ساخت کانفیگ</button>
<button class="btn" onclick="closeModal()">انصراف</button></div>`)}
async function doNewLink(){try{
const body={label:$('f-label').value.trim()||'کانفیگ جدید',
limit_value:parseFloat($('f-limit').value||0),limit_unit:$('f-limit-unit').value,
expires_days:parseInt($('f-exp').value||0),ip_limit:parseInt($('f-ip').value||0),
speed_limit_value:parseFloat($('f-speed').value||0),speed_limit_unit:$('f-speed-unit').value,
protocol:$('f-proto').value,fingerprint:$('f-fp').value,port:parseInt($('f-port').value||443),
note:$('f-note').value.trim()};
const d=await api('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
closeModal();await loadLinks();toast('کانفیگ «'+d.label+'» ساخته شد ✅');
showQR(d.vless_link,d.label,'بعد از ساخت، QR رو اسکن کن یا لینک رو کپی کن:')}
catch(e){toast('خطا در ساخت: '+e.message,'err')}}
function openEditLink(uid){const l=cachedLinks.find(x=>x.uuid===uid);if(!l)return;
openModal(`
<h3><i class="ti ti-settings"></i> ویرایش «${esc(l.label)}»</h3>
<label class="fl">نام</label><input class="inp" id="e-label" value="${esc(l.label)}">
<div class="frow" style="margin-top:12px">
  <div><label class="fl">حجم (۰ = نامحدود)</label><input class="inp" id="e-limit" type="number" min="0" step="any" value="${l.limit_bytes>0?(l.limit_bytes/1073741824).toFixed(2):0}"></div>
  <div><label class="fl">محدودیت IP</label><input class="inp" id="e-ip" type="number" min="0" value="${l.ip_limit||0}"></div>
</div>
<div class="frow" style="margin-top:12px">
  <div><label class="fl">انقضا (روز از الان — ۰ = بی‌نهایت)</label><input class="inp" id="e-exp" type="number" min="0" value="0"></div>
  <div><label class="fl">سرعت (۰ = نامحدود)</label><input class="inp" id="e-speed" type="number" min="0" step="any" value="${l.speed_limit_bytes>0?(l.speed_limit_bytes*8/1048576).toFixed(1):0}"></div>
</div>
<label class="fl" style="margin-top:12px">یادداشت</label><input class="inp" id="e-note" value="${esc(l.note||'')}">
<div class="m-acts">
  <button class="btn pri" onclick="doEditLink('${uid}')"><i class="ti ti-device-floppy"></i> ذخیره</button>
  <button class="btn" onclick="doResetUsage('${uid}')"><i class="ti ti-restore"></i> صفر کردن مصرف</button>
  <button class="btn" onclick="closeModal()">انصراف</button></div>`)}
async function doEditLink(uid){try{
const body={label:$('e-label').value.trim(),
limit_value:parseFloat($('e-limit').value||0),limit_unit:'GB',
expires_days:parseInt($('e-exp').value||0),
ip_limit:parseInt($('e-ip').value||0),
speed_limit_value:parseFloat($('e-speed').value||0),speed_limit_unit:'MBIT',
note:$('e-note').value.trim()};
await api('/api/links/'+uid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
closeModal();await loadLinks();toast('ذخیره شد ✅')}catch(e){toast('خطا در ذخیره: '+e.message,'err')}}
async function doResetUsage(uid){try{await api('/api/links/'+uid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});
toast('مصرف صفر شد ✅');await loadLinks()}catch(e){toast('خطا: '+e.message,'err')}}
async function toggleLink(uid,active){try{await api('/api/links/'+uid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active})});
await loadLinks();toast(active?'فعال شد ✅':'غیرفعال شد')}catch(e){toast('خطا: '+e.message,'err')}}
async function delLink(uid,label){if(!confirm('کانفیگ «'+label+'» حذف بشه؟ این کار برگشتی نداره!'))return;
try{await api('/api/links/'+uid,{method:'DELETE'});await loadLinks();toast('حذف شد')}catch(e){toast('خطا در حذف: '+e.message,'err')}}

/* ═══ QR ═══ */
let qrTimer=null;
function showQR(text,label,extra=''){
openModal(`<div class="qr-wrap">
<h3 style="align-self:flex-start"><i class="ti ti-qrcode"></i> ${esc(label||'QR')}</h3>
<div id="qr-img"></div>${extra?`<div style="font-size:12px;color:var(--t2);text-align:center">${esc(extra)}</div>`:''}
<div class="qr-link">${esc(text)}</div>
<div class="m-acts" style="align-self:stretch">
<button class="btn pri" onclick="copyTxt(document.querySelector('.qr-link').textContent)"><i class="ti ti-copy"></i> کپی لینک</button>
<button class="btn" onclick="closeModal()">بستن</button></div></div>`);
const box=$('qr-img');box.innerHTML='';
try{new QRCode(box,{text:text,width:210,height:210,colorDark:'#04070d',colorLight:'#ffffff',correctLevel:QRCode.CorrectLevel.M})}
catch(e){box.innerHTML='<div style="color:#333;padding:20px;font-size:11px">QR در دسترس نیست — لینک را کپی کن</div>'}}

/* ═══ Sub groups ═══ */
let SUBS_CACHE=[];
async function loadSubs(){try{const [d,ld]=await Promise.all([api('/api/subs'),api('/api/links')]);
cachedLinks=ld.links;SUBS_CACHE=d.subs;const el=$('subs-list');
if(!d.subs.length){el.innerHTML='<div class="empty"><i class="ti ti-folders"></i>گروهی نداری — «گروه جدید» بساز تا لینک اختصاصی بت بدی.</div>';return}
el.innerHTML=d.subs.map(s=>`
<div class="row">
  <span class="st-dot ${s.active_count>0?'ok':'off'}"></span>
  <div class="r-main">
    <div class="r-title">${esc(s.name)} <span class="chip def">${fa(s.links_count)} کانفیگ · ${fa(s.active_count)} فعال</span>${s.has_password?'<span class="chip am"><i class="ti ti-lock"></i> رمزدار</span>':''}</div>
    <div class="r-meta"><span><i class="ti ti-info-circle"></i> ${esc(s.desc||'بدون توضیح')}</span>
    <span><i class="ti ti-database"></i> مصرف کل: ${esc(s.total_used_fmt)}</span></div>
  </div>
  <div class="acts">
    <button class="btn sm" title="صفحه‌ی عمومی" onclick="window.open('${esc(s.public_url)}')"><i class="ti ti-external-link"></i></button>
    <button class="btn sm" title="ساب URL" onclick="showQR('${esc(s.sub_url)}','ساب گروه: ${esc(s.name)}')"><i class="ti ti-qrcode"></i></button>
    <button class="btn sm" title="مدیریت" onclick="openManageSub('${s.sub_id}')"><i class="ti ti-settings"></i></button>
    <button class="btn sm dgr" title="حذف" onclick="delSub('${s.sub_id}','${esc(s.name)}')"><i class="ti ti-trash"></i></button>
  </div>
</div>`).join('')}catch(e){toast('خطا: '+e.message,'err')}}
function openNewSub(){openModal(`
<h3><i class="ti ti-folders"></i> گروه ساب جدید</h3>
<label class="fl">نام گروه</label><input class="inp" id="s-name" placeholder="مثلاً: مشتری‌های ویژه">
<label class="fl" style="margin-top:12px">توضیح (اختیاری)</label><input class="inp" id="s-desc" placeholder="...">
<label class="fl" style="margin-top:12px">رمز عبور (اختیاری — خالی = بدون رمز)</label><input class="inp" id="s-pw" placeholder="برای محافظت از ساب">
<div class="m-acts"><button class="btn pri" onclick="doNewSub()"><i class="ti ti-plus"></i> ساخت گروه</button>
<button class="btn" onclick="closeModal()">انصراف</button></div>`)}
async function doNewSub(){try{
const d=await api('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},
body:JSON.stringify({name:$('s-name').value.trim()||'گروه جدید',desc:$('s-desc').value.trim(),password:$('s-pw').value})});
closeModal();await loadSubs();toast('گروه ساخته شد ✅');
showQR(d.sub_url,'ساب گروه: '+d.name,'این لینک رو در اختیار مشتری بذار')}
catch(e){toast('خطا: '+e.message,'err')}}
function openManageSub(sid){const s=SUBS_CACHE.find(x=>x.sub_id===sid);if(!s)return;
const assigned=new Set(s.link_ids||[]);
const opts=cachedLinks.map(l=>`<label style="display:flex;gap:9px;align-items:center;padding:7px 4px;border-bottom:1px dashed rgba(80,120,190,.12);font-size:13px;cursor:pointer">
<input type="checkbox" value="${l.uuid}" ${assigned.has(l.uuid)?'checked':''} onchange="toggleSubLink('${sid}','${l.uuid}',this.checked)">
<span style="flex:1">${esc(l.label)}</span>${statusChip(l)}</label>`).join('');
openModal(`<h3><i class="ti ti-settings"></i> مدیریت «${esc(s.name)}»</h3>
<label class="fl">نام</label><input class="inp" id="ms-name" value="${esc(s.name)}">
<label class="fl" style="margin-top:12px">توضیح</label><input class="inp" id="ms-desc" value="${esc(s.desc||'')}">
<label class="fl" style="margin-top:12px">رمز جدید (خالی = بدون تغییر)</label><input class="inp" id="ms-pw" placeholder="برای حذف رمز، بنویس: -">
<label class="fl" style="margin-top:14px">کانفیگ‌های این گروه</label>
<div style="max-height:220px;overflow-y:auto;border:1px solid var(--line);border-radius:10px;padding:4px 12px">${opts||'<div class="empty">اول یه کانفیگ بساز</div>'}</div>
<div class="copybox" style="margin-top:12px"><span class="cu">${esc(s.sub_url)}</span>
<button class="btn sm" onclick="copyTxt(document.querySelector('#ovl.on .copybox .cu').textContent)"><i class="ti ti-copy"></i></button></div>
<div class="m-acts"><button class="btn pri" onclick="doSaveSub('${sid}')"><i class="ti ti-device-floppy"></i> ذخیره</button>
<button class="btn" onclick="closeModal()">بستن</button></div>`)}
async function doSaveSub(sid){try{
const body={name:$('ms-name').value.trim(),desc:$('ms-desc').value.trim()};
const pw=$('ms-pw').value;if(pw)body.password=pw==='-'?'':pw;
await api('/api/subs/'+sid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body));
await loadSubs();toast('ذخیره شد ✅')}catch(e){toast('خطا: '+e.message,'err')}}
async function toggleSubLink(sid,lid,add){try{
await api(`/api/subs/${sid}/links`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_id:lid,action:add?'add':'remove'})});
toast(add?'اضافه شد ✅':'حذف شد')}catch(e){toast('خطا: '+e.message,'err');event.target.checked=!add}}
async function delSub(sid,name){if(!confirm('گروه «'+name+'» حذف بشه؟ (کانفیگ‌ها حذف نمی‌شن)'))return;
try{await api('/api/subs/'+sid,{method:'DELETE'});await loadSubs();toast('حذف شد')}catch(e){toast('خطا: '+e.message,'err')}}

/* ═══ Connections ═══ */
async function loadConns(){try{const d=await api('/api/connections');
$('conn-count').textContent=fa(d.count);$('conn-raw').textContent=fa(d.raw_count);
$('nb-conns').textContent=fa(d.count);const el=$('conns-list');
if(!d.connections.length){el.innerHTML='<div class="empty"><i class="ti ti-plug-off"></i>هیچ‌کس وصل نیست — اولین اتصال که بیاد اینجا می‌بینیش.</div>';return}
el.innerHTML=d.connections.map(c=>`
<div class="row">
  <span class="st-dot ok"></span>
  <div class="r-main">
    <div class="r-title" style="direction:ltr;text-align:right;font-family:ui-monospace">${esc(c.ip)}</div>
    <div class="r-meta"><span><i class="ti ti-link"></i> ${esc(c.label)}</span>
    <span><i class="ti ti-arrows-split"></i> ${fa(c.sessions)} سشن</span>
    <span><i class="ti ti-clock"></i> آخرین: ${timeFa(c.last_connected_at)}</span></div>
  </div>
  <span class="chip gr" style="margin-right:auto">${esc(c.bytes_fmt)}</span>
</div>`).join('')}catch(e){toast('خطا: '+e.message,'err')}}

/* ═══ Logs ═══ */
const LOG_ICON={link:'ti-link',sub:'ti-folders',auth:'ti-shield-lock',system:'ti-server',tg:'ti-brand-telegram'};
async function loadLogs(){try{const d=await api('/api/activity');const el=$('logs-list');
if(!d.logs.length){el.innerHTML='<div class="empty"><i class="ti ti-moon"></i>هنوز رویدادی ثبت نشده</div>';return}
el.innerHTML=d.logs.slice().reverse().map(l=>`
<div class="log-it"><i class="ti ${LOG_ICON[l.kind]||'ti-dot'} ${'log-'+(l.level||'info')}"></i>
<div style="flex:1">${esc(l.message)}</div><span class="log-t">${timeFa(l.time)}</span></div>`).join('')}
catch(e){toast('خطا: '+e.message,'err')}}

/* ═══ Boot & auto-refresh ═══ */
async function checkAuth(){try{const d=await api('/api/me');if(!d.authenticated)location.href='/login'}
catch(e){}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
(async function(){await checkAuth();await loadOverview();loadLinks();
setInterval(()=>{if(curPg==='overview')loadOverview();else if(curPg==='conns')loadConns()},8000)})();
"""
