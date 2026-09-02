# panel_css.py — استایل پنل X4G NEON (تیره، نئونی، RTL)
PANEL_CSS = r"""
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#04070d;--bg2:#0a1120;--card:rgba(13,21,38,.85);--line:rgba(80,120,190,.16);
--tx:#e9f2ff;--t2:#8ba6cf;--t3:#4f6590;--cy:#22d3ee;--vi:#a78bfa;--gr:#34d399;--rd:#f87171;--am:#fbbf24;--rad:14px}
html{scrollbar-color:#1d2c4a transparent;scrollbar-width:thin}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--tx);height:100vh;display:flex;overflow:hidden}
body::before{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;
background:radial-gradient(900px 500px at 85% -10%,rgba(34,211,238,.09),transparent 60%),radial-gradient(800px 500px at 10% 110%,rgba(167,139,250,.08),transparent 60%)}
::-webkit-scrollbar{width:8px;height:8px}::-webkit-scrollbar-thumb{background:#1d2c4a;border-radius:8px}
button{font-family:inherit}.ti{vertical-align:middle}
/* ───── Sidebar ───── */
.side{width:236px;flex-shrink:0;background:var(--bg2);border-left:1px solid var(--line);display:flex;flex-direction:column;padding:18px 14px 14px;gap:4px;z-index:5}
.brand{display:flex;align-items:center;gap:11px;padding:4px 8px 16px}
.logo{width:42px;height:42px;border-radius:12px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;color:#04121a;
background:linear-gradient(135deg,var(--cy),var(--vi));box-shadow:0 0 22px rgba(34,211,238,.45)}
.brand b{font-size:17px;letter-spacing:.04em}
.brand small{display:block;font-size:10px;color:var(--t3);margin-top:1px}
.nav-lbl{font-size:10px;color:var(--t3);padding:10px 10px 4px;letter-spacing:.12em}
.nav-it{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:11px;cursor:pointer;color:var(--t2);font-size:13.5px;font-weight:500;transition:.15s;border:1px solid transparent;user-select:none}
.nav-it i{font-size:18px}
.nav-it:hover{color:var(--tx);background:rgba(34,211,238,.05)}
.nav-it.on{color:var(--tx);background:linear-gradient(90deg,rgba(34,211,238,.12),rgba(167,139,250,.08));border-color:rgba(34,211,238,.25);box-shadow:inset 3px 0 0 var(--cy)}
.nav-badge{margin-right:auto;background:rgba(34,211,238,.15);color:var(--cy);font-size:10.5px;font-weight:700;padding:1px 8px;border-radius:20px;min-width:22px;text-align:center}
.side-foot{margin-top:auto;padding:10px;border-top:1px solid var(--line);font-size:10.5px;color:var(--t3);line-height:1.9}
.side-foot a{color:var(--t2)}
/* ───── Main ───── */
.main{flex:1;display:flex;flex-direction:column;min-width:0;z-index:1}
.topbar{display:flex;align-items:center;gap:12px;padding:14px 22px;border-bottom:1px solid var(--line);background:rgba(10,17,32,.6);backdrop-filter:blur(10px)}
.tb-title{font-size:16.5px;font-weight:700}
.tb-sub{font-size:11px;color:var(--t3);margin-top:1px}
.tb-right{margin-right:auto;display:flex;align-items:center;gap:8px}
.badge{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:600;padding:5px 12px;border-radius:20px;border:1px solid var(--line);color:var(--t2);background:rgba(13,21,38,.6)}
.badge .dot{width:7px;height:7px;border-radius:50%}
.dot.g{background:var(--gr);box-shadow:0 0 8px var(--gr)}
.dot.pulse{animation:pl 1.6s infinite}
@keyframes pl{50%{opacity:.35}}
.content{flex:1;overflow-y:auto;padding:20px 22px 40px}
.pg{display:none}.pg.on{display:block;animation:fu .25s ease}
@keyframes fu{from{opacity:0;transform:translateY(6px)}to{opacity:1}}
/* ───── Cards & grid ───── */
.grid{display:grid;gap:14px}
.g4{grid-template-columns:repeat(4,1fr)}.g2{grid-template-columns:repeat(2,1fr)}
@media(max-width:1100px){.g4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.g4,.g2{grid-template-columns:1fr}.side{width:64px}.side .brand b,.side .brand small,.nav-lbl,.nav-it span,.side-foot{display:none}.nav-it{justify-content:center}}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);padding:16px 18px;backdrop-filter:blur(12px)}
.card h3{font-size:13.5px;font-weight:700;margin-bottom:12px;display:flex;align-items:center;gap:8px}
.card h3 i{color:var(--cy)}
.stat{position:relative;overflow:hidden}
.stat .lbl{font-size:11.5px;color:var(--t2);display:flex;align-items:center;gap:7px}
.stat .val{font-size:26px;font-weight:800;margin-top:8px;letter-spacing:-.02em}
.stat .sub{font-size:10.5px;color:var(--t3);margin-top:4px}
.stat .glow{position:absolute;left:-20px;top:-20px;width:90px;height:90px;border-radius:50%;filter:blur(38px);opacity:.35}
.glow.c{background:var(--cy)}.glow.v{background:var(--vi)}.glow.g{background:var(--gr)}.glow.a{background:var(--am)}
/* ───── Chart ───── */
.chart{display:flex;align-items:flex-end;gap:6px;height:150px;padding-top:10px}
.cbar{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;min-width:0}
.cbar .bar{border-radius:6px 6px 3px 3px;background:linear-gradient(180deg,var(--cy),rgba(167,139,250,.55));min-height:3px;transition:height .4s;cursor:default}
.cbar .h{font-size:9px;color:var(--t3);text-align:center;white-space:nowrap;overflow:hidden}
/* ───── Table-ish rows ───── */
.rows{display:flex;flex-direction:column;gap:10px}
.row{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:13px 16px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.row:hover{border-color:rgba(34,211,238,.35)}
.st-dot{width:9px;height:9px;border-radius:50%;flex-shrink:0}
.st-dot.ok{background:var(--gr);box-shadow:0 0 8px var(--gr)}
.st-dot.off{background:#475569}
.st-dot.exp{background:var(--rd);box-shadow:0 0 8px var(--rd)}
.st-dot.full{background:var(--am);box-shadow:0 0 8px var(--am)}
.r-main{min-width:180px;flex:1}
.r-title{font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px}
.r-meta{font-size:10.5px;color:var(--t3);margin-top:3px;display:flex;gap:12px;flex-wrap:wrap}
.chip{font-size:10px;font-weight:700;padding:2px 9px;border-radius:20px;border:1px solid}
.chip.ws{color:var(--cy);border-color:rgba(34,211,238,.4);background:rgba(34,211,238,.08)}
.chip.xh{color:var(--vi);border-color:rgba(167,139,250,.4);background:rgba(167,139,250,.08)}
.chip.gr{color:var(--gr);border-color:rgba(52,211,153,.4);background:rgba(52,211,153,.08)}
.chip.rd{color:var(--rd);border-color:rgba(248,113,113,.4);background:rgba(248,113,113,.08)}
.chip.am{color:var(--am);border-color:rgba(251,191,36,.4);background:rgba(251,191,36,.08)}
.chip.def{color:var(--t2);border-color:var(--line);background:rgba(80,120,190,.08)}
.usage{width:150px}
.usage .u-lbl{display:flex;justify-content:space-between;font-size:10px;color:var(--t3);margin-bottom:4px}
.u-bar{height:5px;border-radius:6px;background:rgba(80,120,190,.15);overflow:hidden}
.u-fill{height:100%;border-radius:6px;background:linear-gradient(90deg,var(--gr),var(--cy));transition:width .4s}
.u-fill.warn{background:linear-gradient(90deg,var(--am),var(--rd))}
.acts{display:flex;gap:6px;margin-right:auto}
/* ───── Buttons ───── */
.btn{border:1px solid var(--line);background:rgba(80,120,190,.1);color:var(--tx);border-radius:10px;padding:8px 14px;font-size:12.5px;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:7px;transition:.15s}
.btn:hover{background:rgba(34,211,238,.12);border-color:rgba(34,211,238,.4)}
.btn.sm{padding:6px 9px;font-size:12px;border-radius:9px}
.btn.pri{background:linear-gradient(135deg,rgba(34,211,238,.2),rgba(167,139,250,.25));border-color:rgba(34,211,238,.45);box-shadow:0 0 18px rgba(34,211,238,.15)}
.btn.dgr{color:#fca5a5}.btn.dgr:hover{background:rgba(248,113,113,.12);border-color:rgba(248,113,113,.4)}
.btn.ok{color:#86efac}.btn.ok:hover{background:rgba(52,211,153,.12);border-color:rgba(52,211,153,.4)}
/* ───── Inputs ───── */
.inp,select.inp,textarea.inp{width:100%;background:rgba(4,8,16,.55);border:1px solid var(--line);border-radius:10px;color:var(--tx);padding:10px 13px;font-family:inherit;font-size:13px;outline:none;transition:.15s}
.inp:focus{border-color:rgba(34,211,238,.55);box-shadow:0 0 0 3px rgba(34,211,238,.08)}
select.inp option{background:#0a1120}
label.fl{display:block;font-size:11px;color:var(--t2);font-weight:600;margin:0 2px 6px}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.toolbar{display:flex;gap:10px;align-items:center;margin-bottom:14px;flex-wrap:wrap}
.toolbar .inp{width:auto;min-width:200px;flex:1;max-width:340px}
/* ───── Modal ───── */
.ovl{position:fixed;inset:0;background:rgba(2,5,10,.75);backdrop-filter:blur(6px);z-index:50;display:none;align-items:center;justify-content:center;padding:20px}
.ovl.on{display:flex;animation:fu .18s ease}
.modal{background:#0b1322;border:1px solid rgba(34,211,238,.25);border-radius:18px;width:100%;max-width:520px;max-height:88vh;overflow-y:auto;padding:22px;box-shadow:0 0 60px rgba(34,211,238,.12),0 30px 80px rgba(0,0,0,.6)}
.modal h3{font-size:15px;margin-bottom:16px;display:flex;align-items:center;gap:9px}
.modal h3 i{color:var(--cy)}
.m-acts{display:flex;gap:9px;margin-top:18px;justify-content:flex-start}
/* ───── QR ───── */
.qr-wrap{display:flex;flex-direction:column;align-items:center;gap:12px}
#qr-img{background:#fff;padding:10px;border-radius:14px}
.qr-link{font-family:ui-monospace,monospace;font-size:10.5px;color:var(--t2);word-break:break-all;text-align:center;background:rgba(4,8,16,.5);border:1px solid var(--line);border-radius:10px;padding:9px 12px;max-width:100%}
/* ───── Logs ───── */
.log-it{display:flex;gap:10px;align-items:flex-start;padding:9px 12px;border-bottom:1px solid rgba(80,120,190,.08);font-size:12.5px}
.log-it:last-child{border-bottom:none}
.log-t{font-size:10px;color:var(--t3);white-space:nowrap;margin-top:2px}
.log-ok{color:var(--gr)}.log-err{color:var(--rd)}.log-warn{color:var(--am)}.log-info{color:var(--cy)}
/* ───── Toast ───── */
#toasts{position:fixed;bottom:18px;right:18px;z-index:99;display:flex;flex-direction:column;gap:8px}
.toast{background:#0b1322;border:1px solid rgba(34,211,238,.35);border-radius:12px;padding:11px 16px;font-size:12.5px;font-weight:600;display:flex;align-items:center;gap:9px;box-shadow:0 10px 30px rgba(0,0,0,.5);animation:tin .25s ease}
.toast.err{border-color:rgba(248,113,113,.5)}.toast.ok{border-color:rgba(52,211,153,.5)}
@keyframes tin{from{opacity:0;transform:translateY(10px)}}
.empty{text-align:center;color:var(--t3);font-size:12.5px;padding:34px 10px;line-height:2}
.empty i{font-size:30px;display:block;margin-bottom:6px;opacity:.5}
.copybox{display:flex;gap:6px;align-items:center;background:rgba(4,8,16,.5);border:1px solid var(--line);border-radius:10px;padding:8px 12px}
.copybox .cu{flex:1;font-family:ui-monospace,monospace;font-size:11px;color:var(--cy);direction:ltr;text-align:left;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.kv{display:flex;justify-content:space-between;font-size:12px;padding:7px 2px;border-bottom:1px dashed rgba(80,120,190,.12)}
.kv:last-child{border:none}
.kv b{direction:ltr}
"""
