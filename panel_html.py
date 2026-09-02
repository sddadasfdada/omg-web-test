# panel_html.py — بدنه‌ی HTML پنل X4G NEON
PANEL_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>X4G · پنل مدیریت</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<style>__PANEL_CSS__</style>
</head>
<body>

<!-- ═══════════ Sidebar ═══════════ -->
<aside class="side">
  <div class="brand">
    <div class="logo">X4</div>
    <div><b>X4G NEON</b><small>پنل مدیریت وی‌پی‌ان</small></div>
  </div>
  <div class="nav-lbl">مدیریت</div>
  <div class="nav-it on" data-pg="overview"><i class="ti ti-gauge"></i><span>داشبورد</span></div>
  <div class="nav-it" data-pg="links"><i class="ti ti-link"></i><span>کانفیگ‌ها</span><span class="nav-badge" id="nb-links">۰</span></div>
  <div class="nav-it" data-pg="subs"><i class="ti ti-folders"></i><span>گروه‌های ساب</span><span class="nav-badge" id="nb-subs">۰</span></div>
  <div class="nav-lbl">نظارت</div>
  <div class="nav-it" data-pg="conns"><i class="ti ti-plug-connected"></i><span>اتصال‌های زنده</span><span class="nav-badge" id="nb-conns">۰</span></div>
  <div class="nav-it" data-pg="logs"><i class="ti ti-activity"></i><span>لاگ رویدادها</span></div>
  <div class="side-foot">
    <div>X4G NEON v1.0</div>
    <div><a href="https://t.me/Farajian2004f" target="_blank"><i class="ti ti-brand-telegram"></i> پشتیبانی</a></div>
    <div style="margin-top:6px"><button class="btn sm dgr" onclick="logout()" style="width:100%;justify-content:center"><i class="ti ti-logout"></i> خروج</button></div>
  </div>
</aside>

<!-- ═══════════ Main ═══════════ -->
<div class="main">
  <div class="topbar">
    <div><div class="tb-title" id="tb-title">داشبورد</div><div class="tb-sub" id="tb-sub">در حال بارگذاری…</div></div>
    <div class="tb-right">
      <span class="badge"><span class="dot g pulse"></span> سرور فعال</span>
      <span class="badge"><i class="ti ti-clock"></i> <span id="uptime">—</span></span>
      <button class="btn sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button>
    </div>
  </div>

  <div class="content">

  <!-- ═══ صفحه ۱: داشبورد ═══ -->
  <section class="pg on" id="pg-overview">
    <div class="grid g4">
      <div class="card stat"><div class="glow c"></div>
        <div class="lbl"><i class="ti ti-plug-connected"></i> اتصال‌های زنده</div>
        <div class="val" id="st-conns">۰</div><div class="sub" id="st-ips">— آی‌پی یکتا</div></div>
      <div class="card stat"><div class="glow v"></div>
        <div class="lbl"><i class="ti ti-link"></i> کانفیگ‌ها</div>
        <div class="val" id="st-links">۰</div><div class="sub" id="st-links-sub">— فعال</div></div>
      <div class="card stat"><div class="glow g"></div>
        <div class="lbl"><i class="ti ti-traffic-cone"></i> ترافیک کل</div>
        <div class="val" id="st-traffic">۰</div><div class="sub">از ابتدای راه‌اندازی</div></div>
      <div class="card stat"><div class="glow a"></div>
        <div class="lbl"><i class="ti ti-folders"></i> گروه‌های ساب</div>
        <div class="val" id="st-subs">۰</div><div class="sub" id="st-req">— درخواست پردازش‌شده</div></div>
    </div>

    <div class="grid g2" style="margin-top:14px">
      <div class="card">
        <h3><i class="ti ti-chart-bar"></i> ترافیک ۲۴ ساعت اخیر</h3>
        <div class="chart" id="chart"></div>
      </div>
      <div class="card">
        <h3><i class="ti ti-alert-triangle"></i> آخرین خطاها</h3>
        <div id="err-list"><div class="empty"><i class="ti ti-check"></i>خطایی ثبت نشده — همه‌چیز سالمه ✨</div></div>
      </div>
    </div>

    <div class="card" style="margin-top:14px">
      <h3><i class="ti ti-rss"></i> سابسکریپشن کامل ادمین</h3>
      <div class="copybox"><span class="cu" id="sub-all-url">—</span>
        <button class="btn sm pri" onclick="copyTxt(document.getElementById('sub-all-url').textContent)"><i class="ti ti-copy"></i></button>
        <button class="btn sm" onclick="showQR(document.getElementById('sub-all-url').textContent,'سابسکریپشن کامل')"><i class="ti ti-qrcode"></i></button>
      </div>
      <div style="font-size:11px;color:var(--t3);margin-top:9px;line-height:1.9"><i class="ti ti-info-circle"></i> این آدرس فقط در مرورگری کار می‌کنه که توش لاگین هستی (کوکی سشن).</div>
    </div>
  </section>

  <!-- ═══ صفحه ۲: کانفیگ‌ها ═══ -->
  <section class="pg" id="pg-links">
    <div class="toolbar">
      <input class="inp" id="link-search" placeholder="جستجو بر اساس نام یا یادداشت…" oninput="renderLinks()">
      <button class="btn pri" onclick="openNewLink()"><i class="ti ti-plus"></i> کانفیگ جدید</button>
    </div>
    <div class="rows" id="links-list"></div>
  </section>

  <!-- ═══ صفحه ۳: گروه‌های ساب ═══ -->
  <section class="pg" id="pg-subs">
    <div class="toolbar">
      <button class="btn pri" onclick="openNewSub()"><i class="ti ti-plus"></i> گروه جدید</button>
    </div>
    <div class="rows" id="subs-list"></div>
  </section>

  <!-- ═══ صفحه ۴: اتصال‌های زنده ═══ -->
  <section class="pg" id="pg-conns">
    <div class="toolbar">
      <span class="badge"><i class="ti ti-plug-connected"></i> <span id="conn-count">۰</span> آی‌پی متصل</span>
      <span class="badge"><i class="ti ti-arrows-split"></i> <span id="conn-raw">۰</span> سشن خام</span>
      <button class="btn sm" onclick="loadConns()"><i class="ti ti-refresh"></i></button>
    </div>
    <div class="rows" id="conns-list"></div>
  </section>

  <!-- ═══ صفحه ۵: لاگ‌ها ═══ -->
  <section class="pg" id="pg-logs">
    <div class="toolbar">
      <button class="btn sm" onclick="loadLogs()"><i class="ti ti-refresh"></i> بروزرسانی</button>
    </div>
    <div class="card" style="padding:6px 4px" id="logs-list"></div>
  </section>

  </div>
</div>

<!-- ═══════════ Modal ═══════════ -->
<div class="ovl" id="ovl" onclick="if(event.target===this)closeModal()">
  <div class="modal" id="modal"></div>
</div>
<div id="toasts"></div>

<script>__PANEL_JS1__</script>
<script>__PANEL_JS2__</script>
</body>
</html>"""
