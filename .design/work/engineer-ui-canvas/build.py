# -*- coding: utf-8 -*-
import lib
from lib import *

def shell(active, scope, content):
    return (header()
      + '\n  <div style="position: relative; display: flex; height: 844px;">\n\n'
      + rail(active)
      + '\n    <div style="flex: 1; padding: 18px; display: flex; flex-direction: column;">\n\n'
      + scope
      + content
      + '\n    </div>\n  </div>\n')

FACT_FAULT = ('<div style="display: flex; align-items: center; gap: 8px;">' + WARN_GLYPH +
  '<span class="t-caption" style="color: #F8F9F7;">1 fault</span>'
  '<span class="t-datas" style="color: #6D757D;">motor-drive</span></div>')

OBJ_CHIP = ('<div style="height: 32px; padding: 0 12px; display: flex; align-items: center; gap: 9px; '
  'border-radius: 6px; border: 1px solid #2A2E33;">'
  '<svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M7.4 2.6L4.4 6l3 3.4" stroke="#8B939B" stroke-width="1.2"></path></svg>'
  '<span class="t-caption">carried from Inspect</span>'
  '<span class="t-datas" style="color: #A7AEB4;">motor-drive 0x2C1</span></div>')

CHG_CHIP = OBJ_CHIP.replace('carried from Inspect', 'carried from Diagnose')

LENS_WRAP = '<div style="width: 1px; height: 20px; background: #212528;"></div>\n        ' + lens_chips()

# ------------------------------------------------------------------ 1. Inspect / healthy
body = ('      <div style="display: flex; gap: 16px; height: 498px;">\n        '
        + map_plane() + '\n        ' + attention_healthy() + '\n      </div>\n\n'
        '      <div style="height: 14px;"></div>\n\n      '
        + bottom_band('compute') + '\n\n      <div style="height: 14px;"></div>\n\n      '
        + evidence_strip('window 20 min &middot; 13:48&ndash;14:08 &middot; can0 &middot; /proc/stat &middot; journald &times;3',
                         'gas adc channel map unconfirmed', note_glyph='unknown') + '\n')
open('Main.dc.html','w').write(page(shell('inspect', scopebar('Inspect', LENS_WRAP), body)))

# ------------------------------------------------------------------ 2. Inspect / selected fault
body = ('      <div style="display: flex; gap: 16px; height: 498px;">\n        '
        + map_plane(selected=True, fault=True) + '\n        ' + inspector(498, True) + '\n      </div>\n\n'
        '      <div style="height: 14px;"></div>\n\n      '
        + bottom_band('can') + '\n\n      <div style="height: 14px;"></div>\n\n      '
        + evidence_strip('window 20 min &middot; 13:52&ndash;14:12 &middot; aligned on 14:02:11 &middot; can0 &middot; journald &times;3',
                         'ordering reliable &mdash; chrony &plusmn;0.4 ms') + '\n')
open('Degraded.dc.html','w').write(page(shell('inspect', scopebar('Inspect', LENS_WRAP, FACT_FAULT), body)))

# ------------------------------------------------------------------ 3. Diagnose / evidence expanded
body = ('      <div style="display: flex; gap: 16px; height: 326px;">\n        '
        + map_plane_cropped() + '\n        ' + inspector(326, False) + '\n      </div>\n\n'
        '      <div style="height: 14px;"></div>\n\n      ' + drawer() + '\n')
open('Evidence.dc.html','w').write(page(shell('diagnose', scopebar('Diagnose', '<div style="width: 1px; height: 20px; background: #212528;"></div>\n        ' + OBJ_CHIP), body)))

# ------------------------------------------------------------------ 4. Change / review
body = ('      ' + change_body() + '\n\n      <div style="height: 14px;"></div>\n\n      '
        + evidence_strip('window 20 min &middot; 13:52&ndash;14:12 &middot; held with request chg-4471',
                         'an unresolved request stays visible in every mode until it is settled') + '\n')
open('Change.dc.html','w').write(page(shell('change', scopebar('Change', '<div style="width: 1px; height: 20px; background: #212528;"></div>\n        ' + CHG_CHIP), body)))

print('built 4 artboards')
