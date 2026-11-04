import math
X0, X1 = 46.0, 824.0
YB, YT = 112.0, 8.0            # value 0 and value 70
def yv(v): return YB - v * (104.0/70.0)
pts_f = [(0.00,29),(0.08,31),(0.16,28),(0.24,33),(0.32,30),(0.40,35),(0.46,44),
         (0.490,56),(0.5075,62.4),(0.525,47),(0.545,18),(0.570,7),(0.64,6),
         (0.72,6.5),(0.80,6.0),(0.90,6.2),(1.00,6.0)]
P = [(X0 + f*(X1-X0), yv(v)) for f, v in pts_f]

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

curve = catmull(P)
area = curve + " L %.2f %.2f L %.2f %.2f Z" % (X1, YB, X0, YB)

# 45 degree hatch, 9px perpendicular pitch -> 12.73px horizontal step
step = 9.0 * math.sqrt(2.0)
lines = []
h = YB - YT
i = int(-h/step) - 1
x = X0 + i*step
while x < X1 + h:
    lines.append('<path d="M %.1f %.1f L %.1f %.1f"></path>' % (x, YB, x + h, YB - h))
    x += step
hatch = "".join(lines)

probe_x = X0 + 0.5075*(X1-X0)
probe_y = yv(62.4)
thr_y = yv(55)

svg = f'''<svg width="860" height="120" viewBox="0 0 860 120" fill="none" style="display: block;">
              <g stroke="#272B2F" stroke-width="1">
                <path d="M{X0} {YB:.0f}H{X1:.0f}"></path>
                <path d="M{X0} {yv(20):.0f}H{X1:.0f}"></path>
                <path d="M{X0} {yv(40):.0f}H{X1:.0f}"></path>
                <path d="M{X0} {yv(60):.0f}H{X1:.0f}"></path>
              </g>
              <g font-family="Roboto Mono, monospace" font-size="10" fill="#8B939B" text-anchor="end">
                <text x="36" y="{YB+3:.0f}">0</text>
                <text x="36" y="{yv(20)+3:.0f}">20</text>
                <text x="36" y="{yv(40)+3:.0f}">40</text>
                <text x="36" y="{yv(60)+3:.0f}">60</text>
              </g>
              <clipPath id="mc-area"><path d="{area}"></path></clipPath>
              <g clip-path="url(#mc-area)" stroke="#CDD2CA" stroke-opacity="0.13" stroke-width="1">{hatch}</g>
              <path d="M{X0} {thr_y:.1f}H{X1:.0f}" stroke="#FF8A3D" stroke-opacity="0.5" stroke-width="1" stroke-dasharray="4 3"></path>
              <text x="{X1:.0f}" y="{thr_y-6:.1f}" font-family="Roboto Mono, monospace" font-size="10" fill="#FF8A3D" text-anchor="end">55 A threshold</text>
              <path d="{curve}" stroke="#F8F9F7" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"></path>
              <path d="M{probe_x:.1f} {YT:.0f}V{YB:.0f}" stroke="#F5C400" stroke-width="1" stroke-dasharray="3 3"></path>
              <circle cx="{probe_x:.1f}" cy="{probe_y:.1f}" r="3.5" fill="#F5C400"></circle>
              <text x="{probe_x-8:.1f}" y="{probe_y-8:.1f}" font-family="Roboto Mono, monospace" font-size="10" fill="#F5C400" text-anchor="end">62.4 A &#183; 14:02:09</text>
            </svg>'''
open('chart_current.svg','w').write(svg)
print('probe_x %.1f' % probe_x, 'len', len(svg))
