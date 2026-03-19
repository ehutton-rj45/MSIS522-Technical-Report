import streamlit as st
from pathlib import Path

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LinkedOut — MSIS 522",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap');

html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

/* Kill default Streamlit padding at top */
.block-container { padding-top: 2rem; padding-bottom: 4rem; }

/* ── Shared card ── */
.card {
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(240,249,255,0.78));
    border: 1px solid rgba(186,230,253,0.8);
    border-radius: 24px;
    box-shadow: 0 14px 40px rgba(8,47,73,0.08);
    padding: 1.75rem;
    height: 100%;
}
.dark-card {
    background: linear-gradient(135deg, rgba(15,23,42,0.97), rgba(8,47,73,0.93));
    border-radius: 24px;
    color: #cbd5e1;
    padding: 1.75rem;
    height: 100%;
}

/* ── Hero ── */
.hero {
    background:
        radial-gradient(circle at top left, rgba(16,185,129,0.10), transparent 28%),
        radial-gradient(circle at top right, rgba(56,189,248,0.14), transparent 32%),
        linear-gradient(180deg, rgba(240,253,255,0.85), rgba(235,245,255,0.6) 50%, rgba(255,255,255,0.7));
    border: 1px solid rgba(186,230,253,0.8);
    border-radius: 30px;
    box-shadow: 0 28px 72px rgba(8,47,73,0.10);
    padding: 3rem;
    margin-bottom: 0.5rem;
}
.hero-pill {
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(186,230,253,0.9);
    border-radius: 999px;
    color: #0e7490;
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.24em;
    padding: 0.6rem 1rem;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}
.hero h1 {
    color: #020617;
    font-size: 4rem;
    font-weight: 900;
    letter-spacing: -0.05em;
    line-height: 0.95;
    margin: 0 0 0.8rem;
}
.hero .owner { color: #64748b; font-size: 1.1rem; font-weight: 600; margin: 0 0 1rem; }
.hero .subtitle { color: #334155; font-size: 1.4rem; line-height: 1.55; margin: 0 0 1rem; }
.hero .summary { color: #475569; font-size: 1.02rem; line-height: 1.9; margin: 0; }

/* ── Badges ── */
.badge-row { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.5rem; }
.chip {
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(186,230,253,0.9);
    border-radius: 999px;
    color: #334155;
    font-size: 0.88rem;
    font-weight: 500;
    padding: 0.5rem 0.95rem;
}

/* ── Link buttons ── */
.btn-row { display: flex; flex-wrap: wrap; gap: 0.7rem; margin-top: 1.4rem; }
.btn-primary {
    background: #020617;
    border-radius: 999px;
    box-shadow: 0 12px 30px rgba(15,23,42,0.18);
    color: white !important;
    font-weight: 700;
    padding: 0.75rem 1.3rem;
    text-decoration: none !important;
    font-size: 0.95rem;
}
.btn-secondary {
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(186,230,253,0.9);
    border-radius: 999px;
    color: #334155 !important;
    font-weight: 600;
    padding: 0.75rem 1.3rem;
    text-decoration: none !important;
    font-size: 0.95rem;
}

/* ── Section header ── */
.section-header { margin: 0.5rem 0 1.2rem; }
.eyebrow {
    color: #0e7490;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.26em;
    text-transform: uppercase;
    margin: 0 0 0.3rem;
}
.section-header h2 {
    color: #020617;
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: -0.04em;
    margin: 0 0 0.6rem;
}
.section-header p { color: #475569; line-height: 1.85; margin: 0; font-size: 1rem; }

/* ── Metric card ── */
.metric-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(240,249,255,0.78));
    border: 1px solid rgba(186,230,253,0.7);
    border-radius: 22px;
    padding: 1.4rem;
    box-shadow: 0 10px 28px rgba(8,47,73,0.06);
}
.metric-label { color: #0e7490; font-size: 0.74rem; font-weight: 700; letter-spacing: 0.24em; text-transform: uppercase; margin: 0; }
.metric-value { color: #020617; font-size: 1.9rem; font-weight: 900; letter-spacing: -0.04em; margin: 0.6rem 0 0; }
.metric-note { color: #64748b; line-height: 1.65; margin: 0.6rem 0 0; font-size: 0.9rem; }

/* ── Problem / solution ── */
.prob-card { background: linear-gradient(180deg,rgba(255,255,255,0.92),rgba(240,249,255,0.78)); border:1px solid rgba(186,230,253,0.8); border-radius:24px; padding:1.75rem; }
.prob-card .eyebrow { color:#10b981; }
.sol-card { background:linear-gradient(135deg,rgba(15,23,42,0.97),rgba(8,47,73,0.93)); border-radius:24px; padding:1.75rem; color:#cbd5e1; }
.sol-card .eyebrow { color:rgba(186,230,253,0.85); }
.sol-card h3 { color:white; font-size:1.45rem; font-weight:900; letter-spacing:-0.03em; margin:0.3rem 0 0.8rem; }
.sol-card p { line-height:1.9; margin:0; }
.mini-row { display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:1.2rem; }
.dark-chip { background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.1); border-radius:999px; color:#f8fafc; font-size:0.88rem; font-weight:500; padding:0.45rem 0.9rem; }
.mini-grid { display:grid; grid-template-columns:1fr 1fr; gap:0.8rem; margin-top:1.2rem; }
.mini-panel { background:rgba(240,249,255,0.5); border:1px solid rgba(186,230,253,0.6); border-radius:14px; padding:0.85rem; }
.mini-label { color:#0e7490; font-size:0.72rem; font-weight:700; letter-spacing:0.22em; text-transform:uppercase; margin:0 0 0.3rem; }
.mini-panel p { color:#334155; margin:0; font-size:0.92rem; line-height:1.6; }

/* ── Team ── */
.team-card {
    background: linear-gradient(180deg,rgba(255,255,255,0.92),rgba(240,249,255,0.78));
    border: 1px solid rgba(186,230,253,0.7);
    border-radius: 22px;
    padding: 1.4rem 1.4rem 1.4rem 1rem;
    display: flex; gap: 1rem; align-items: flex-start;
    height: 100%;
}
.team-avatar {
    background: linear-gradient(135deg,#06b6d4,#38bdf8);
    border-radius: 16px;
    color: white;
    font-size: 1rem;
    font-weight: 700;
    height: 2.8rem;
    min-width: 2.8rem;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.team-name { color:#020617; font-size:1.05rem; font-weight:900; margin:0; }
.team-role { color:#0e7490; font-size:0.88rem; font-weight:700; margin:0.25rem 0 0.5rem; }
.team-focus { color:#475569; font-size:0.9rem; line-height:1.7; margin:0; }

/* ── Feature card ── */
.feature-card {
    background: linear-gradient(180deg,rgba(255,255,255,0.92),rgba(240,249,255,0.78));
    border: 1px solid rgba(186,230,253,0.7);
    border-radius: 22px;
    padding: 1.5rem;
    height: 100%;
}
.feature-icon {
    background: linear-gradient(135deg,#06b6d4,#38bdf8);
    border-radius: 14px;
    color: white;
    display: inline-flex; align-items: center; justify-content: center;
    height: 2.4rem; width: 2.4rem;
    font-size: 1rem;
    margin-bottom: 0.8rem;
}
.feature-card h3 { color:#020617; font-size:1.15rem; font-weight:900; letter-spacing:-0.02em; margin:0 0 0.5rem; }
.feature-card p { color:#475569; font-size:0.93rem; line-height:1.85; margin:0 0 0.9rem; }
.check-list li { color:#334155; font-size:0.9rem; line-height:1.75; }

/* ── Stack card ── */
.stack-card {
    background: rgba(240,249,255,0.55);
    border: 1px solid rgba(186,230,253,0.6);
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 0.8rem;
}
.stack-cat { color:#0e7490; font-size:0.82rem; font-weight:700; margin:0 0 0.6rem; display:flex; align-items:center; gap:0.4rem; }
.stack-note { color:#475569; font-size:0.88rem; line-height:1.75; margin:0.75rem 0 0; }

/* ── Architecture steps ── */
.arch-card {
    background: linear-gradient(180deg,rgba(255,255,255,0.92),rgba(240,249,255,0.78));
    border: 1px solid rgba(186,230,253,0.7);
    border-radius: 18px;
    padding: 1.2rem 1.2rem 1.2rem 1rem;
    display: flex; gap: 0.9rem; align-items: flex-start;
    margin-bottom: 0.75rem;
}
.step-badge {
    background: white;
    border: 1px solid rgba(186,230,253,0.8);
    border-radius: 12px;
    color: #020617;
    font-weight: 700;
    font-size: 0.95rem;
    height: 2rem; min-width: 2rem;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.arch-card h4 { color:#020617; font-size:1rem; font-weight:900; margin:0 0 0.35rem; }
.arch-card p { color:#475569; font-size:0.9rem; line-height:1.75; margin:0; }

/* ── Roadmap ── */
.roadmap-card {
    background: linear-gradient(180deg,rgba(255,255,255,0.92),rgba(240,249,255,0.78));
    border: 1px solid rgba(186,230,253,0.7);
    border-radius: 20px;
    padding: 1.4rem;
}
.roadmap-phase { color:#0e7490; font-size:0.74rem; font-weight:700; letter-spacing:0.24em; text-transform:uppercase; margin:0 0 0.9rem; }
.roadmap-card ul { margin:0; padding-left:1.2rem; }
.roadmap-card li { color:#334155; font-size:0.92rem; line-height:1.8; }

/* ── Risk card ── */
.risk-card {
    background: linear-gradient(180deg,rgba(255,255,255,0.92),rgba(240,249,255,0.78));
    border: 1px solid rgba(186,230,253,0.7);
    border-radius: 18px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.75rem;
}
.risk-title { color:#be123c; font-size:1rem; font-weight:900; margin:0 0 0.4rem; }
.risk-mit { color:#475569; font-size:0.9rem; line-height:1.75; margin:0; }

/* ── Closing ── */
.closing {
    background: linear-gradient(135deg,rgba(15,23,42,0.97),rgba(8,47,73,0.93));
    border-radius: 28px;
    color: #cbd5e1;
    padding: 2.25rem;
    margin-top: 0.5rem;
}
.closing h2 { color: white; font-size: 2rem; font-weight: 900; letter-spacing: -0.04em; margin: 0.5rem 0 0.8rem; }
.closing p { color: #94a3b8; line-height: 1.9; margin: 0; }
.closing-mini {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 18px;
    padding: 1.2rem;
    height: 100%;
}
.closing-mini h3 { color: white; font-size: 1rem; font-weight: 900; margin: 0.5rem 0 0.4rem; }
.closing-mini p { color: #94a3b8; font-size: 0.9rem; line-height: 1.7; margin: 0; }

/* ── Gallery: force uniform height ── */
.gallery-img { border-radius: 16px; overflow: hidden; }
.gallery-caption { color: #020617; font-size: 1rem; font-weight: 700; margin: 0.7rem 0 0.25rem; }
.gallery-sub { color: #475569; font-size: 0.9rem; line-height: 1.75; margin: 0; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Helper: inject raw HTML block
# ─────────────────────────────────────────────────────────────────────────────
def html(content: str):
    st.markdown(content, unsafe_allow_html=True)


def spacer(h: str = "1.5rem"):
    html(f'<div style="height:{h}"></div>')


# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────
html("""
<div class="hero">
  <div class="hero-pill">✦ MSIS 522 — University of Washington</div>
  <h1>LinkedOut</h1>
  <p class="owner">Hardik Sharma, Aria Wang, Ethan Hutton &amp; Jingying Deng</p>
  <p class="subtitle">An AI-powered interactive portfolio that lets recruiters and hiring teams talk live to a digital avatar of the candidate — anytime, without scheduling.</p>
  <p class="summary">LinkedOut reimagines the job-search portfolio as a two-way conversation. Instead of a static resume page, hiring managers and recruiters visit a personal website and instantly connect with a real-time AI video avatar of the candidate. The avatar is powered by the LiveAvatar API and orchestrated by an ElevenLabs Conversational Agent, streaming audio and video through a LiveKit room so the interaction feels like a live video call. A lightweight Node/Express backend handles session lifecycle securely, while a clean HTML/CSS/JS frontend keeps the experience fast and frictionless. The core insight is that recruiters make decisions on personality and communication as much as credentials — LinkedOut closes that gap by letting candidates "be present" 24/7 without engineering a live meeting.</p>
  <div class="badge-row">
    <span class="chip">Node.js / Express</span>
    <span class="chip">LiveAvatar API</span>
    <span class="chip">LiveKit WebRTC</span>
    <span class="chip">ElevenLabs Agent</span>
    <span class="chip">HTML / CSS / JS</span>
    <span class="chip">Conversational AI</span>
  </div>
  <div class="btn-row">
    <a class="btn-primary" href="https://github.com/hdksrma/theportfolioproject" target="_blank">🔗 GitHub Repo</a>
    <a class="btn-secondary" href="https://github.com/ehutton-rj45/MSIS522-Technical-Report/blob/main/public/project-assets/Technical%20report.pdf" target="_blank">📄 Technical Report</a>
    <a class="btn-secondary" href="https://github.com/ehutton-rj45/MSIS522-Technical-Report/blob/main/public/project-assets/MSIS%20522%20Project_LinkedOut.pptx?raw=true" target="_blank">📊 Slide Deck</a>
  </div>
</div>
""")

spacer("0.5rem")

# ─────────────────────────────────────────────────────────────────────────────
# METRICS
# ─────────────────────────────────────────────────────────────────────────────
cols = st.columns(4)
metrics = [
    ("Core User", "Recruiters &amp; Hiring Managers", "Anyone who reviews candidates asynchronously"),
    ("Availability", "24 / 7", "Avatar is always on — no scheduling required"),
    ("Response Latency", "Real-time", "Streamed via LiveKit WebRTC, sub-second turns"),
    ("Status", "Live Prototype", "Deployed and functional end-to-end"),
]
for col, (label, value, note) in zip(cols, metrics):
    with col:
        html(f"""
        <div class="metric-card">
          <p class="metric-label">{label}</p>
          <p class="metric-value">{value}</p>
          <p class="metric-note">{note}</p>
        </div>""")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# PROBLEM / SOLUTION
# ─────────────────────────────────────────────────────────────────────────────
col_prob, col_sol = st.columns(2)

with col_prob:
    html("""
    <div class="prob-card" style="height:100%">
      <p class="eyebrow">Problem</p>
      <h3 style="color:#020617;font-size:1.45rem;font-weight:900;letter-spacing:-0.03em;margin:0.3rem 0 0.9rem">What problem are we solving?</h3>
      <p style="color:#475569;line-height:1.9;margin:0">
        Job seekers spend enormous effort crafting static resumes and portfolio sites — yet recruiters still cannot get a sense of how someone communicates, thinks, or presents themselves without scheduling a screening call. Scheduling friction, time-zone gaps, and high candidate volume mean many strong candidates are screened out before a human ever speaks to them. Traditional async video recordings feel stiff and one-directional. There is no way for a recruiter to ask a follow-up question, probe for depth, or test how a candidate handles a novel prompt.
      </p>
      <div class="mini-grid" style="margin-top:1.4rem">
        <div class="mini-panel">
          <p class="mini-label">Audience</p>
          <p>Recruiters, hiring managers, and technical interviewers</p>
        </div>
        <div class="mini-panel">
          <p class="mini-label">Impact Goal</p>
          <p>Reduce screening friction, help communicators stand out</p>
        </div>
        <div class="mini-panel">
          <p class="mini-label">Status</p>
          <p>Live Prototype — deployed end-to-end</p>
        </div>
      </div>
    </div>""")

with col_sol:
    html("""
    <div class="sol-card" style="height:100%">
      <p class="eyebrow" style="color:rgba(186,230,253,0.85)">Solution</p>
      <h3>What are we building?</h3>
      <p>
        LinkedOut replaces the static portfolio with a live, conversational AI avatar that represents the candidate on demand. A recruiter visits the site, clicks "Start Session," and is immediately connected to a streaming video avatar trained on the candidate's background, projects, and communication style. The avatar handles push-to-talk or open-mic input, responds via ElevenLabs voice synthesis, and transcribes the conversation in real time. The candidate's actual identity — their experience, projects, and technical depth — is encoded into the avatar's context so every answer is authentic.
      </p>
      <div class="mini-row">
        <span class="dark-chip">Real-time WebRTC streaming</span>
        <span class="dark-chip">Conversational AI agent</span>
        <span class="dark-chip">Push-to-Talk &amp; Open-Mic</span>
        <span class="dark-chip">Live transcript &amp; event log</span>
        <span class="dark-chip">Secure session management</span>
      </div>
    </div>""")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# TEAM
# ─────────────────────────────────────────────────────────────────────────────
html("""
<div class="section-header">
  <p class="eyebrow">Team</p>
  <h2>Who built LinkedOut</h2>
  <p>Four students from the UW MSIS program.</p>
</div>""")

team = [
    ("Hardik Sharma",
     "Built the full Node.js/Express backend, integrated the LiveAvatar API, wired up the LiveKit WebRTC room to carry video, audio, and bidirectional data events, tuned the ElevenLabs agent persona, crafted the context prompts and conversational flow."),
    ("Aria Wang",
     "Built the demo day presentation. Synthesized the full project into a compelling narrative for stakeholders, designed the slide deck structure and visual story, and prepared the live demonstration flow for the class presentation."),
    ("Ethan Hutton",
     "Built the Technical Report based off the professor's template. Documented the project in a structured academic format aligned with MSIS 522 course requirements."),
    ("Jingying Deng",
     "Led the live demonstration during the demo day presentation, showcased the avatar's real-time conversational capabilities to the class, and fielded questions from the audience."),
]

t_cols = st.columns(2)
for i, (name, focus) in enumerate(team):
    initials = "".join(p[0] for p in name.split())[:2].upper()
    with t_cols[i % 2]:
        html(f"""
        <div class="team-card">
          <div class="team-avatar">{initials}</div>
          <div>
            <p class="team-name">{name}</p>
            <p class="team-focus">{focus}</p>
          </div>
        </div>""")
        spacer("0.6rem")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# GALLERY
# ─────────────────────────────────────────────────────────────────────────────
html("""
<div class="section-header">
  <p class="eyebrow">Gallery</p>
  <h2>See LinkedOut in action</h2>
  <p>Screenshots of the live portfolio and avatar interface, plus the system architecture diagram.</p>
</div>""")

gallery = [
    ("assets/screenshot_home.jpg",      "Portfolio Home",               "The landing page — dark-mode design with impact stats, experience timeline, and a 'Talk to my avatar' CTA."),
    ("assets/screenshot_session.jpg",   "Live Avatar — Session Starting","The Talk to Me interface with Start Session, Hold to Talk, and End Session controls plus a live status strip."),
    ("assets/screenshot_active.jpg",    "Live Avatar — Active Conversation","The avatar face streams in the video panel and speaks; the transcript panel captures every turn in real time."),
    ("assets/architecture.png",         "System Architecture",           "Data flow: Browser → Node/Express → LiveAvatar API → LiveKit Room + ElevenLabs Agent → streamed response."),
]

g_cols = st.columns(2)
for i, (path, title, caption) in enumerate(gallery):
    with g_cols[i % 2]:
        img_path = Path(__file__).parent / path
        if img_path.exists():
            st.image(str(img_path), use_container_width=True)
        html(f"""
        <p class="gallery-caption">{title}</p>
        <p class="gallery-sub">{caption}</p>""")
        spacer("0.8rem")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# STACK + METHODS
# ─────────────────────────────────────────────────────────────────────────────
col_stack, col_methods = st.columns(2)

with col_stack:
    html("""
    <div class="card">
      <p class="eyebrow">Stack</p>
      <h3 style="color:#020617;font-size:1.45rem;font-weight:900;letter-spacing:-0.03em;margin:0.3rem 0 1rem">What LinkedOut is built on</h3>""")

    stack = [
        ("🖥 Frontend & Experience",
         ["HTML5", "CSS3 (custom dark-mode design system)", "Vanilla JavaScript", "Space Grotesk / Space Mono"],
         "Zero-framework frontend keeps the bundle tiny and load instant. Custom CSS variables handle the dark-mode palette and responsive layout."),
        ("🤖 AI, Avatar & Real-Time",
         ["LiveAvatar API (session token + start/stop)", "ElevenLabs Conversational Agent", "LiveKit WebRTC (video + audio + data)", "livekit-client JS SDK"],
         "LiveAvatar provisions sessions. LiveKit carries video, audio, and data events. ElevenLabs handles speech synthesis and conversational context."),
        ("⚙ Backend & Infrastructure",
         ["Node.js", "Express", "dotenv (secrets management)", "Static file serving"],
         "Express acts as a secure proxy — API keys never reach the client. Two endpoints handle the full session lifecycle."),
    ]
    for cat, tools, note in stack:
        chips = "".join(f'<span class="chip" style="font-size:0.8rem;padding:0.35rem 0.75rem">{t}</span>' for t in tools)
        html(f"""
        <div class="stack-card">
          <p class="stack-cat">{cat}</p>
          <div class="badge-row" style="margin-top:0;gap:0.4rem">{chips}</div>
          <p class="stack-note">{note}</p>
        </div>""")

    html("</div>")

with col_methods:
    html("""
    <div class="card">
      <p class="eyebrow">Methods</p>
      <h3 style="color:#020617;font-size:1.45rem;font-weight:900;letter-spacing:-0.03em;margin:0.3rem 0 1rem">Key techniques powering the experience</h3>""")

    methods = [
        ("Real-time WebRTC streaming",     "LiveKit publishes video and audio tracks into the browser with sub-second latency."),
        ("Conversational AI agent",        "ElevenLabs agent maintains context, generates responses, and drives the avatar's voice output."),
        ("Push-to-Talk & Open-Mic",        "Two input modes let users choose whether they hold a button to speak or leave the mic open."),
        ("Session token management",       "The Express backend mints per-session tokens so no API credentials are ever exposed to the client."),
        ("Live transcript & event logging","Every turn is decoded from the LiveKit data channel and rendered as a real-time chat transcript."),
    ]
    for title, note in methods:
        html(f"""
        <div style="display:flex;gap:0.75rem;align-items:flex-start;
                    background:rgba(240,249,255,0.55);border:1px solid rgba(186,230,253,0.6);
                    border-radius:16px;padding:1rem;margin-bottom:0.7rem">
          <div style="background:rgba(6,182,212,0.12);border-radius:12px;color:#0891b2;
                      height:2rem;min-width:2rem;display:flex;align-items:center;justify-content:center;
                      flex-shrink:0;font-size:0.85rem">✦</div>
          <div>
            <p style="color:#0f172a;font-size:0.93rem;font-weight:700;margin:0">{title}</p>
            <p style="color:#475569;font-size:0.85rem;line-height:1.7;margin:0.25rem 0 0">{note}</p>
          </div>
        </div>""")

    html("</div>")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# FEATURES
# ─────────────────────────────────────────────────────────────────────────────
html("""
<div class="section-header">
  <p class="eyebrow">Product</p>
  <h2>What LinkedOut delivers</h2>
  <p>Four distinct experiences — live avatar chat, real-time transcription, secure session management, and a full candidate portfolio — all in a single fast-loading site.</p>
</div>""")

features = [
    ("🎥", "Live Video Avatar Chat",
     "Visitors click 'Start Session' and within seconds are face-to-face with a lifelike video avatar. The avatar speaks, listens, and responds to natural questions about the candidate's background, skills, and projects.",
     ["Push-to-Talk (spacebar or button) and Open-Mic modes",
      "ElevenLabs voice synthesis — natural, low-latency speech",
      "LiveKit WebRTC streams video and audio with sub-second latency"]),
    ("📝", "Live Transcript & Event Stream",
     "Every conversation turn is captured and displayed in real time. A Live Transcript panel shows user and avatar utterances side-by-side. A separate Event Stream panel renders raw JSON events from the LiveKit data channel.",
     ["User and avatar lines distinguished by role labels",
      "Events: speak_started, speak_ended, transcription, mic state",
      "Full session history visible for the duration of the call"]),
    ("🔒", "Secure Session Management",
     "The Node/Express backend handles all credential operations server-side. The browser never touches an API key. Session tokens are minted per call and the stop endpoint is called on both End Session click and browser unload.",
     ["API key in .env — never exposed to the client",
      "Session stop called on click AND via sendBeacon on unload",
      "UUID validation guards avatar_id and voice_id inputs"]),
    ("🗂", "Candidate Portfolio Pages",
     "Alongside the avatar, the site ships full portfolio pages: a Home page with impact stats, an Experience timeline, a Projects gallery with modal overlays, and a Skills breakdown across languages, cloud, AI/ML, and agent systems.",
     ["Impact stats: 20+ hrs/week saved, 90% faster retrieval, 95% overhead reduction",
      "Projects: RAG platform, LLM fine-tuning, autonomous trading system",
      "Skills: Python/JS/C++, AWS, LangGraph, CrewAI, Pinecone, MLflow"]),
]

f_cols = st.columns(2)
for i, (icon, title, desc, highlights) in enumerate(features):
    with f_cols[i % 2]:
        checks = "".join(f"<li>{h}</li>" for h in highlights)
        html(f"""
        <div class="feature-card">
          <div class="feature-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <ul class="check-list">{checks}</ul>
        </div>""")
        spacer("0.75rem")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# ARCHITECTURE + CODE HIGHLIGHTS
# ─────────────────────────────────────────────────────────────────────────────
col_arch, col_code = st.columns(2)

with col_arch:
    html("""
    <div class="card">
      <p class="eyebrow">Architecture</p>
      <h3 style="color:#020617;font-size:1.45rem;font-weight:900;letter-spacing:-0.03em;margin:0.3rem 0 1rem">How the real-time pipeline works</h3>""")

    arch_steps = [
        ("User Input (Browser)",
         "The visitor uses mic controls (Push-to-Talk or Open-Mic) on talk.html. The livekit-client SDK publishes local audio tracks and sends control events over a data channel."),
        ("Session Provisioning (Node/Express)",
         "POST /api/session calls LiveAvatar API in two steps: minting a session token then starting the session. Returns the LiveKit URL and client token to the browser."),
        ("Real-Time Streaming (LiveKit Room)",
         "The browser connects to the LiveKit room. The avatar's video and audio tracks are subscribed and rendered. Data events flow bidirectionally for transcription and push-to-talk control."),
        ("Conversational AI (LiveAvatar + ElevenLabs)",
         "LiveAvatar's Plugin Worker routes the session to an ElevenLabs Agent that handles speech recognition, response generation, voice synthesis, and lip-sync back through LiveKit."),
    ]
    for n, (title, desc) in enumerate(arch_steps, 1):
        html(f"""
        <div class="arch-card">
          <div class="step-badge">{n}</div>
          <div>
            <h4>{title}</h4>
            <p>{desc}</p>
          </div>
        </div>""")

    html("</div>")

with col_code:
    html("""
    <div class="card">
      <p class="eyebrow">Code Highlights</p>
      <h3 style="color:#020617;font-size:1.45rem;font-weight:900;letter-spacing:-0.03em;margin:0.3rem 0 1rem">Key implementation details</h3>""")

    html("<p style='color:#475569;font-size:0.93rem;margin:0 0 0.6rem'><strong>Backend — Two-step session creation</strong><br>The Express proxy mints a token then immediately starts the session, returning the LiveKit URL/token in one response.</p>")
    st.code("""\
# Step 1 — mint a session token
const tokenResp = await fetch(`${BASE_URL}/v1/sessions/token`, {
  method: 'POST',
  headers: { 'X-API-KEY': LIVEAVATAR_API_KEY },
  body: JSON.stringify({
    mode: 'FULL', avatar_id: AVATAR_ID,
    interactivity_type: 'PUSH_TO_TALK',
    avatar_persona: { voice_id, context_id }
  })
});
const { session_token, session_id } = await tokenResp.json();

# Step 2 — activate the session
const startResp = await fetch(`${BASE_URL}/v1/sessions/start`, {
  method: 'POST',
  headers: { Authorization: `Bearer ${session_token}` },
  body: JSON.stringify({})
});
return res.json({ session_id, session_token, ...await startResp.json() });
""", language="javascript")

    html("<p style='color:#475569;font-size:0.93rem;margin:0.9rem 0 0.6rem'><strong>Frontend — LiveKit track subscription &amp; avatar render</strong><br>Video attaches to the avatar div; audio is appended to the body as a hidden element for auto-play.</p>")
    st.code("""\
room.on(RoomEvent.TrackSubscribed, (track) => {
  if (track.kind === 'video') {
    const el = track.attach();
    el.style.width = '100%'; el.style.height = '100%';
    avatarEl.innerHTML = '';
    avatarEl.appendChild(el);      // avatar face renders here
  } else if (track.kind === 'audio') {
    const el = track.attach();
    el.style.display = 'none';
    document.body.appendChild(el); // hidden audio auto-plays
  }
});
""", language="javascript")

    html("</div>")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# ROADMAP + RISKS
# ─────────────────────────────────────────────────────────────────────────────
col_road, col_risk = st.columns(2)

with col_road:
    html("""
    <div class="card">
      <p class="eyebrow">Roadmap</p>
      <h3 style="color:#020617;font-size:1.45rem;font-weight:900;letter-spacing:-0.03em;margin:0.3rem 0 1rem">Where LinkedOut is headed</h3>""")

    roadmap = [
        ("Now", [
            "Fully functional live avatar with Push-to-Talk and Open-Mic modes",
            "Secure Express backend handling session lifecycle for LiveAvatar API",
            "Static portfolio pages: Home, Projects (with modal), Skills, and Talk to Me",
            "Live transcript and raw event stream during every session",
        ]),
        ("Next", [
            "Context document upload so any candidate can configure their own avatar persona",
            "RAG layer over resume, portfolio, and GitHub repos for citation-backed answers",
            "Recruiter-facing session replay and summary for sharing/annotation",
            "Analytics dashboard tracking which questions were asked most",
        ]),
        ("Later", [
            "Multi-candidate platform: recruiter interviews shortlisted candidates via avatars",
            "ATS integration to trigger avatar sessions from a job application submit",
            "Mobile-optimized PWA so recruiters can talk to candidates on the go",
            "Bring-your-own-voice fine-tuning to match the candidate's actual vocal pattern",
        ]),
    ]

    phase_colors = {"Now": "#10b981", "Next": "#0891b2", "Later": "#6366f1"}
    for phase, items in roadmap:
        color = phase_colors.get(phase, "#0e7490")
        lis = "".join(f"<li>{item}</li>" for item in items)
        html(f"""
        <div class="roadmap-card" style="margin-bottom:0.75rem">
          <p class="roadmap-phase" style="color:{color}">{phase}</p>
          <ul style="margin:0;padding-left:1.2rem">
            {lis}
          </ul>
        </div>""")

    html("</div>")

with col_risk:
    html("""
    <div class="card">
      <p class="eyebrow">Risks</p>
      <h3 style="color:#020617;font-size:1.45rem;font-weight:900;letter-spacing:-0.03em;margin:0.3rem 0 1rem">Risks and how they are managed</h3>""")

    risks = [
        ("Third-Party API Dependency (LiveAvatar + ElevenLabs)",
         "Session-level error handling, graceful 'session failed' UI states, and a fallback text-chat mode keep the portfolio usable if streaming is unavailable."),
        ("Context Drift & Hallucination",
         "A tightly scoped persona context is injected at session creation. Future work adds a RAG grounding layer over verified candidate documents."),
        ("Session Cost and Latency at Scale",
         "LiveAvatar carries per-minute API costs. Mitigated by countdown timers enforced server-side and lazy session start to avoid idle charges."),
        ("Browser Mic Permission & WebRTC Compatibility",
         "Push-to-talk requires mic access; some corporate networks block WebRTC. The text-input Send button works without audio as a fallback."),
    ]
    for title, mit in risks:
        html(f"""
        <div class="risk-card">
          <p class="risk-title">⚠ {title}</p>
          <p class="risk-mit">{mit}</p>
        </div>""")

    html("</div>")

spacer()

# ─────────────────────────────────────────────────────────────────────────────
# CLOSING CARD
# ─────────────────────────────────────────────────────────────────────────────
html("""
<div class="closing">
  <div style="margin-bottom:1.5rem">
    <p style="color:rgba(186,230,253,0.85);font-size:0.74rem;font-weight:700;letter-spacing:0.26em;text-transform:uppercase;margin:0">The Bottom Line</p>
    <h2>LinkedOut: a portfolio that talks back</h2>
    <p>The job search is broken for strong communicators who get filtered out before a human ever hears them. LinkedOut fixes that — a live AI avatar, always available, representing the candidate with depth and personality.</p>
  </div>
""")

c1, c2, c3, c4 = st.columns(4)
closing_cards = [
    ("👥", "Who benefits?", "Recruiters and hiring managers get richer signal faster. Candidates get a 24/7 voice — no meeting needed."),
    ("🎯", "What changes?",  "Screening conversations happen on the recruiter's schedule, not the candidate's calendar — eliminating scheduling friction."),
    ("🏗", "Why this build?", "LiveKit WebRTC + ElevenLabs means the interaction is real-time and lifelike — not a chatbot, not a recording, but a live conversation."),
    ("🚀", "What is next?",  "RAG grounding over verified documents, recruiter-facing session replays, and a multi-candidate platform for agencies."),
]
for col, (icon, title, body) in zip([c1, c2, c3, c4], closing_cards):
    with col:
        html(f"""
        <div class="closing-mini">
          <div style="font-size:1.4rem">{icon}</div>
          <h3>{title}</h3>
          <p>{body}</p>
        </div>""")

html("</div>")
spacer()
