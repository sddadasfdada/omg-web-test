# panel.py — X4G NEON Panel (جمع‌کننده‌ی CSS/HTML/JS و رندر صفحه‌ی نهایی)
from panel_css import PANEL_CSS
from panel_html import PANEL_HTML
from panel_js1 import PANEL_JS1
from panel_js2 import PANEL_JS2

PANEL_PAGE: str = (
    PANEL_HTML
    .replace("__PANEL_CSS__", PANEL_CSS)
    .replace("__PANEL_JS1__", PANEL_JS1)
    .replace("__PANEL_JS2__", PANEL_JS2)
)

# صفحه‌ی لندینگ کوچیک برای روت «/» — با دکمه‌ی ورود به پنل
LANDING_PAGE: str = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>X4G</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Vazirmatn',sans-serif;background:#04070d;color:#e9f2ff;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(700px 400px at 50% 0%,rgba(34,211,238,.12),transparent 65%),radial-gradient(600px 400px at 80% 100%,rgba(167,139,250,.1),transparent 60%)}
.wrap{position:relative;text-align:center;max-width:420px;width:100%}
.logo{width:86px;height:86px;margin:0 auto 18px;border-radius:24px;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:800;color:#04121a;background:linear-gradient(135deg,#22d3ee,#a78bfa);box-shadow:0 0 45px rgba(34,211,238,.5)}
h1{font-size:26px;font-weight:800;letter-spacing:.02em}
.sub{color:#8ba6cf;font-size:13px;margin:8px 0 26px;line-height:2}
.acts{display:flex;flex-direction:column;gap:11px}
a.btn{display:flex;align-items:center;justify-content:center;gap:9px;padding:14px;border-radius:13px;text-decoration:none;font-weight:700;font-size:14.5px;transition:.2s;border:1px solid rgba(80,120,190,.25);color:#e9f2ff;background:rgba(13,21,38,.7)}
a.btn:hover{border-color:rgba(34,211,238,.5);transform:translateY(-2px)}
a.btn.pri{background:linear-gradient(135deg,rgba(34,211,238,.25),rgba(167,139,250,.3));border-color:rgba(34,211,238,.5);box-shadow:0 8px 30px rgba(34,211,238,.18)}
.foot{margin-top:26px;font-size:11px;color:#4f6590}
.foot a{color:#8ba6cf;text-decoration:none}
</style>
</head>
<body>
<div class="wrap">
  <div class="logo">X4</div>
  <h1>X4G NEON</h1>
  <div class="sub">پنل مدیریت کانفیگ و اشتراک وی‌پی‌ان<br>سرور فعال و در حال سرویس‌دهی است</div>
  <div class="acts">
    <a class="btn pri" href="/panel"><i class="ti ti-gauge"></i> ورود به پنل مدیریت</a>
    <a class="btn" href="/login"><i class="ti ti-layout-dashboard"></i> پنل کلاسیک</a>
  </div>
  <div class="foot">X4G v9.5 · <a href="https://t.me/Farajian2004f" target="_blank"><i class="ti ti-brand-telegram"></i> پشتیبانی</a></div>
</div>
</body>
</html>"""
