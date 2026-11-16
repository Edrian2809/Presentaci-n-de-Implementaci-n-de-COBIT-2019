import streamlit as st
import streamlit.components.v1 as components
from dhm_command_center.config.nav import NAV_OPTIONS, set_nav_page
from dhm_command_center.data.fuentes import FUENTES
from dhm_command_center.components.status_bar import live_status_bar

def render_pitch_hero():
    # Hero Title con efecto de typing CSS
    html = f"""
    <!DOCTYPE html><html><head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Share+Tech+Mono&family=Inter:wght@400;600;700&display=swap');
    body {{ background: transparent; margin: 0; font-family: 'Inter', sans-serif; color: #E2E8F0; text-align: center; }}
    
    .hero-container {{
        background: radial-gradient(circle at center, rgba(0,240,255,0.08) 0%, #06090F 75%);
        border: 1px solid #00F0FF;
        border-radius: 12px;
        padding: 40px 25px;
        box-shadow: 0 0 40px rgba(0,240,255,0.2), inset 0 0 30px rgba(0,240,255,0.05);
        position: relative;
        overflow: hidden;
    }}
    
    /* Scanlines effect CSS */
    .hero-container::before {{
        content: " ";
        display: block; position: absolute; top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
        z-index: 2; background-size: 100% 3px, 6px 100%; pointer-events: none;
    }}
    
    .typing-title {{
        font-family: 'Bebas Neue', sans-serif;
        font-size: 3.8rem;
        color: #00F0FF;
        letter-spacing: 5px;
        margin: 0;
        text-shadow: 0 0 20px rgba(0,240,255,0.9), 0 0 40px rgba(0,240,255,0.4);
    }}
    
    .hero-sub {{
        font-family: 'Share Tech Mono', monospace;
        color: #00FF66;
        font-size: 1.15rem;
        letter-spacing: 2px;
        margin-top: 10px;
        text-shadow: 0 0 10px rgba(0,255,102,0.7);
    }}
    
    .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin: 35px auto 25px auto;
        max-width: 900px;
    }}
    
    .kpi-box {{
        background: rgba(13, 19, 31, 0.85);
        border: 1px solid #1E293B;
        border-radius: 8px;
        padding: 22px 15px;
        transition: transform .3s, border-color .3s;
    }}
    .kpi-box:hover {{
        transform: translateY(-5px);
        border-color: #00F0FF;
        box-shadow: 0 0 25px rgba(0,240,255,0.3);
    }}
    
    .kpi-val {{
        font-family: 'Bebas Neue', sans-serif;
        font-size: 3.2rem;
        line-height: 1;
        margin-bottom: 6px;
    }}
    .kpi-lbl {{
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.82rem;
        color: #94A3B8;
        letter-spacing: 1px;
    }}
    
    .terminal-box {{
        font-family: 'Share Tech Mono', monospace;
        background: #020408;
        border: 1px solid #00FF66;
        border-left: 4px solid #00FF66;
        border-radius: 6px;
        padding: 16px 20px;
        max-width: 850px;
        margin: 25px auto;
        text-align: left;
        color: #00FF66;
        font-size: 0.9rem;
        line-height: 1.7;
        box-shadow: 0 0 20px rgba(0,255,102,0.15);
    }}
    </style></head><body>
    <div class="hero-container">
        <div style="font-family:'Share Tech Mono'; color:#00F0FF; font-size:0.8rem; letter-spacing:4px; margin-bottom:8px;">[ UNIVERSIDAD NACIONAL DE INGENIERÍA · ISACA COBIT 2019 &amp; CMMI v3.0 ]</div>
        <h1 class="typing-title">DHM COMMAND CENTER v4.0</h1>
        <div class="hero-sub">&gt; TRANSFORMANDO EL GOBIERNO DE I&amp;T EN DISTRIBUIDORA HUEVOS MÉNDEZ</div>
        
        <div class="kpi-grid">
            <div class="kpi-box" style="border-top:3px solid #00F0FF;">
                <div class="kpi-val" style="color:#00F0FF; text-shadow:0 0 15px #00F0FF;">$6,320</div>
                <div class="kpi-lbl">INVERSIÓN TOTAL (LICENCIAS + CAPACITACIÓN)</div>
            </div>
            <div class="kpi-box" style="border-top:3px solid #FF003C;">
                <div class="kpi-val" style="color:#FF003C; text-shadow:0 0 15px #FF003C;">$15,000</div>
                <div class="kpi-lbl">PÉRDIDA ANUAL EVITADA (SPOF RESIDUAL)</div>
            </div>
            <div class="kpi-box" style="border-top:3px solid #00FF66;">
                <div class="kpi-val" style="color:#00FF66; text-shadow:0 0 15px #00FF66;">+270%</div>
                <div class="kpi-lbl">ROI NETO ESTIMADO (+$17,080 USD A 12M)</div>
            </div>
        </div>
        
        <div class="terminal-box">
            &gt; ENTIDAD: Distribuidora Huevos Méndez, S.A. (DHM) — 38 Empleados (38.0 FTE)<br>
            &gt; VULNERABILIDAD DIAGNOSTICADA: Sistema central PostgreSQL operando en una única PC sin backup automático<br>
            &gt; DICTAMEN: Riesgo Muy Alto (20/25) de parálisis total operativa por fallo de infraestructura (DF3)<br>
            &gt; ESTRATEGIA: Implementación de 9 Objetivos Prioritarios COBIT 2019 + Cierre de 10 Brechas CMMI Nivel 2<br>
            &gt; RETORNO: Break-even alcanzado en Mes 4. Retorno neto generado de +$17,080 USD en el primer año.<br>
            &gt; <span style="animation:cursor-blink 1s infinite;">█ SISTEMA LISTO PARA DEFENSA ANTE EL JURADO</span>
        </div>
        
        <div style="font-family:'Share Tech Mono'; font-size:0.75rem; color:#64748B; margin-top:20px;">
            // FUENTE OFICIAL: {FUENTES["CASO_NEGOCIO"]} + {FUENTES["DF_PLANTILLAS"]}
        </div>
    </div>
    </body></html>
    """
    components.html(html, height=620)
    
    # Giant CTA Button Streamlit
    st.markdown("<br>", unsafe_allow_html=True)
    c_l, c_btn, c_r = st.columns([1, 2, 1])
    with c_btn:
        if st.button("⚡ INICIAR DIAGNÓSTICO Y DEFENSA →", use_container_width=True, type="primary"):
            set_nav_page(NAV_OPTIONS[1])
            st.rerun()


def render_acto_0():
    live_status_bar()
    render_pitch_hero()

