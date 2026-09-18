"""Generate the theme-aware SVG cards and stack panel for the profile README.

Edit PROJECTS or STACK below, then run:

    python3 scripts/build-cards.py

Each card is written in a dark and a light variant to assets/. When you change
a card, rename its slug (for example trading-v2 -> trading-v3) and update the
README, otherwise GitHub keeps serving the cached image.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark": dict(bg0="#0B0F14", bg1="#141C25", border="#1F2A36", dots="#18222D",
                 title="#F0F6FC", text="#8B98A5", accent="#3FB950",
                 chip="#16202B", chipborder="#223040", chiptext="#C9D1D9", faint="#2A3947"),
    "light": dict(bg0="#FFFFFF", bg1="#F6F8FA", border="#D0D7DE", dots="#E7EBEF",
                  title="#1F2328", text="#57606A", accent="#1A7F37",
                  chip="#F0F3F6", chipborder="#D8DEE4", chiptext="#24292F", faint="#C9D1D9"),
}

SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
CHAR = 6.6  # width of one 11px monospace glyph

PROJECTS = [
    dict(slug="mototrack", label="REALTIME TELEMATICS", title="MotoTrack", glyph="signal",
         lines=["Fleet tracking from device to map. GSM and MQTT",
                "trackers feed a TCP gateway; telemetry, rules and",
                "alert workers talk over NATS; maps update live."],
         chips=["NATS", "MQTT", "TimescaleDB", "Socket.IO", "Next.js", "Expo"]),
    dict(slug="zischool", label="MULTI-TENANT PLATFORM", title="ZiSchool OS", glyph="tenants",
         lines=["An operating system for schools: one kernel for",
                "identity, RBAC and tenancy, apps as guests,",
                "events on NATS, metrics in Prometheus and Grafana."],
         chips=["Fastify", "NATS", "PostgreSQL", "Prometheus", "Grafana"]),
    dict(slug="trading-v2", label="TRADING & QUANT", title="Trading systems", glyph="candles",
         lines=["Trading bots in Go and Python on exchange APIs:",
                "market data, indicators and execution, with deep",
                "and reinforcement learning for signal research."],
         chips=["Go", "Python", "Reinforcement learning", "Bybit", "Binance"]),
    dict(slug="ai", label="AI ENGINEERING", title="LLM systems", glyph="graph",
         lines=["LLM features built into products: RAG pipelines,",
                "agent workflows with LangGraph, tracing and",
                "evaluation in Langfuse, Claude and OpenAI models."],
         chips=["LangGraph", "LangChain", "RAG", "Vercel AI SDK", "Langfuse"]),
    dict(slug="bicollect", label="EVENT-DRIVEN · IN DEVELOPMENT", title="BiCollect", glyph="bus",
         lines=["A business operating platform: POS, inventory,",
                "finance, banking and CRM as services on NATS",
                "JetStream, sharing one kernel and one identity."],
         chips=["NATS JetStream", "Fastify", "PostgreSQL", "BullMQ", "MinIO"]),
    dict(slug="roadside-v2", label="REALTIME DISPATCH", title="Roadside Assistant", glyph="route",
         lines=["Dispatch platform with live responder",
                "positions over WebSockets, a mobile app for",
                "responders and a console for operators."],
         chips=["Fastify", "WebSockets", "React Native", "Next.js"]),
]

STACK = [
    ("Product", ["TypeScript", "Next.js / React", "Vue 3 / Nuxt", "React Native / Expo", "Tailwind CSS"]),
    ("Backend & data", ["Go", "Node.js / Fastify", "Python", "PostgreSQL / TimescaleDB", "Redis / BullMQ"]),
    ("Realtime & events", ["NATS JetStream", "WebSockets / Socket.IO", "MQTT", "TCP device gateways", "ESP32 / GSM firmware"]),
    ("AI & LLMs", ["LLMs: Claude, OpenAI", "LangChain / LangGraph", "RAG pipelines", "Vercel AI SDK", "Langfuse"]),
    ("ML for trading", ["pandas / NumPy", "scikit-learn", "Deep learning", "Reinforcement learning", "Backtesting"]),
    ("DevOps & Linux", ["Linux servers", "Bash scripting", "Docker / Compose", "Nginx / TLS", "GitHub Actions CI/CD", "Prometheus / Grafana"]),
]


def frame(w, h, c, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c['bg0']}"/><stop offset="1" stop-color="{c['bg1']}"/>
    </linearGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1.1" fill="{c['dots']}"/>
    </pattern>
  </defs>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="14" fill="url(#bg)" stroke="{c['border']}"/>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="14" fill="url(#dots)" opacity="0.7"/>
{body}
</svg>
"""


def glyph(kind, c, x, y):
    a, f = c["accent"], c["faint"]
    if kind == "signal":
        return f"""  <g transform="translate({x} {y})" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M0 44 L18 30 L32 36 L46 14 L60 20 L72 2" stroke="{a}" stroke-width="2"/>
    <circle cx="18" cy="30" r="3" fill="{c['bg0']}" stroke="{a}" stroke-width="1.6"/>
    <circle cx="46" cy="14" r="3" fill="{c['bg0']}" stroke="{a}" stroke-width="1.6"/>
    <circle cx="72" cy="2" r="4" fill="{a}"/>
  </g>"""
    if kind == "tenants":
        cells = []
        for r in range(3):
            for col in range(4):
                fill = a if (r, col) == (1, 2) else f
                cells.append(f'<rect x="{col * 19}" y="{r * 16}" width="14" height="11" rx="2.5" fill="{fill}"/>')
        return f'  <g transform="translate({x} {y})">{"".join(cells)}</g>'
    if kind == "route":
        return f"""  <g transform="translate({x} {y})" fill="none" stroke-linecap="round">
    <path d="M2 44 C 20 44, 16 18, 38 22 S 58 6, 70 8" stroke="{f}" stroke-width="2" stroke-dasharray="3 5"/>
    <circle cx="2" cy="44" r="3.5" fill="{f}"/>
    <path d="M70 -4 a8 8 0 0 1 8 8 c0 6 -8 14 -8 14 s-8 -8 -8 -14 a8 8 0 0 1 8 -8 z" fill="{a}"/>
    <circle cx="70" cy="4" r="2.6" fill="{c['bg0']}"/>
  </g>"""
    if kind == "candles":
        bars = [(0, 20, 34, 12, 40, False), (15, 12, 26, 6, 32, True), (30, 16, 30, 10, 38, False),
                (45, 6, 22, 0, 28, True), (60, 0, 14, -6, 20, True)]
        out = []
        for bx, top, bot, wt, wb, up in bars:
            col = a if up else f
            out.append(f'<line x1="{bx + 4}" y1="{wt}" x2="{bx + 4}" y2="{wb}" stroke="{col}" stroke-width="1.5"/>'
                       f'<rect x="{bx}" y="{top}" width="8" height="{bot - top}" rx="1.5" fill="{col}"/>')
        return f'  <g transform="translate({x} {y + 6})">{"".join(out)}</g>'
    if kind == "graph":
        nodes = [(4, 22), (30, 6), (30, 38), (58, 22), (76, 4)]
        edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
        lines = "".join(f'<line x1="{nodes[i][0]}" y1="{nodes[i][1]}" x2="{nodes[j][0]}" y2="{nodes[j][1]}" stroke="{f}" stroke-width="1.6"/>'
                        for i, j in edges)
        dots = "".join(f'<circle cx="{nx}" cy="{ny}" r="{5 if k == 3 else 4}" fill="{a if k in (3, 4) else c["bg0"]}" stroke="{a if k in (3, 4) else f}" stroke-width="1.6"/>'
                       for k, (nx, ny) in enumerate(nodes))
        return f'  <g transform="translate({x} {y + 4})">{lines}{dots}</g>'
    if kind == "bus":
        taps = "".join(f'<line x1="{tx}" y1="{8 if k % 2 == 0 else 26}" x2="{tx}" y2="{18 if k % 2 == 0 else 36}" stroke="{f}" stroke-width="1.6"/>'
                       f'<rect x="{tx - 6}" y="{0 if k % 2 == 0 else 36}" width="12" height="9" rx="2" fill="{a if k == 2 else f}"/>'
                       for k, tx in enumerate((8, 26, 44, 62)))
        return (f'  <g transform="translate({x} {y + 2})"><rect x="0" y="19" width="76" height="6" rx="3" fill="{a}" opacity="0.85"/>'
                f'{taps}</g>')
    return ""


def chips(items, c, x0, y0, maxw):
    out, x, y = [], x0, y0
    for item in items:
        w = len(item) * CHAR + 14
        if x + w > x0 + maxw:
            x, y = x0, y + 30
        out.append(f'  <rect x="{x}" y="{y}" width="{w:.1f}" height="22" rx="11" fill="{c["chip"]}" stroke="{c["chipborder"]}"/>'
                   f'<text x="{x + w / 2:.1f}" y="{y + 15}" text-anchor="middle" font-family="{MONO}" '
                   f'font-size="11" fill="{c["chiptext"]}">{escape(item)}</text>')
        x += w + 6
    return "\n".join(out)


def project_card(p, c):
    w, h, pad = 440, 226, 28
    body = [
        f'  <rect x="{pad}" y="30" width="3" height="12" rx="1.5" fill="{c["accent"]}"/>',
        f'  <text x="{pad + 12}" y="41" font-family="{MONO}" font-size="11" letter-spacing="1.4" fill="{c["accent"]}">{escape(p["label"])}</text>',
        f'  <text x="{pad}" y="80" font-family="{SANS}" font-size="24" font-weight="700" letter-spacing="-0.5" fill="{c["title"]}">{escape(p["title"])}</text>',
        glyph(p["glyph"], c, w - pad - 80, 26),
    ]
    for i, line in enumerate(p["lines"]):
        body.append(f'  <text x="{pad}" y="{112 + i * 21}" font-family="{SANS}" font-size="14" fill="{c["text"]}">{escape(line)}</text>')
    body.append(chips(p["chips"], c, pad, 180, w - 2 * pad))
    return frame(w, h, c, "\n".join(body))


def stack_card(c):
    w, rowh, pad = 888, 222, 36
    h = rowh * 2 + 44
    colw = (w - 2 * pad) / 3
    body = []
    for i, (head, items) in enumerate(STACK):
        x, base = pad + (i % 3) * colw, (i // 3) * rowh
        body.append(f'  <text x="{x}" y="{base + 50}" font-family="{MONO}" font-size="11" letter-spacing="1.4" fill="{c["accent"]}">{escape(head.upper())}</text>')
        body.append(f'  <rect x="{x}" y="{base + 62}" width="{colw - 28:.0f}" height="1" fill="{c["border"]}"/>')
        for j, item in enumerate(items):
            y = base + 94 + j * 28
            body.append(f'  <circle cx="{x + 4}" cy="{y - 5}" r="2.5" fill="{c["accent"] if j == 0 else c["faint"]}"/>'
                        f'<text x="{x + 16}" y="{y}" font-family="{SANS}" font-size="15" fill="{c["title"]}">{escape(item)}</text>')
    return frame(w, h, c, "\n".join(body))


for theme, c in THEMES.items():
    for p in PROJECTS:
        (OUT / f"card-{p['slug']}-{theme}.svg").write_text(project_card(p, c))
    (OUT / f"stack-v2-{theme}.svg").write_text(stack_card(c))
print("ok")
