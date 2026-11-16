import math
import streamlit as st
import streamlit.components.v1 as components
from dhm_command_center.config.nav import NAV_OPTIONS
from dhm_command_center.data.factores import FACTORES
from dhm_command_center.components.status_bar import live_status_bar
from dhm_command_center.components.narrative import render_narrative_banner, render_plain_tooltip
from dhm_command_center.components.header import render_header
from dhm_command_center.components.nav_buttons import render_nav_buttons
from dhm_command_center.components.charts.heatmap import render_risk_heatmap_interactive

def render_epic_flip_cards(filtro_cat="Todos"):
    items = FACTORES
    if filtro_cat != "Todos":
        items = {k: v for k, v in FACTORES.items() if v["categoria"] == filtro_cat}

    html = """
    <!DOCTYPE html><html><head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Share+Tech+Mono&display=swap');
    body { background: transparent; margin: 0; font-family: 'Share Tech Mono'; }
    .deck { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; padding: 10px; }
    .card { height: 330px; perspective: 1200px; cursor: pointer; transition: transform 0.3s; }
    .card:hover { transform: translateY(-6px); }
    .card-inner { position: relative; width: 100%; height: 100%; transition: transform 0.8s cubic-bezier(.175,.885,.32,1.275); transform-style: preserve-3d; }
    .card.flipped .card-inner { transform: rotateY(180deg); }
    .card-front, .card-back { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; border-radius: 12px; padding: 22px; box-sizing: border-box; display: flex; flex-direction: column; }
    
    .card-front { background: linear-gradient(180deg, #0D131F 0%, #06090F 100%); border: 1px solid #00F0FF; border-top: 4px solid #00F0FF; align-items: center; justify-content: center; text-align: center; box-shadow: 0 0 25px rgba(0,240,255,0.25); }
    .card-icon { font-size: 2.8rem; margin-bottom: 6px; filter: drop-shadow(0 0 10px rgba(0,240,255,0.8)); }
    .card-title { font-family: 'Bebas Neue'; font-size: 2.4rem; color: #00F0FF; margin: 0; line-height: 1; letter-spacing: 2px; text-shadow: 0 0 15px rgba(0,240,255,0.8); }
    .card-subtitle { font-size: 0.8rem; color: #00FF66; margin-top: 6px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; text-shadow: 0 0 6px rgba(0,255,102,0.6); }
    .card-impact { font-size: 1.05rem; color: #FFB800; font-weight: 800; margin-top: 12px; text-shadow: 0 0 10px rgba(255,184,0,0.7); }
    .card-badges { display: flex; gap: 6px; margin-top: 10px; }
    
    .badge-pr { font-size: 0.65rem; padding: 3px 8px; border-radius: 4px; font-weight: 700; letter-spacing: 1px; }
    .pr-CRÍTICA { background: #FF003C; color: #FFF; box-shadow: 0 0 10px #FF003C; }
    .pr-ALTA { background: #FFB800; color: #000; box-shadow: 0 0 10px #FFB800; }
    .pr-MEDIA { background: #00F0FF; color: #000; box-shadow: 0 0 10px #00F0FF; }
    .badge-verif { font-size: 0.65rem; padding: 3px 8px; border-radius: 4px; background: rgba(0,255,102,0.15); color: #00FF66; border: 1px solid #00FF66; }

    .card-back { background: #04070D; border: 1px solid #FF003C; border-top: 4px solid #FF003C; transform: rotateY(180deg); text-align: left; justify-content: flex-start; overflow-y: auto; box-shadow: 0 0 25px rgba(255,0,60,0.25); }
    .card-back-title { font-family: 'Bebas Neue'; font-size: 1.5rem; color: #FF003C; margin: 0 0 8px 0; letter-spacing: 2px; text-shadow: 0 0 10px rgba(255,0,60,0.7); }
    
    /* Estilo para la nueva etiqueta de herramienta */
    .card-tool { background: rgba(0, 240, 255, 0.1); border-left: 3px solid #00F0FF; color: #00F0FF; padding: 6px 10px; font-size: 0.75rem; font-family: 'Share Tech Mono'; margin-bottom: 12px; border-radius: 0 4px 4px 0; }
    
    .card-back-text { font-size: 0.82rem; color: #E2E8F0; line-height: 1.55; }
    .card-back-ref { margin-top: auto; font-size: 0.68rem; color: #94A3B8; font-style: italic; border-top: 1px solid #1E293B; padding-top: 8px; }
    .card:hover .card-front { box-shadow: 0 0 35px rgba(0,240,255,0.5); }
    </style></head><body>
    <div class="deck">
    """
    
    for k, v in items.items():
        # Lógica para mostrar la etiqueta de herramienta solo si existe
        tool_html = f'<div class="card-tool">🛠️ HERRAMIENTA: {v["herramienta"]}</div>' if v.get("herramienta") else ''
        
        html += f"""
        <div class="card" onclick="this.classList.toggle('flipped')">
            <div class="card-inner">
                <div class="card-front">
                    <div class="card-icon">{v['icon']}</div>
                    <h3 class="card-title">{k}</h3>
                    <div class="card-subtitle">{v['nombre']}</div>
                    <div class="card-impact">{v['impacto']}</div>
                    <div class="card-badges">
                        <span class="badge-pr pr-{v['prioridad']}">{v['prioridad']}</span>
                        <span class="badge-verif">✓ VERIFICADO</span>
                    </div>
                    <div style="font-size:0.68rem; color:#64748B; margin-top:8px;">[CLIC PARA VOLTEAR]</div>
                </div>
                <div class="card-back">
                    <div class="card-back-title">&gt; CLASIFICACIÓN</div>
                    <div style="color:#00FF66; font-size:0.8rem; font-weight:bold; margin-bottom:6px;">{v['clase']}</div>
                    {tool_html}
                    <div class="card-back-text">{v['detalle']}</div>
                    <div class="card-back-ref">// FUENTE: {v['ref']}</div>
                </div>
            </div>
        </div>
        """
    
    html += "</div></body></html>"

    filas = math.ceil(len(items) / 3)
    altura = filas * 350 + 80
    components.html(html, height=altura, scrolling=True)


def render_acto_2():
    live_status_bar()
    render_narrative_banner(
        "ACTO II: EL DIAGNÓSTICO",
        "EVALUACIÓN INTEGRAL DE 11 FACTORES DE DISEÑO Y PERFIL DE RIESGOS",
        "Cruzamos las características reales de DHM con la metodología COBIT 2019. El resultado revela que la prioridad número 1 es APO13 (+85) por el severo perfil de riesgo de infraestructura y ciberseguridad."
    )
    render_plain_tooltip(
        "Haga clic en cualquiera de las 11 tarjetas para voltearlas y ver la evidencia documental y la cita académica que justifica la calificación asignada por el equipo.",
        "¿Cómo navegar este diagnóstico?"
    )
    render_header("FACTORES DE DISEÑO Y RIESGOS P×I", "DECK DE CARTAS VERIFICADAS Y MATRIZ INTERACTIVA 5×5", "ACTO II: DIAGNÓSTICO")

    st.markdown("""
    <div class="main-panel" style="border-left:4px solid var(--success);">
        <p style="font-family:'Share Tech Mono'; font-size:0.85rem; color:var(--success); margin:0;">
            ✓ <b>AUDITORÍA COMPLETADA:</b> Los 11 Factores de Diseño han sido validados con la plantilla oficial del expediente (extraido/PlantillasCobit11FactoresdeDiseño.txt) y la salida cuantitativa del Toolkit de Excel.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c_f1, c_f2 = st.columns([1, 2])
    with c_f1:
        filtro = st.selectbox("🔎 Filtrar Factores por Categoría:", ["Todos", "Gobernanza", "Gestión", "Comportamiento"])

    render_epic_flip_cards(filtro)

        # ... código anterior de render_epic_flip_cards(filtro) ...

    st.markdown('<div class="main-panel"><h3 style="color:var(--primary); font-family:\'Bebas Neue\'; font-size:1.8rem; margin:0 0 10px 0;">&gt; MAPA DE CALOR DE RIESGOS P×I (19 CATEGORÍAS COBIT)</h3><p style="color:var(--text-muted); font-size:0.85rem;">Haga clic en las celdas del cuadrante para explorar los 19 riesgos evaluados en DHM y conocer el objetivo COBIT responsable de mitigarlo.</p>', unsafe_allow_html=True)
    render_risk_heatmap_interactive()
    st.markdown('</div>', unsafe_allow_html=True)

    render_nav_buttons(prev_target=NAV_OPTIONS[1], next_target=NAV_OPTIONS[3])

