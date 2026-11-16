import streamlit as st


def inject_styles(pres_scale: str = "1.0", border_glow: str = "") -> None:
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&family=Inter:wght@300;400;600;700&display=swap');

:root {{
    --bg-dark: #06090F;
    --bg-panel: #0D131F;
    --border: #1E293B;
    --primary: #00F0FF;
    --secondary: #B026FF;
    --danger: #FF003C;
    --warning: #FFB800;
    --success: #00FF66;
    --text: #E2E8F0;
    --text-muted: #94A3B8;
}}

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-dark) !important;
    color: var(--text);
    font-size: calc(15px * {pres_scale});
}}

#MainMenu, footer {{ visibility: hidden; }}
.block-container {{ padding: 1.2rem 2rem 2.5rem 2rem; max-width: 100%; }}

h1, h2, h3, h4 {{ font-family: 'Rajdhani', sans-serif; letter-spacing: 1px; }}

.stApp {{
    background-color: var(--bg-dark);
    background-image:
        linear-gradient(rgba(0,240,255,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,240,255,0.04) 1px, transparent 1px);
    background-size: 36px 36px;
    animation: fadeIn 0.4s ease-in-out;
}}

@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(6px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes pulse-border {{
    0%, 100% {{ box-shadow: 0 0 15px rgba(0,240,255,0.4); border-color: #00F0FF; }}
    50% {{ box-shadow: 0 0 30px rgba(0,240,255,0.8); border-color: #00FF66; }}
}}

@keyframes cursor-blink {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0; }}
}}

.cursor-blink {{
    display: inline-block;
    color: var(--success);
    font-weight: bold;
    animation: cursor-blink 1s infinite;
}}

/* Micro-interacción: Hover suave en paneles */
.main-panel {{
    background: linear-gradient(180deg, var(--bg-panel) 0%, #06090F 100%);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 24px;
    box-shadow: 0 0 20px rgba(0,240,255,0.06);
    margin-bottom: 22px;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
    {border_glow}
}}

.main-panel:hover {{
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(0,240,255,0.18);
}}

.terminal-text {{
    font-family: 'Share Tech Mono', monospace;
    color: var(--success);
    background: #020408;
    padding: 20px;
    border-radius: 6px;
    border-left: 3px solid var(--success);
    box-shadow: 0 0 18px rgba(0,255,102,0.15), inset 0 0 20px rgba(0,0,0,0.8);
    font-size: 0.92rem;
    line-height: 1.8;
    text-shadow: 0 0 5px rgba(0,255,102,0.4);
}}

.source-cite {{
    font-size: 0.78rem;
    color: var(--text-muted);
    font-style: italic;
    margin-top: 14px;
    border-top: 1px solid #1E293B;
    padding-top: 8px;
    font-family: 'Share Tech Mono', monospace;
    letter-spacing: 0.5px;
}}

/* Banners narrativos estilo cómic/terminal para los 5 Actos */
.narrative-banner {{
    background: linear-gradient(90deg, #0D1B2A 0%, #06090F 100%);
    border-left: 4px solid var(--primary);
    border-right: 1px solid var(--primary);
    border-top: 1px solid #1E293B;
    border-bottom: 1px solid #1E293B;
    border-radius: 8px;
    padding: 16px 22px;
    margin-bottom: 22px;
    box-shadow: 0 0 25px rgba(0,240,255,0.12);
}}
.narrative-banner .act-tag {{
    font-family: 'Share Tech Mono', monospace;
    font-weight: 700;
    color: var(--primary);
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}}
.narrative-banner .act-desc {{
    font-family: 'Inter', sans-serif;
    color: #E2E8F0;
    font-size: 1.05rem;
    font-weight: 600;
    line-height: 1.5;
}}

/* Tooltips explicativos en lenguaje llano (CSS puro) */
.plain-tooltip {{
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(0,240,255,0.1);
    color: var(--primary);
    border: 1px solid var(--primary);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.8rem;
    font-family: 'Share Tech Mono', monospace;
    cursor: help;
    margin-bottom: 16px;
}}
.plain-tooltip:hover::after {{
    content: attr(data-tip);
    position: absolute;
    bottom: 125%;
    left: 0;
    width: 320px;
    background: #0D131F;
    color: #E2E8F0;
    border: 1px solid var(--primary);
    border-radius: 6px;
    padding: 12px;
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    line-height: 1.4;
    box-shadow: 0 0 25px rgba(0,240,255,0.4);
    z-index: 1000;
}}

/* Live Status Bar */
.live-status {{
    display: flex; gap: 14px; justify-content: space-between; flex-wrap: wrap;
    background: linear-gradient(90deg, #0D131F, #06090F);
    border: 1px solid var(--primary);
    border-radius: 6px;
    padding: 10px 18px;
    margin-bottom: 20px;
    box-shadow: 0 0 22px rgba(0,240,255,0.12);
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.78rem;
}}
.live-status .stat-item {{ display: flex; align-items: center; gap: 7px; }}
.live-status .dot {{
    width: 8px; height: 8px; border-radius: 50%;
    animation: pulse-dot 1.5s infinite;
}}
.dot-green  {{ background: #00FF66; box-shadow: 0 0 8px #00FF66; }}
.dot-red    {{ background: #FF003C; box-shadow: 0 0 8px #FF003C; }}
.dot-yellow {{ background: #FFB800; box-shadow: 0 0 8px #FFB800; }}
.dot-cyan   {{ background: #00F0FF; box-shadow: 0 0 8px #00F0FF; }}
@keyframes pulse-dot {{
    0%,100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.4; transform: scale(0.8); }}
}}

/* Sidebar Customization */
[data-testid="stSidebar"] {{
    background-color: var(--bg-dark) !important;
    border-right: 1px solid var(--primary);
    box-shadow: 4px 0 25px rgba(0,240,255,0.12);
}}
[data-testid="stSidebar"] .stRadio > div {{ display: flex; flex-direction: column; gap: 8px; }}
[data-testid="stSidebar"] .stRadio label {{
    background-color: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 12px 16px;
    cursor: pointer;
    transition: all 0.25s;
    color: var(--text-muted);
    font-weight: 600;
    font-size: 0.95rem;
    font-family: 'Rajdhani', sans-serif;
    letter-spacing: 0.5px;
}}
[data-testid="stSidebar"] .stRadio label:hover {{
    border-color: var(--primary); color: var(--primary);
    box-shadow: 0 0 16px rgba(0,240,255,0.35);
    text-shadow: 0 0 5px rgba(0,240,255,0.8);
}}
[data-testid="stSidebar"] .stRadio input {{ display: none; }}

/* Tags */
.tag {{
    display: inline-block; padding: 4px 10px; border-radius: 4px;
    font-size: 0.72rem; font-weight: 700; text-transform: uppercase;
    letter-spacing: 1.5px; font-family: 'Share Tech Mono', monospace;
}}
.tag-blue {{ background: rgba(0,240,255,0.12); color: var(--primary); border: 1px solid var(--primary); box-shadow: 0 0 10px rgba(0,240,255,0.3); }}
.tag-green {{ background: rgba(0,255,102,0.12); color: var(--success); border: 1px solid var(--success); box-shadow: 0 0 10px rgba(0,255,102,0.3); }}
.tag-red {{ background: rgba(255,0,60,0.12); color: var(--danger); border: 1px solid var(--danger); box-shadow: 0 0 10px rgba(255,0,60,0.3); }}
.tag-yellow {{ background: rgba(255,184,0,0.12); color: var(--warning); border: 1px solid var(--warning); box-shadow: 0 0 10px rgba(255,184,0,0.3); }}

/* Glow animations */
@keyframes glow-pulse {{
    0%, 100% {{ text-shadow: 0 0 12px rgba(0,240,255,0.6), 0 0 25px rgba(0,240,255,0.4); }}
    50% {{ text-shadow: 0 0 20px rgba(0,240,255,0.95), 0 0 35px rgba(0,240,255,0.7); }}
}}
.cyber-title {{ animation: glow-pulse 3s ease-in-out infinite; }}

/* Progress Bar animada con shine */
.animated-progress-container {{
    width: 100%; background: #0A0F1A; border: 1px solid var(--border);
    border-radius: 8px; height: 26px; overflow: hidden; position: relative;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.8);
}}
.animated-progress-bar {{
    height: 100%;
    background: linear-gradient(90deg, #00FF66, #00F0FF);
    position: relative;
    transition: width 0.6s ease;
}}
.animated-progress-bar::after {{
    content: '';
    position: absolute; top: 0; left: 0; bottom: 0; right: 0;
    background-image: linear-gradient(
        -45deg, 
        rgba(255, 255, 255, 0.25) 25%, 
        transparent 25%, 
        transparent 50%, 
        rgba(255, 255, 255, 0.25) 50%, 
        rgba(255, 255, 255, 0.25) 75%, 
        transparent 75%, 
        transparent
    );
    background-size: 50px 50px;
    animation: move-stripes 2s linear infinite;
}}
@keyframes move-stripes {{
    0% {{ background-position: 0 0; }}
    100% {{ background-position: 50px 50px; }}
}}

/* Achievement Badges */
.badge {{
    display: inline-flex; align-items: center; gap: 6px;
    padding: 8px 14px; border-radius: 20px;
    font-family: 'Share Tech Mono', monospace; font-size: 0.8rem; font-weight: 700;
    margin: 4px; text-transform: uppercase; letter-spacing: 1px;
}}
.badge-locked {{ background: rgba(100,116,139,0.12); color: #64748B; border: 1px dashed #64748B; }}
.badge-unlocked {{ background: rgba(0,255,102,0.15); color: var(--success); border: 1px solid var(--success); box-shadow: 0 0 15px rgba(0,255,102,0.45); }}

/* Botones de navegación al pie de página */
.nav-btn-row {{
    display: flex; justify-content: space-between; gap: 15px; margin-top: 30px;
    padding-top: 20px; border-top: 1px solid var(--border);
}}
</style>
""", unsafe_allow_html=True)

