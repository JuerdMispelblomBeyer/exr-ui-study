# -*- coding: utf-8 -*-
BASE_CSS = '''    *, *::before, *::after { box-sizing: border-box; }
    body { margin: 0; background: #121416; font-family: Inter, "Helvetica Neue", Arial, sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: #F5C400; } a:hover { color: #FFDA4D; }
    .sg { font-family: "Space Grotesk", "Helvetica Neue", Arial, sans-serif; }
    .mono { font-family: "Roboto Mono", ui-monospace, "SF Mono", Menlo, monospace; }
    .t-title { font-family: "Space Grotesk", "Helvetica Neue", Arial, sans-serif; font-weight: 500; font-size: 22px; line-height: 28px; letter-spacing: -0.22px; color: #F8F9F7; }
    .t-object { font-family: "Space Grotesk", "Helvetica Neue", Arial, sans-serif; font-weight: 400; font-size: 15px; line-height: 20px; letter-spacing: -0.08px; color: #F8F9F7; }
    .t-eyebrow { font-size: 10px; line-height: 12px; letter-spacing: 1.3px; text-transform: uppercase; color: #6D757D; }
    .t-body { font-size: 13px; line-height: 20px; color: #CBD1D6; }
    .t-caption { font-size: 12px; line-height: 16px; color: #8B939B; }
    .t-micro { font-size: 11px; line-height: 14px; letter-spacing: 0.22px; color: #8B939B; }
    .t-data { font-family: "Roboto Mono", ui-monospace, Menlo, monospace; font-size: 12px; line-height: 18px; color: #CBD1D6; }
    .t-datas { font-family: "Roboto Mono", ui-monospace, Menlo, monospace; font-size: 10px; line-height: 14px; letter-spacing: 0.2px; color: #8B939B; }
    .plane { background: #171A1D; border: 1px solid #22262A; border-radius: 10px; }
    .rule { height: 1px; background: #212528; }
    .node { background: #1E2226; border-radius: 6px; }'''

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500'
         '&amp;family=Roboto+Mono:wght@400;500&amp;family=Space+Grotesk:wght@400;500&amp;display=swap">')

def page(body):
    return f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  {FONTS}
  <style>
{BASE_CSS}
  </style>
</helmet>

<div style="width: 1440px; height: 900px; position: relative; overflow: hidden; background: #121416;">
  <div style="position: absolute; inset: 0; background: radial-gradient(1100px 620px at 50% -10%, rgba(36,41,46,0.30), rgba(36,41,46,0) 70%); pointer-events: none;"></div>
{body}
</div>
</x-dc>
<script data-dc-script data-props='{{"$preview":{{"width":1440,"height":900}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

def catmull(P):
    d = ["M %.2f %.2f" % P[0]]
    n = len(P)
    for i in range(n-1):
        p0 = P[i-1] if i > 0 else P[0]
        p1, p2 = P[i], P[i+1]
        p3 = P[i+2] if i+2 < n else P[n-1]
        c1 = (p1[0] + (p2[0]-p0[0])/6.0, p1[1] + (p2[1]-p0[1])/6.0)
        c2 = (p2[0] - (p3[0]-p1[0])/6.0, p2[1] - (p3[1]-p1[1])/6.0)
        d.append("C %.2f %.2f %.2f %.2f %.2f %.2f" % (c1[0], c1[1], c2[0], c2[1], p2[0], p2[1]))
    return " ".join(d)

def spark(vals, w, h, lo=0.0, hi=100.0):
    n = len(vals)
    P = [(i*(w-2)/(n-1)+1, h-1 - (v-lo)/(hi-lo)*(h-2)) for i, v in enumerate(vals)]
    return catmull(P)

# ---------------------------------------------------------------- chrome
def header():
    return '''  <header style="position: relative; height: 56px; display: flex; align-items: center; gap: 16px; padding: 0 22px; border-bottom: 1px solid #212528;">
    <div style="display: flex; align-items: center; gap: 9px;">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M1.2 5.2V1.2h4M10.8 1.2h4v4M14.8 10.8v4h-4M5.2 14.8h-4v-4" stroke="#F5C400" stroke-width="1.4" stroke-linecap="square"></path></svg>
      <span style="font-size: 11px; letter-spacing: 1.1px; color: #CBD1D6; font-weight: 500;">EXROBOTICS</span>
    </div>
    <div style="width: 1px; height: 22px; background: #212528;"></div>

    <div style="display: flex; align-items: center; gap: 10px; height: 34px; padding: 0 12px; border: 1px solid #2A2E33; border-radius: 6px;">
      <span class="t-object">EXR-04</span>
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 4.6L6 7.6l3-3" stroke="#8B939B" stroke-width="1.2"></path></svg>
    </div>

    <div style="display: flex; align-items: center; gap: 7px;">
      <svg width="10" height="10" viewBox="0 0 10 10" fill="none"><circle cx="5" cy="5" r="3.2" stroke="#757E88" stroke-width="1.3"></circle><circle cx="5" cy="5" r="1.2" fill="#757E88"></circle></svg>
      <span class="t-caption" style="color: #CBD1D6;">Connected</span>
      <span class="t-datas">0.8 s ago</span>
    </div>

    <div style="margin-left: auto; display: flex; align-items: center; gap: 14px;">
      <div style="text-align: right;">
        <div class="t-eyebrow">SAFETY CHAIN</div>
        <div style="display: flex; align-items: center; gap: 6px; justify-content: flex-end; margin-top: 3px;">
          <svg width="11" height="11" viewBox="0 0 11 11" fill="none"><circle cx="5.5" cy="5.5" r="4" stroke="#757E88" stroke-width="1.3"></circle><path d="M3.6 5.5l1.4 1.4 2.4-2.6" stroke="#757E88" stroke-width="1.3"></path></svg>
          <span class="t-caption" style="color: #CBD1D6;">Ready</span>
          <span class="t-datas">0.4 s</span>
        </div>
      </div>
      <div style="display: flex; align-items: center; gap: 9px; height: 36px; padding: 0 14px; border: 1px solid #3A3F44; border-radius: 6px;">
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M4.7 1.4h4.6L12.6 4.7v4.6L9.3 12.6H4.7L1.4 9.3V4.7z" stroke="#FF5765" stroke-width="1.3" stroke-linejoin="round"></path></svg>
        <span class="t-body" style="color: #F8F9F7;">Safety Stop</span>
      </div>
    </div>
  </header>
'''

RAIL_ICONS = {
 'inspect': '<rect x="2.5" y="3.5" width="15" height="5" rx="1" stroke="{c}" stroke-width="1.3"></rect><rect x="2.5" y="11.5" width="6.5" height="5" rx="1" stroke="{c}" stroke-width="1.3"></rect><path d="M12.5 11.5h5m-5 5h5" stroke="{c}" stroke-width="1.3"></path>',
 'diagnose': '<path d="M2 12h3l2.2-6.5L11 15.5l2-3.5h5" stroke="{c}" stroke-width="1.3" stroke-linejoin="round"></path>',
 'change': '<path d="M3 6h14M3 14h14" stroke="{c}" stroke-width="1.3"></path><circle cx="7.5" cy="6" r="2.2" fill="#171A1D" stroke="{c}" stroke-width="1.3"></circle><circle cx="13" cy="14" r="2.2" fill="#171A1D" stroke="{c}" stroke-width="1.3"></circle>'}

def rail(active):
    items = []
    for key, label in (('inspect', 'Inspect'), ('diagnose', 'Diagnose'), ('change', 'Change')):
        on = key == active
        c = '#F5C400' if on else '#8B939B'
        box = ('border: 1px solid #F5C400; background: rgba(245,196,0,0.07);' if on else 'border: 1px solid transparent;')
        lab = 'color: #F8F9F7;' if on else ''
        items.append(f'''<div style="width: 60px; height: 58px; border-radius: 8px; {box} display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px;">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">{RAIL_ICONS[key].replace('{c}', c)}</svg>
          <span class="t-micro" style="{lab}">{label}</span>
        </div>''')
    return '''    <nav style="width: 76px; border-right: 1px solid #212528; display: flex; flex-direction: column; align-items: center; padding: 14px 0 16px;">
      <div style="display: flex; flex-direction: column; align-items: center; gap: 6px;">
        ''' + '\n        '.join(items) + '''
      </div>
      <div style="margin-top: auto; width: 60px; height: 48px; display: flex; align-items: center; justify-content: center;">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="2.6" stroke="#6D757D" stroke-width="1.3"></circle><path d="M10 2.5v2.2M10 15.3v2.2M17.5 10h-2.2M4.7 10H2.5M15.3 4.7l-1.6 1.6M6.3 13.7l-1.6 1.6M15.3 15.3l-1.6-1.6M6.3 6.3L4.7 4.7" stroke="#6D757D" stroke-width="1.3"></path></svg>
      </div>
    </nav>
'''

def window_control():
    return '''<div style="height: 32px; padding: 0 12px; display: flex; align-items: center; gap: 9px; border-radius: 6px; border: 1px solid #2A2E33;">
            <span class="t-caption">window</span>
            <span class="t-data">20 min</span>
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 4.6L6 7.6l3-3" stroke="#8B939B" stroke-width="1.2"></path></svg>
          </div>'''

def lens_chips(active='Physical'):
    out = []
    for name in ('Physical', 'Network', 'Software', 'Time', 'Integration'):
        if name == active:
            out.append(f'<div style="height: 30px; padding: 0 11px; display: flex; align-items: center; border-radius: 6px; border: 1px solid #F5C400; background: rgba(245,196,0,0.07);"><span class="t-caption" style="color: #F8F9F7;">{name}</span></div>')
        else:
            out.append(f'<div style="height: 30px; padding: 0 11px; display: flex; align-items: center; border-radius: 6px;"><span class="t-caption" style="color: #6D757D;">{name}</span></div>')
    return '<div style="display: flex; align-items: center; gap: 2px;">' + ''.join(out) + '</div>'

WARN_GLYPH = '<svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M6 1.6l4.6 8.2H1.4z" stroke="#FF5765" stroke-width="1.2" stroke-linejoin="round"></path><path d="M6 4.8v2.2" stroke="#FF5765" stroke-width="1.2"></path><circle cx="6" cy="8.4" r="0.6" fill="#FF5765"></circle></svg>'

def scopebar(title, left_extra='', fact=''):
    return f'''      <div style="height: 44px; display: flex; align-items: center; gap: 16px;">
        <div class="t-title">{title}</div>
        {left_extra}
        <div style="margin-left: auto; display: flex; align-items: center; gap: 16px;">
          {fact}
          {window_control()}
        </div>
      </div>

      <div style="height: 14px;"></div>
'''

# ---------------------------------------------------------------- platform map
CPU_SERIES = {
 'intel':    [58,61,60,63,62,65,63,66,64,62,63,62],
 'jetson-1': [39,41,40,43,41,40,42,44,43,41,42,42],
 'jetson-2': [36,35,38,37,39,38,37,39,38,40,38,38],
}

def compute_node(name, x, faded=False):
    op = 'opacity: 0.6; ' if faded else ''
    d = spark(CPU_SERIES[name], 150, 16, 30, 70)
    return f'''<div style="position: absolute; left: {x}px; top: 206px; width: 210px; height: 56px; {op}background: #1E2226; border-radius: 6px; padding: 9px 14px;">
            <div class="t-object">{name}</div>
            <svg width="150" height="16" viewBox="0 0 150 16" fill="none" style="display: block; margin-top: 4px;"><path d="{d}" stroke="#6D757D" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"></path></svg>
          </div>'''

def sub_node(label, left, width, faded=False, fault=False, selected=False, suffix=''):
    op = 'opacity: 0.6; ' if faded else ''
    if fault:
        style = 'background: rgba(255,87,101,0.13); border: 1px solid #A83A48;'
        inner = f'<span class="t-object" style="font-size: 14px;">{label}</span>{WARN_GLYPH}'
        gap = 'gap: 7px;'
    else:
        style = 'background: #1E2226;'
        suf = f'<span class="t-datas" style="color: #6D757D;">{suffix}</span>' if suffix else ''
        inner = f'<span class="t-object" style="font-size: 14px;">{label}</span>{suf}'
        gap = 'gap: 8px;'
    just = 'space-between' if suffix and not fault else 'center'
    pad = 'padding: 0 11px;' if suffix and not fault else ''
    return f'''<div style="position: absolute; left: {left}px; top: 358px; width: {width}px; height: 34px; {op}{style} border-radius: 6px; display: flex; align-items: center; justify-content: {just}; {gap} {pad} white-space: nowrap;">{inner}</div>'''

def map_svg(selected=False):
    sel = ''
    if selected:
        sel = '''
            <path d="M197 262v68h309v28" stroke="rgba(245,196,0,0.12)" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"></path>
            <path d="M197 262v68h309v28" stroke="#F5C400" stroke-width="2" stroke-linejoin="round"></path>
            <circle cx="197" cy="330" r="3.5" fill="#F5C400"></circle>
            <circle cx="506" cy="330" r="3.5" fill="#F5C400"></circle>
            <path d="M443 362v-9h9M560 353h9v9M569 388v9h-9M452 397h-9v-9" stroke="#F5C400" stroke-width="1.5"></path>'''
    return f'''<svg width="992" height="498" viewBox="0 0 992 498" fill="none" style="position: absolute; left: 0; top: 0;">
            <path d="M540 82v18" stroke="#31363B" stroke-width="1"></path>
            <path d="M700 82v30h-72" stroke="#282D32" stroke-width="1" stroke-dasharray="4 4"></path>
            <path d="M540 134v42" stroke="#31363B" stroke-width="1"></path>
            <path d="M60 176h880" stroke="#383D42" stroke-width="2"></path>
            <path d="M197 176v30M497 176v30M797 176v30" stroke="#2C3136" stroke-width="1"></path>
            <path d="M197 262v68" stroke="#2C3136" stroke-width="1"></path>
            <path d="M120 262v96" stroke="#2C3136" stroke-width="1"></path>
            <path d="M286 262v32h280" stroke="#2C3136" stroke-width="1"></path>
            <path d="M197 330h493" stroke="#383D42" stroke-width="2"></path>
            <path d="M258 330v28M382 330v28M506 330v28M634 330v28" stroke="#2C3136" stroke-width="1"></path>
            <path d="M497 262v10h443M797 262v10h143" stroke="#282D32" stroke-width="1" stroke-dasharray="4 4"></path>
            <path d="M940 289v41" stroke="#282D32" stroke-width="1" stroke-dasharray="4 4"></path>
            <circle cx="940" cy="282" r="7" fill="#171A1D" stroke="#4A525A" stroke-width="1"></circle>
            <path d="M726 330h230" stroke="#383D42" stroke-width="2"></path>
            <path d="M776 330v28M900 330v28" stroke="#2C3136" stroke-width="1"></path>{sel}
          </svg>'''

def map_body(selected=False, fault=False, cropped=False):
    fade = fault
    gpio_cells = ''.join(
        '<div style="width: 12px; height: 10px; border-radius: 2px; background: #434A51;"></div>' if on else
        '<div style="width: 12px; height: 10px; border-radius: 2px; background: #1A1E22;"></div>'
        for on in (1, 1, 0, 1, 0, 1, 1, 0))
    ms = sub_node('motor-drive', 448, 116, fault=fault) if fault else sub_node('motor-drive', 448, 116)
    return f'''{map_svg(selected)}
          <div style="position: absolute; left: 22px; top: 16px;"><span class="t-eyebrow">LIVE PLATFORM / EXR-04</span></div>
          <div style="position: absolute; right: 22px; top: 16px;"><span class="t-datas" style="color: #6D757D;">chrony &plusmn;0.4 ms &middot; 14:08:04</span></div>

          <div style="position: absolute; left: 22px; top: 48px;"><span class="t-eyebrow">OUTSIDE THE PLATFORM</span></div>
          <div style="position: absolute; left: 120px; top: 62px; width: 120px; text-align: center;"><span class="t-caption" style="color: #6D757D;">fleet-manager</span></div>
          <div style="position: absolute; left: 300px; top: 62px; width: 120px; text-align: center;"><span class="t-caption" style="color: #6D757D;">tailscale</span></div>
          <div style="position: absolute; left: 480px; top: 62px; width: 120px; text-align: center;"><span class="t-caption" style="color: #CBD1D6;">wi-fi</span></div>
          <div style="position: absolute; left: 640px; top: 62px; width: 120px; text-align: center;"><span class="t-caption" style="color: #6D757D;">cellular</span></div>
          <div style="position: absolute; left: 762px; top: 63px;"><span class="t-datas" style="color: #565E65;">standby</span></div>

          <div style="position: absolute; left: 452px; top: 100px; width: 176px; height: 34px; background: #1E2226; border-radius: 6px; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <span class="t-caption" style="color: #CBD1D6;">uplink</span><span class="t-datas" style="color: #6D757D;">vrrp master</span>
          </div>

          <div style="position: absolute; left: 60px; top: 154px;"><span class="t-datas" style="color: #6D757D;">onboard LAN &middot; 1 GbE</span></div>

          {compute_node('intel', 92)}
          {compute_node('jetson-1', 392)}
          {compute_node('jetson-2', 692)}

          <div style="position: absolute; left: 300px; top: 270px;"><span class="t-datas" style="color: #565E65;">usb3 &middot; switched</span></div>
          <div style="position: absolute; left: 566px; top: 277px; width: 134px; height: 34px; {'opacity: 0.6; ' if fade else ''}background: #1E2226; border-radius: 6px; display: flex; align-items: center; justify-content: center;">
            <span class="t-object" style="font-size: 14px;">drive camera</span>
          </div>

          <div style="position: absolute; left: 215px; top: 308px;"><span class="t-datas" style="color: #6D757D;">can0 &middot; 500 kbit/s &middot; intel-attached via motherboard</span></div>
          <div style="position: absolute; left: 726px; top: 308px;"><span class="t-datas" style="color: #6D757D;">comms box &middot; switched power</span></div>
          <div style="position: absolute; left: 800px; top: 290px; width: 128px; text-align: right;"><span class="t-datas" style="color: #8B939B;">host TBD</span></div>

          <div style="position: absolute; left: 64px; top: 358px; width: 112px; height: 34px; {'opacity: 0.6; ' if fade else ''}background: #1E2226; border-radius: 6px; display: flex; align-items: center; justify-content: center;">
            <span class="t-object" style="font-size: 14px;">gas adc</span>
          </div>
          <div style="position: absolute; left: 64px; top: 398px; width: 112px; text-align: center;"><span class="t-datas" style="color: #565E65;">4&ndash;20 mA analog</span></div>

          {sub_node('charging', 206, 104, faded=fade)}
          {sub_node('battery', 330, 104, faded=fade)}
          {ms}
          {sub_node('power gpio', 579, 110, faded=fade, suffix='&times;8')}
          <div style="position: absolute; left: 576px; top: 400px; display: flex; gap: 3px; {'opacity: 0.6;' if fade else ''}">{gpio_cells}</div>
          <div style="position: absolute; left: 579px; top: 416px; width: 110px; text-align: center;"><span class="t-datas" style="color: #565E65;">5 of 8 on</span></div>

          {sub_node('lidar', 720, 112, faded=fade, suffix='12 V')}
          {sub_node('inspection', 844, 112, faded=fade, suffix='36 V')}
'''

def map_plane(selected=False, fault=False):
    stall = ('\n          <div style="position: absolute; left: 440px; top: 398px; width: 132px; text-align: center;">'
             '<span class="t-datas" style="color: #FF5765;">Drive Stall &middot; latched</span></div>') if fault else ''
    legend = '''
          <div style="position: absolute; left: 22px; bottom: 18px; display: flex; align-items: center; gap: 18px;">
            <div style="display: flex; align-items: center; gap: 7px;"><svg width="18" height="3"><path d="M0 1.5h18" stroke="#383D42" stroke-width="2"></path></svg><span class="t-datas" style="color: #565E65;">physical bus</span></div>
            <div style="display: flex; align-items: center; gap: 7px;"><svg width="18" height="3"><path d="M0 1.5h18" stroke="#282D32" stroke-width="1" stroke-dasharray="4 4"></path></svg><span class="t-datas" style="color: #565E65;">unconfirmed attachment</span></div>
          </div>'''
    return f'''<div class="plane" style="width: 992px; height: 498px; position: relative; overflow: hidden;">
          {map_body(selected, fault)}{stall}{legend}
        </div>'''

def map_plane_cropped():
    stall = ('\n            <div style="position: absolute; left: 440px; top: 398px; width: 132px; text-align: center;">'
             '<span class="t-datas" style="color: #FF5765;">Drive Stall &middot; latched</span></div>')
    return f'''<div class="plane" style="width: 992px; height: 326px; position: relative; overflow: hidden;">
          <div style="position: absolute; left: 0; top: -152px; width: 992px; height: 498px;">
          {map_body(True, True)}{stall}
          </div>
          <div style="position: absolute; right: 22px; bottom: 12px;"><span class="t-datas" style="color: #565E65;">cropped to the selected path &middot; uplink layer above</span></div>
        </div>'''

# ---------------------------------------------------------------- panels
def attention_healthy():
    checks = [
        'all <span class="mono" style="font-size: 11px;">8</span> can0 identifiers in rate',
        'chrony offset within <span class="mono" style="font-size: 11px;">&plusmn;1 ms</span> on all hosts',
        'uplink owner stable &middot; no VRRP transition',
        'no container restarts',
    ]
    rows = ''.join(f'''<div style="display: flex; align-items: flex-start; gap: 10px; padding: 5px 0;">
              <svg width="12" height="12" viewBox="0 0 12 12" fill="none" style="margin-top: 3px; flex: none;"><path d="M2.2 6.2l2.5 2.5L9.8 3.4" stroke="#5F686F" stroke-width="1.4"></path></svg>
              <span class="t-caption" style="color: #A7AEB4;">{c}</span>
            </div>''' for c in checks)
    unknowns = ''.join(f'''<div style="display: flex; align-items: flex-start; gap: 10px; padding: 5px 0;">
              <svg width="12" height="12" viewBox="0 0 12 12" fill="none" style="margin-top: 3px; flex: none;"><circle cx="6" cy="6" r="4.4" stroke="#4A525A" stroke-width="1.2" stroke-dasharray="2.6 2.2"></circle></svg>
              <span class="t-caption" style="color: #A7AEB4;">{u}</span>
            </div>''' for u in (
        'comms-box host is jetson-1 or jetson-2',
        'gas detector channel map unconfirmed'))
    return f'''<div class="plane" style="width: 320px; height: 498px; padding: 20px; display: flex; flex-direction: column;">
          <div><span class="t-eyebrow">ATTENTION</span></div>
          <div style="margin-top: 12px; display: flex; align-items: flex-start; gap: 10px;">
            <svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="margin-top: 4px; flex: none;"><circle cx="7.5" cy="7.5" r="6" stroke="#5F686F" stroke-width="1.3"></circle><path d="M4.8 7.6l2 2 3.5-3.9" stroke="#5F686F" stroke-width="1.3"></path></svg>
            <span class="t-title" style="font-size: 18px; line-height: 24px;">Nothing needs attention</span>
          </div>
          <div style="margin-top: 8px; padding-left: 25px;"><span class="t-datas" style="color: #565E65;">last full analysis 14:08:04 &middot; 3 s ago</span></div>

          <div class="rule" style="margin: 20px 0 12px;"></div>
          <div><span class="t-eyebrow">VERIFIED IN THIS WINDOW</span></div>
          <div style="margin-top: 6px;">{rows}</div>

          <div class="rule" style="margin: 16px 0 12px;"></div>
          <div><span class="t-eyebrow">NOT ESTABLISHED</span></div>
          <div style="margin-top: 6px;">{unknowns}</div>

          <div style="margin-top: auto;"><span class="t-datas" style="color: #565E65;">health rolls up from observed sources only</span></div>
        </div>'''

INSP_SHELL = ('width: 320px; height: {h}px; position: relative; border-radius: 10px; border: 1px solid #353B41; '
  'background: linear-gradient(180deg, #252A2F 0%, #1D2125 100%); '
  'box-shadow: inset 0 1px 0 rgba(255,255,255,0.085), inset 0 10px 26px rgba(255,255,255,0.05), '
  'inset 0 -8px 22px rgba(0,0,0,0.20), 0 18px 44px -14px rgba(0,0,0,0.6); '
  'padding: 20px; display: flex; flex-direction: column; overflow: hidden;')

def kv(label, value, last=False):
    b = '' if last else ' border-bottom: 1px solid #2B3036;'
    return (f'<div style="display: flex; justify-content: space-between; align-items: baseline; padding: 6px 0;{b}">'
            f'<span class="t-caption">{label}</span><span class="t-data">{value}</span></div>')

def inspector(h=498, full=True):
    head = f'''<div style="position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: #F5C400; border-radius: 10px 0 0 10px;"></div>
          <div><span class="t-eyebrow">SELECTED OBJECT</span></div>
          <div style="margin-top: 8px; display: flex; align-items: baseline; justify-content: space-between;">
            <span class="t-title">motor-drive</span><span class="t-datas">0x2C1</span>
          </div>
          <div style="margin-top: 4px; display: flex; align-items: center; gap: 7px;">
            {WARN_GLYPH}<span class="t-body" style="color: #FF5765;">Fault &middot; Drive Stall latched</span>
          </div>'''
    rows = ('<div style="margin-top: 16px; display: flex; flex-direction: column;">'
            + kv('stall state', '<span style="color: #FF5765;">active &middot; latched</span>')
            + kv('peak current', '<span style="color: #FF8A3D;">62.4</span> / 55 A')
            + kv('overload', 'cleared 14:02:41', last=True)
            + '</div>')
    if full:
        mid = f'''<div style="margin-top: 16px;"><span class="t-body">Activated 14:02:11 after a motor overload. The overload has cleared; the state stays latched until it is manually deactivated.</span></div>
          {rows}
          <div style="margin-top: 16px;"><span class="t-eyebrow">IMPACT</span></div>
          <div style="margin-top: 6px;"><span class="t-caption" style="color: #A7AEB4;">Drive output inhibited. No other CAN subsystem affected.</span></div>
          <div style="margin-top: auto; padding-top: 14px; display: flex; gap: 8px;">
            <div style="height: 38px; flex: 1; border-radius: 6px; background: #F5C400; display: flex; align-items: center; justify-content: center;"><span style="font-size: 13px; line-height: 20px; color: #090B0A;">Review deactivation</span></div>
            <div style="height: 38px; padding: 0 14px; border-radius: 6px; border: 1px solid #3A3F44; display: flex; align-items: center; justify-content: center;"><span class="t-body">Evidence</span></div>
          </div>
          <div style="margin-top: 10px;"><span class="t-datas" style="color: #565E65;">remote deactivation not confirmed</span></div>'''
    else:
        mid = f'''{rows}
          <div style="margin-top: auto; padding-top: 14px; display: flex; gap: 8px;">
            <div style="height: 38px; flex: 1; border-radius: 6px; background: #F5C400; display: flex; align-items: center; justify-content: center;"><span style="font-size: 13px; line-height: 20px; color: #090B0A;">Review deactivation</span></div>
          </div>
          <div style="margin-top: 10px;"><span class="t-datas" style="color: #565E65;">src can0 0x2C1 &middot; state observed 0.8 s ago</span></div>'''
    return f'<div style="{INSP_SHELL.format(h=h)}">\n          {head}\n          {mid}\n        </div>'

# ---------------------------------------------------------------- bottom band
CHANGE_ROWS_HEALTHY = [
    ('13:47:12', 'config change <span class="mono" style="font-size: 11px; color: #CBD1D6;">chrony.conf</span>', 'intel'),
    ('13:31:55', 'container restart <span class="mono" style="font-size: 11px; color: #CBD1D6;">poi-manager</span>', 'jetson-1'),
    ('12:04:38', 'uplink failover cellular &rarr; wi-fi', 'vrrp'),
]
CHANGE_ROWS_FAULT = [
    ('14:02:41', 'overload cleared &middot; <span class="mono" style="font-size: 11px; color: #CBD1D6;">41.2 A</span>', 'observed'),
    ('14:02:11', '<span style="color: #F8F9F7;">Drive Stall activated &middot; latched</span>', 'fault'),
    ('14:02:09', 'current peak <span class="mono" style="font-size: 11px; color: #FF8A3D;">62.4 A</span> over <span class="mono" style="font-size: 11px;">55 A</span>', 'observed'),
]

def recent_change(rows, caption):
    body = ''
    for i, (t, text, src) in enumerate(rows):
        b = '' if i == len(rows)-1 else ' border-bottom: 1px solid #212528;'
        body += (f'<div style="display: flex; align-items: baseline; gap: 12px; padding: 8px 0;{b}">'
                 f'<span class="t-datas" style="width: 52px; flex: none;">{t}</span>'
                 f'<span class="t-caption" style="color: #A7AEB4; flex: 1;">{text}</span>'
                 f'<span class="t-datas" style="color: #565E65;">{src}</span></div>')
    return f'''<div style="width: 427px; flex: none; padding: 16px 20px; display: flex; flex-direction: column;">
            <div style="display: flex; align-items: baseline; justify-content: space-between;">
              <span class="t-object" style="font-size: 15px;">Recent change</span>
              <span class="t-datas" style="color: #565E65;">{caption}</span>
            </div>
            <div style="margin-top: 8px;">{body}</div>
          </div>'''

MEM = {'intel': 44, 'jetson-1': 57, 'jetson-2': 50}
THERM = {'intel': 62, 'jetson-1': 71, 'jetson-2': 67}

def compute_band():
    lanes = ''
    for name in ('intel', 'jetson-1', 'jetson-2'):
        d = spark(CPU_SERIES[name], 300, 22, 30, 70)
        lanes += f'''<div style="display: grid; grid-template-columns: 92px 300px minmax(0, 1fr) minmax(0, 1fr); gap: 0 24px; align-items: center; height: 32px;">
              <span class="t-object" style="font-size: 14px;">{name}</span>
              <svg width="300" height="22" viewBox="0 0 300 22" fill="none" style="display: block;"><path d="{d}" stroke="#6D757D" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"></path></svg>
              <div style="height: 4px; border-radius: 2px; background: #23282D;"><div style="width: {MEM[name]}%; height: 4px; border-radius: 2px; background: #6D757D;"></div></div>
              <div style="height: 4px; border-radius: 2px; background: #23282D;"><div style="width: {THERM[name]}%; height: 4px; border-radius: 2px; background: #6D757D;"></div></div>
            </div>'''
    return f'''<div style="flex: 1; min-width: 0; padding: 16px 20px; display: flex; flex-direction: column;">
            <div style="display: flex; align-items: baseline; justify-content: space-between;">
              <span class="t-object" style="font-size: 15px;">Compute</span>
              <span class="t-datas" style="color: #565E65;">3 hosts &middot; 15 min &middot; cpu scale 30&ndash;70 % &middot; select a host for exact values</span>
            </div>
            <div style="display: grid; grid-template-columns: 92px 300px minmax(0, 1fr) minmax(0, 1fr); gap: 0 24px; margin-top: 12px;">
              <span></span><span class="t-eyebrow">CPU LOAD</span><span class="t-eyebrow">MEMORY</span><span class="t-eyebrow">THERMAL</span>
            </div>
            <div style="margin-top: 4px;">{lanes}</div>
          </div>'''

CAN_GROUPS = [
    ('battery',     [('0x100', '50 Hz', None), ('0x101', '10 Hz', None), ('0x102', '10 Hz', None)]),
    ('charging',    [('0x181', '10 Hz', None)]),
    ('motor-drive', [('0x1A0', '100 Hz', None), ('0x2C1', '50 Hz', 'stall_active')]),
    ('power gpio',  [('0x200', '20 Hz', None), ('0x201', '20 Hz', None)]),
]

def can_band():
    def chip(mid, rate, state):
        dot = '#FF5765' if state else '#3A4148'
        sid = '#F8F9F7' if state else '#A7AEB4'
        extra = f'<span class="mono" style="font-size: 10px; color: #FF5765;">{state}</span>' if state else ''
        return (f'<div style="display: flex; align-items: center; gap: 7px; white-space: nowrap;">'
                f'<span style="width: 5px; height: 5px; border-radius: 3px; background: {dot}; display: inline-block;"></span>'
                f'<span class="mono" style="font-size: 12px; color: {sid};">{mid}</span>'
                f'<span class="t-datas" style="color: #6D757D;">{rate}</span>{extra}</div>')
    cols = [[], []]
    for i, (grp, msgs) in enumerate(CAN_GROUPS):
        chips = '<div style="display: flex; align-items: center; gap: 22px; flex-wrap: nowrap;">' + ''.join(chip(*m) for m in msgs) + '</div>'
        cols[i % 2].append(f'''<div style="display: flex; align-items: center; gap: 16px; height: 30px;">
                <span class="t-object" style="font-size: 14px; width: 96px; flex: none;">{grp}</span>
                {chips}
              </div>''')
    colhtml = ''.join(f'<div style="flex: 1; min-width: 0;">{"".join(c)}</div>' for c in cols)
    return f'''<div style="flex: 1; min-width: 0; padding: 16px 20px; display: flex; flex-direction: column;">
            <div style="display: flex; align-items: baseline; justify-content: space-between;">
              <span class="t-object" style="font-size: 15px;">can0 messages</span>
              <span class="t-datas" style="color: #565E65;">grouped by subsystem &middot; 8 expected &middot; 8 present &middot; 1 not nominal</span>
            </div>
            <div style="display: flex; gap: 28px; margin-top: 14px;">{colhtml}</div>
            <div style="margin-top: auto;"><span class="t-datas" style="color: #565E65;">gas adc reports through the motherboard analog path and has no can0 identifier</span></div>
          </div>'''

def bottom_band(kind):
    left = compute_band() if kind == 'compute' else can_band()
    rows, cap = (CHANGE_ROWS_HEALTHY, '3 in 6 h') if kind == 'compute' else (CHANGE_ROWS_FAULT, 'motor-drive')
    return f'''<div class="plane" style="height: 180px; display: flex; overflow: hidden;">
          {left}
          <div style="width: 1px; background: #212528;"></div>
          {recent_change(rows, cap)}
        </div>'''

def evidence_strip(meta, note, note_glyph='clock', action='Expand evidence'):
    g = ('<svg width="12" height="12" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="4.6" stroke="#5F686F" stroke-width="1.2"></circle><path d="M6 3.4V6l1.8 1.2" stroke="#5F686F" stroke-width="1.2"></path></svg>'
         if note_glyph == 'clock' else
         '<svg width="12" height="12" viewBox="0 0 12 12" fill="none"><circle cx="6" cy="6" r="4.6" stroke="#4A525A" stroke-width="1.2" stroke-dasharray="2.6 2.2"></circle></svg>')
    return f'''<div style="height: 44px; border: 1px solid #22262A; border-radius: 8px; display: flex; align-items: center; padding: 0 18px; gap: 16px;">
          <span class="t-eyebrow">EVIDENCE</span>
          <span class="t-datas" style="color: #6D757D;">{meta}</span>
          <div style="width: 1px; height: 16px; background: #212528;"></div>
          <div style="display: flex; align-items: center; gap: 8px;">{g}<span class="t-caption" style="color: #8B939B;">{note}</span></div>
          <div style="margin-left: auto; display: flex; align-items: center; gap: 8px;">
            <span class="t-caption" style="color: #A7AEB4;">{action}</span>
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 7.4L6 4.4l3 3" stroke="#8B939B" stroke-width="1.2"></path></svg>
          </div>
        </div>'''

# ---------------------------------------------------------------- evidence drawer
import math

def current_chart():
    X0, X1 = 46.0, 824.0
    YB = 112.0
    def yv(v): return YB - v * (104.0/70.0)
    pts_f = [(0.00,29),(0.08,31),(0.16,28),(0.24,33),(0.32,30),(0.40,35),(0.46,44),
             (0.490,56),(0.5075,62.4),(0.525,47),(0.545,18),(0.570,7),(0.64,6),
             (0.72,6.5),(0.80,6.0),(0.90,6.2),(1.00,6.0)]
    P = [(X0 + f*(X1-X0), yv(v)) for f, v in pts_f]
    curve = catmull(P)
    area = curve + " L %.2f %.2f L %.2f %.2f Z" % (X1, YB, X0, YB)
    step = 9.0 * math.sqrt(2.0)
    h = YB - 8.0
    lines, i = [], int(-h/step) - 1
    x = X0 + i*step
    while x < X1 + h:
        lines.append('<path d="M %.1f %.1f L %.1f %.1f"></path>' % (x, YB, x + h, YB - h))
        x += step
    hatch = "".join(lines)
    px = X0 + 0.5075*(X1-X0); py = yv(62.4); thr = yv(55)
    return f'''<svg width="860" height="120" viewBox="0 0 860 120" fill="none" style="display: block;">
              <g stroke="#25292D" stroke-width="1">
                <path d="M{X0} {YB:.0f}H{X1:.0f}"></path><path d="M{X0} {yv(20):.0f}H{X1:.0f}"></path>
                <path d="M{X0} {yv(40):.0f}H{X1:.0f}"></path><path d="M{X0} {yv(60):.0f}H{X1:.0f}"></path>
              </g>
              <g font-family="Roboto Mono, monospace" font-size="10" fill="#8B939B" text-anchor="end">
                <text x="36" y="{YB+3:.0f}">0</text><text x="36" y="{yv(20)+3:.0f}">20</text>
                <text x="36" y="{yv(40)+3:.0f}">40</text><text x="36" y="{yv(60)+3:.0f}">60</text>
              </g>
              <clipPath id="mc-area"><path d="{area}"></path></clipPath>
              <g clip-path="url(#mc-area)" stroke="#CDD2CA" stroke-opacity="0.11" stroke-width="1">{hatch}</g>
              <path d="M{X0} {thr:.1f}H{X1:.0f}" stroke="#FF8A3D" stroke-opacity="0.45" stroke-width="1" stroke-dasharray="4 3"></path>
              <text x="{X1:.0f}" y="{thr-6:.1f}" font-family="Roboto Mono, monospace" font-size="10" fill="#C97438" text-anchor="end">55 A threshold</text>
              <path d="{curve}" stroke="#F8F9F7" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"></path>
              <path d="M{px:.1f} 8V{YB:.0f}" stroke="#F5C400" stroke-width="1" stroke-dasharray="3 3"></path>
              <circle cx="{px:.1f}" cy="{py:.1f}" r="3.5" fill="#F5C400"></circle>
              <text x="{px-8:.1f}" y="{py-8:.1f}" font-family="Roboto Mono, monospace" font-size="10" fill="#F5C400" text-anchor="end">62.4 A &#183; 14:02:09</text>
            </svg>'''

def _log(t, rest, col='#A7AEB4'):
    return ('<div style="display: flex; gap: 10px; padding: 1px 0;">'
            f'<span class="mono" style="font-size: 11px; line-height: 18px; color: #5F686F;">{t}</span>'
            f'<span class="mono" style="font-size: 11px; line-height: 18px; color: {col}; white-space: nowrap;">{rest}</span></div>')

def drawer():
    logs = (_log('13:57:44.102', 'can0 0x1A0 current=31.8A')
      + _log('13:58:02.000', '-- journald jetson-2 unavailable --', '#5F686F')
      + _log('13:58:54.311', '-- source resumed &middot; 52 s gap --', '#5F686F')
      + _log('14:01:58.640', 'can0 0x1A0 current=44.1A')
      + _log('14:02:06.220', 'can0 0x1A0 current=57.9A')
      + _log('14:02:09.008', 'can0 0x1A0 current=62.4A over=55.0A', '#F8F9F7')
      + '<div style="display: flex; gap: 10px; padding: 3px 0 3px 9px; margin: 3px 0; background: #1E2226; border-left: 2px solid #FF5765; border-radius: 0 3px 3px 0;">'
        '<span class="mono" style="font-size: 11px; line-height: 18px; color: #8B939B;">14:02:11.884</span>'
        '<span class="mono" style="font-size: 11px; line-height: 18px; color: #FF5765; white-space: nowrap;">can0 0x2C1 stall_active=1 latched=1</span></div>'
      + _log('14:02:11.884', 'intel motor-drive state=fault')
      + _log('14:02:12.010', 'intel drive_output=inhibited')
      + _log('14:02:41.552', 'can0 0x1A0 current=41.2A over=0')
      + _log('14:02:41.552', 'can0 0x2C1 stall_active=1 latched=1')
      + _log('14:05:00.114', 'can0 0x2C1 stall_active=1 latched=1')
      + _log('14:11:58.902', 'can0 0x2C1 stall_active=1 latched=1'))

    def lane_head(title, right, first=False):
        mt = '' if first else ' margin-top: 7px;'
        return (f'<div style="display: flex; align-items: baseline; justify-content: space-between; width: 824px;{mt}">'
                f'<span class="t-caption" style="color: #CBD1D6;">{title}</span>'
                f'<span class="t-datas" style="color: #565E65;">{right}</span></div>')

    return f'''<div style="height: 410px; background: #171A1D; border: 1px solid #22262A; border-radius: 10px; display: flex; flex-direction: column; overflow: hidden;">
        <div style="height: 44px; display: flex; align-items: center; gap: 14px; padding: 0 20px; border-bottom: 1px solid #212528; flex: none;">
          <span class="t-eyebrow">EVIDENCE</span>
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="t-caption" style="color: #F8F9F7;">motor-drive</span><span class="t-datas">0x2C1</span>
          </div>
          <span class="t-datas" style="color: #6D757D;">13:52:04 &ndash; 14:12:04 &middot; aligned on 14:02:11</span>
          <div style="margin-left: auto; display: flex; align-items: center; gap: 16px;">
            <span class="t-caption">ordering reliable &mdash; chrony <span class="mono" style="font-size: 11px; color: #A7AEB4;">&plusmn;0.4 ms</span></span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span class="t-caption" style="color: #A7AEB4;">Collapse</span>
              <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 4.6L6 7.6l3-3" stroke="#8B939B" stroke-width="1.2"></path></svg>
            </div>
          </div>
        </div>

        <div style="flex: 1; display: flex; min-height: 0;">
          <div style="width: 860px; padding: 16px 0 16px 20px; flex: none;">
            {lane_head('motor current', 'can0 0x1A0 &middot; 10 Hz &middot; continuously sampled', True)}
            {current_chart()}
            {lane_head('drive stall state', 'can0 0x2C1 &middot; reported state &middot; stepped')}
            <svg width="860" height="52" viewBox="0 0 860 52" fill="none" style="display: block;">
              <path d="M46 40H436" stroke="#7A828A" stroke-width="2"></path>
              <path d="M436 40C439 40 439 16 442 16H824" stroke="#FF5765" stroke-width="2" stroke-linejoin="round"></path>
              <text x="48" y="35" font-family="Roboto Mono, monospace" font-size="10" fill="#8B939B">inactive</text>
              <text x="450" y="11" font-family="Roboto Mono, monospace" font-size="10" fill="#FF5765">active &#183; latched</text>
            </svg>
            {lane_head('source coverage', '3 sources')}
            <svg width="860" height="26" viewBox="0 0 860 26" fill="none" style="display: block;">
              <rect x="46" y="4" width="778" height="6" rx="3" fill="#252A2F"></rect>
              <rect x="279" y="3.5" width="27" height="7" rx="3" fill="#16181B" stroke="#4A525A" stroke-width="1" stroke-dasharray="3 2"></rect>
              <text x="312" y="24" font-family="Roboto Mono, monospace" font-size="10" fill="#8B939B">journald jetson-2 &#183; 52 s gap</text>
            </svg>
            {lane_head('can0 events', '2 in window')}
            <svg width="860" height="36" viewBox="0 0 860 36" fill="none" style="display: block;">
              <path d="M46 6h778" stroke="#212528" stroke-width="1"></path>
              <path d="M442 2v9M461 2v9" stroke="#6D757D" stroke-width="1"></path>
              <circle cx="442" cy="6" r="2.6" fill="#FF5765"></circle>
              <circle cx="461" cy="6" r="2.6" fill="#6D757D"></circle>
              <text x="472" y="21" font-family="Roboto Mono, monospace" font-size="10" fill="#A7AEB4">14:02:11 &#183; 0x2C1 stall_active</text>
              <text x="472" y="33" font-family="Roboto Mono, monospace" font-size="10" fill="#8B939B">14:02:41 &#183; 0x1A0 41.2 A below threshold</text>
            </svg>
            <svg width="860" height="16" viewBox="0 0 860 16" fill="none" style="display: block; margin-top: 6px;">
              <g font-family="Roboto Mono, monospace" font-size="10" fill="#6D757D">
                <text x="46" y="11">13:52</text><text x="240" y="11">13:57</text><text x="435" y="11">14:02</text>
                <text x="630" y="11">14:07</text><text x="824" y="11" text-anchor="end">now</text>
              </g>
            </svg>
          </div>

          <div style="width: 1px; background: #212528; flex: none;"></div>

          <div style="flex: 1; padding: 16px 20px; min-width: 0;">
            <div style="display: flex; align-items: baseline; justify-content: space-between;">
              <span class="t-eyebrow">RAW</span>
              <span class="t-datas" style="color: #565E65;">3 sources merged on chrony time</span>
            </div>
            <div style="margin-top: 8px;">{logs}</div>
            <div style="margin-top: 10px;"><span class="t-datas" style="color: #565E65;">ordering across the 52 s gap is not asserted</span></div>
          </div>
        </div>
      </div>'''

# ---------------------------------------------------------------- change review
OK_G = '<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="margin-top: 3px; flex: none;"><circle cx="7.5" cy="7.5" r="6" stroke="#5F686F" stroke-width="1.3"></circle><path d="M4.8 7.6l2 2 3.5-3.9" stroke="#5F686F" stroke-width="1.3"></path></svg>'
UNK_G = '<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="margin-top: 3px; flex: none;"><circle cx="7.5" cy="7.5" r="6" stroke="#4A525A" stroke-width="1.3" stroke-dasharray="2.8 2.4"></circle><path d="M6 6.1c0-1.6 3-1.6 3 0 0 1.1-1.5 1.1-1.5 2.2" stroke="#8B939B" stroke-width="1.2"></path><circle cx="7.5" cy="10.6" r="0.7" fill="#8B939B"></circle></svg>'
DONE_G = '<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex: none;"><circle cx="7.5" cy="7.5" r="6" stroke="#5F686F" stroke-width="1.3"></circle><path d="M4.8 7.6l2 2 3.5-3.9" stroke="#5F686F" stroke-width="1.3"></path></svg>'
WAIT_G = '<svg width="15" height="15" viewBox="0 0 15 15" fill="none" style="flex: none;"><circle cx="7.5" cy="7.5" r="6" stroke="#F5C400" stroke-width="1.3" stroke-dasharray="2.4 3.2"></circle><path d="M7.5 4.4v3.3l2.1 1.3" stroke="#F5C400" stroke-width="1.3"></path></svg>'

def precond(glyph, name, evidence, right, last=False):
    b = '' if last else ' border-bottom: 1px solid #212528;'
    return f'''<div style="display: flex; align-items: flex-start; gap: 12px; padding: 11px 0;{b}">
              {glyph}
              <div style="width: 244px; flex: none;"><span class="t-body" style="color: #F8F9F7;">{name}</span></div>
              <div style="flex: 1; min-width: 0;"><span class="t-caption">{evidence}</span></div>
              <div style="width: 210px; flex: none; text-align: right;"><span class="t-datas" style="color: #6D757D;">{right}</span></div>
            </div>'''

def life(glyph, name, value, meta, current=False):
    box = ('border: 1px solid #F5C400; background: rgba(245,196,0,0.07); border-radius: 6px; padding: 11px 13px;'
           if current else 'border: 1px solid transparent; padding: 11px 13px;')
    return f'''<div style="display: flex; align-items: center; gap: 12px; {box}">
              {glyph}
              <div style="width: 232px; flex: none;"><span class="t-body" style="color: #F8F9F7;">{name}</span></div>
              <div style="flex: 1; min-width: 0;"><span class="t-caption">{value}</span></div>
              <div style="width: 240px; flex: none; text-align: right;"><span class="t-data">{meta}</span></div>
            </div>'''

AUDIT = [('request id', 'chg-4471'), ('requester', 'j.mispelblom'), ('role', 'platform.recovery'),
         ('client', 'web &middot; 10.42.0.14'), ('scope', 'motor-drive 0x2C1'), ('starting state', 'stall_active=1'),
         ('requested', '14:07:03.412'), ('acknowledged', '14:07:03.980')]

def change_body():
    audit = ''.join(f'<div style="display: flex; justify-content: space-between; padding: 3px 0;">'
                    f'<span class="t-caption">{k}</span><span class="t-datas" style="color: #A7AEB4;">{v}</span></div>'
                    for k, v in AUDIT)
    audit += ('<div style="display: flex; justify-content: space-between; padding: 3px 0;">'
              '<span class="t-caption">observed result</span><span class="t-datas" style="color: #F5C400;">pending</span></div>')
    return f'''<div style="display: flex; gap: 16px; height: 692px;">

        <div class="plane" style="width: 992px; height: 692px; padding: 24px 26px; display: flex; flex-direction: column;">
          <div style="display: flex; align-items: baseline; justify-content: space-between;">
            <span class="t-title">Deactivate Drive Stall</span>
            <span class="t-datas" style="color: #6D757D;">motor-drive &middot; 0x2C1 &middot; EXR-04</span>
          </div>

          <div class="rule" style="margin: 16px 0;"></div>

          <div style="display: flex; gap: 26px;">
            <div style="width: 546px; flex: none;">
              <span class="t-eyebrow">SCOPE</span>
              <div style="display: flex; gap: 24px; margin-top: 12px;">
                <div style="width: 150px;"><div class="t-caption">platform</div><div class="t-data" style="color: #F8F9F7; margin-top: 2px;">EXR-04</div></div>
                <div style="width: 170px;"><div class="t-caption">object</div><div class="t-data" style="color: #F8F9F7; margin-top: 2px;">motor-drive</div><div class="t-datas" style="margin-top: 1px; color: #6D757D;">0x2C1 &middot; via can0</div></div>
                <div style="flex: 1;"><div class="t-caption">power domain</div><div class="t-data" style="color: #F8F9F7; margin-top: 2px;">not switched</div><div class="t-datas" style="margin-top: 1px; color: #6D757D;">no gpio channel changes</div></div>
              </div>
            </div>
            <div style="width: 1px; background: #212528;"></div>
            <div style="flex: 1; min-width: 0;">
              <span class="t-eyebrow">EXPECTED RESULT</span>
              <div style="margin-top: 12px;"><span class="t-body">Drive Stall becomes inactive. Drive output is <span style="color: #F8F9F7;">not</span> enabled by this action; a separate enable step is required and is not part of this request.</span></div>
            </div>
          </div>

          <div class="rule" style="margin: 16px 0;"></div>

          <div style="display: flex; align-items: baseline; justify-content: space-between;">
            <span class="t-eyebrow">PRECONDITIONS</span>
            <span class="t-datas" style="color: #565E65;">3 satisfied &middot; 1 not established</span>
          </div>
          <div style="margin-top: 4px;">
{precond(OK_G, 'Overload cleared', 'Observed 41.2 A, below the 55 A threshold, for 5 min 23 s.', 'can0 0x1A0 &middot; since 14:02:41')}
{precond(OK_G, 'Controller reachable', 'The motor-drive controller answered on the current connection.', 'can0 0x2C1 &middot; 0.8 s ago')}
{precond(OK_G, 'Authority', 'Role permits recovery actions on this platform.', 'platform.recovery')}
{precond(UNK_G, 'Remote deactivation permitted', 'Not established for this platform. A local action at the robot may still be required.', 'unknown &middot; see platform owner', last=True)}
          </div>

          <div class="rule" style="margin: 16px 0;"></div>

          <div style="display: flex; align-items: baseline; justify-content: space-between;">
            <span class="t-eyebrow">LIFECYCLE</span>
            <span class="t-datas" style="color: #565E65;">request chg-4471</span>
          </div>
          <div style="margin-top: 6px; margin-left: -13px; margin-right: -13px; display: flex; flex-direction: column; gap: 2px;">
{life(DONE_G, 'Requested', 'Sent to the motor-drive controller over can0.', '14:07:03.412')}
{life(DONE_G, 'Acknowledged', 'The controller accepted the request. This is not a result.', '14:07:03.980')}
{life(WAIT_G, 'Observed result', 'Waiting for an authoritative <span class="mono" style="font-size: 11px; color: #A7AEB4;">stall_active=0</span>.', '12 s elapsed &middot; timeout 60 s', True)}
          </div>

          <div style="margin-top: auto; padding-top: 16px;">
            <span class="t-caption">Success is not reported until the controller reports the state. Rollback does not apply &mdash; Drive Stall is reactivated by motor-drive protection, not by this interface.</span>
          </div>
        </div>

        <div class="plane" style="width: 320px; height: 692px; padding: 20px; display: flex; flex-direction: column;">
          <div><span class="t-eyebrow">OBJECT</span></div>
          <div style="margin-top: 8px; display: flex; align-items: baseline; justify-content: space-between;">
            <span class="t-object">motor-drive</span><span class="t-datas">0x2C1</span>
          </div>
          <div style="margin-top: 4px; display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 7px;">{WARN_GLYPH}<span class="t-caption" style="color: #FF5765;">Fault &middot; stall latched</span></div>
            <span class="t-datas" style="color: #6D757D;">since 14:02:11</span>
          </div>

          <div class="rule" style="margin: 18px 0 12px;"></div>
          <div><span class="t-eyebrow">AUDIT RECORD</span></div>
          <div style="margin-top: 10px;">{audit}</div>

          <div style="margin-top: auto;"></div>
          <div class="rule" style="margin: 18px 0 12px;"></div>
          <div><span class="t-eyebrow">NOT A SAFETY FUNCTION</span></div>
          <div style="margin-top: 8px;"><span class="t-caption" style="color: #A7AEB4;">Safety Stop is unchanged and remains <span style="color: #CBD1D6;">Ready</span>. Clearing Drive Stall does not release, reset or restart any safety function, and does not command motion.</span></div>

          <div style="margin-top: 14px;"><span class="t-datas" style="color: #565E65;">the audit record is written before the result is known</span></div>
        </div>
      </div>'''
