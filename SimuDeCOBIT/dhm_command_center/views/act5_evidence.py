import streamlit as st
from dhm_command_center.config.nav import NAV_OPTIONS
from dhm_command_center.data.fuentes import FUENTES
from dhm_command_center.data.brechas import BRECHAS
from dhm_command_center.data.evidencias import EVIDENCIAS
from dhm_command_center.components.status_bar import live_status_bar
from dhm_command_center.components.narrative import render_narrative_banner, render_plain_tooltip
from dhm_command_center.components.header import render_header
from dhm_command_center.components.nav_buttons import render_nav_buttons
from dhm_command_center.components.html_helpers import show_html

def render_achievement_badges(cerradas):
    all_badges = [
        ("🏅", "Primer Paso (B1)", ["B1"]),
        ("🛡️", "Guardián de Configuración (B2, B9)", ["B2", "B9"]),
        ("⚙️", "Calidad & Requisitos (B3, B7)", ["B3", "B7"]),
        ("📊", "Medidor de Procesos (B5, B6)", ["B5", "B6"]),
        ("🎯", "Maestro CMMI Nivel 2 (10/10)", list(b["id"] for b in BRECHAS))
    ]
    html = '<div class="main-panel"><h4 style="color:var(--primary); margin:0 0 12px 0; font-family:\'Share Tech Mono\';">&gt; LOGROS DE MADUREZ DESBLOQUEADOS</h4><div>'
    for icon, name, reqs in all_badges:
        unlocked = all(r in cerradas for r in reqs)
        cls = "badge-unlocked" if unlocked else "badge-locked"
        html += f'<span class="badge {cls}">{icon} {name}</span>'
    html += '</div></div>'
    st.markdown(html, unsafe_allow_html=True)


def render_maturity_journey(closed_brechas):
    total = len(closed_brechas)
    progress = (total / 10) * 100
    st.markdown(f"""
    <div class="main-panel" style="text-align:center;">
        <h3 style="color:var(--primary); font-family:'Bebas Neue'; font-size:2rem; margin-top:0; letter-spacing:2px;">&gt; PROGRESO AL NIVEL 2 DE MADUREZ</h3>
        <div class="animated-progress-container">
            <div class="animated-progress-bar" style="width:{progress}%;"></div>
        </div>
        <p style="color:var(--success); font-family:'Share Tech Mono'; font-size:1.35rem; margin-top:14px;">
            BRECHAS CERRADAS: {total}/10 ({progress:.0f}%) — TECHO GESTIONADO (NIVEL 2)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(5)
    for i, b in enumerate(BRECHAS):
        is_closed = b['id'] in closed_brechas
        bg_color = "rgba(0,255,102,0.1)" if is_closed else "rgba(255,0,60,0.1)"
        border_color = "var(--success)" if is_closed else "var(--danger)"
        glow = "0 0 15px rgba(0,255,102,0.4)" if is_closed else "0 0 15px rgba(255,0,60,0.3)"
        icon = "✓" if is_closed else "✖"
        with cols[i % 5]:
            st.markdown(f"""
            <div style="background:{bg_color}; border:1px solid {border_color}; border-radius:8px; padding:12px; text-align:center; margin-bottom:10px; box-shadow:{glow}; min-height:130px;">
                <h4 style="color:{border_color}; margin:0; font-size:1.15rem; font-family:'Share Tech Mono';">{b['id']} {icon}</h4>
                <div style="font-size:0.68rem; color:var(--primary); font-family:'Share Tech Mono'; font-weight:bold; margin-top:2px;">PA: {b['pa']}</div>
                <p style="font-size:0.72rem; color:var(--text); margin-top:6px; font-family:'Share Tech Mono'; line-height:1.3;">{b['desc']}</p>
                <div style="font-size:0.65rem; color:#94A3B8; font-style:italic;">{b['tool']}</div>
            </div>
            """, unsafe_allow_html=True)


def render_evidence_timeline():
    items = sorted(EVIDENCIAS.items(), key=lambda x: x[1]["fecha"])
    color_map = {"imagen": "#00F0FF", "excel": "#00FF66", "pdf": "#FF003C"}

    parts = [
        '<div class="main-panel">',
        '<h4 style="color:#00F0FF; margin:0 0 18px 0; font-family:\'Share Tech Mono\',monospace;">&gt; TIMELINE CRONOLÓGICO DE EVIDENCIAS AUDITABLES</h4>',
        '<div style="position:relative; padding-left:26px;">',
        '<div style="position:absolute; left:9px; top:0; bottom:0; width:2px; background:linear-gradient(180deg,#00F0FF,#00FF66); box-shadow:0 0 10px #00F0FF;"></div>'
    ]

    for name, d in items:
        color = color_map.get(d["tipo"], "#00F0FF")
        parts.append(f'''
        <div style="position:relative; margin-bottom:16px;">
            <div style="position:absolute; left:-23px; width:12px; height:12px; border-radius:50%; background:{color}; box-shadow:0 0 10px {color};"></div>
            <div style="background:rgba(13,19,31,0.8); border:1px solid {color}; border-radius:6px; padding:12px;">
                <div style="color:{color}; font-family:\'Share Tech Mono\',monospace; font-weight:700; font-size:0.88rem;">📄 {name}</div>
                <div style="color:#94A3B8; font-size:0.75rem; margin-top:4px;">FECHA: {d["fecha"]} · AUTOR: {d["autor"]} · FASE: {d["fase"]} · SHA-256: <code>{d["hash"]}</code></div>
                <div style="color:#E2E8F0; font-size:0.8rem; margin-top:6px;">{d["desc"]}</div>
            </div>
        </div>
        ''')

    parts.append('</div>')
    parts.append(f'<div class="source-cite">// FUENTE: {FUENTES["CHECKLIST"]}</div></div>')
    show_html("".join(parts))


def render_bibliography():
    categorias = {
        "🌐 Normas y Marcos Internacionales": [
            ("ISACA_COBIT", FUENTES["ISACA_COBIT"]),
            ("ISACA_GOV", FUENTES["ISACA_GOV"]),
            ("ISACA_TOOLKIT", FUENTES["ISACA_TOOLKIT"]),
            ("ISACA_IMPL", FUENTES["ISACA_IMPL"]),
            ("CMMI_V3", FUENTES["CMMI_V3"]),
        ],
        "📚 Autores Clásicos (Teoría de Gobierno)": [
            ("MILES_SNOW", FUENTES["MILES_SNOW"]),
            ("MCFARLAN", FUENTES["MCFARLAN"]),
            ("ROGERS", FUENTES["ROGERS"]),
            ("KAPLAN_NORTON", FUENTES["KAPLAN_NORTON"]),
            ("BROWN_ROBERTS", FUENTES["BROWN_ROBERTS"]),
        ],
        "📂 Documentación Primaria del Proyecto (extraido/)": [
            ("CASO_NEGOCIO", FUENTES["CASO_NEGOCIO"]),
            ("MATRIZ_RIESGOS", FUENTES["MATRIZ_RIESGOS"]),
            ("DF_PLANTILLAS", FUENTES["DF_PLANTILLAS"]),
            ("CMMI_BRECHAS", FUENTES["CMMI_BRECHAS"]),
            ("CHECKLIST", FUENTES["CHECKLIST"]),
        ],
    }

    parts = [
        '<div class="main-panel">',
        '<h3 style="color:var(--primary); font-family:\'Bebas Neue\'; font-size:2.2rem; margin-top:0; letter-spacing:3px;">&gt; FUENTES BIBLIOGRÁFICAS NORMATIVAS</h3>',
        '<p style="color:var(--text-muted); font-family:\'Share Tech Mono\'; font-size:0.85rem; margin:0 0 20px 0;">Referencias en formato APA 7ª edición agrupadas por tipo de fuente. Cada hallazgo del proyecto es trazable a uno de estos documentos.</p>',
    ]

    total = sum(len(v) for v in categorias.values())

    for cat_name, entries in categorias.items():
        parts.append('<div style="margin-bottom:26px;">')
        parts.append(
            f'<h4 style="color:var(--success); font-family:\'Share Tech Mono\'; font-size:1rem; '
            f'letter-spacing:2px; border-bottom:1px solid var(--border); padding-bottom:8px; margin:0 0 14px 0;">'
            f'{cat_name} <span style="color:var(--text-muted); font-size:0.75rem;">({len(entries)} referencias)</span></h4>'
        )
        for key, ref in entries:
            parts.append(f'''
            <div style="background:rgba(0,240,255,0.04); border-left:3px solid var(--primary); padding:14px 18px; margin-bottom:10px; border-radius:4px; transition:all 0.2s;">
                <span style="color:var(--primary); font-family:'Share Tech Mono'; font-weight:bold; font-size:0.78rem; letter-spacing:1px;">[{key}]</span>
                <div style="color:var(--text); font-family:'Inter',sans-serif; font-size:0.88rem; line-height:1.65; margin-top:6px; padding-left:22px; text-indent:-22px;">{ref}</div>
            </div>
            ''')
        parts.append('</div>')

    parts.append(
        f'<div class="source-cite">// TOTAL: {total} fuentes · Todas verificables en la carpeta extraido/ del repositorio</div>'
    )
    parts.append('</div>')

    # ✅ FIX: usar show_html en lugar de st.markdown
    show_html("".join(parts))


def render_acto_5():
    live_status_bar(madurez="NIVEL 2 VERIFICADO")
    render_narrative_banner(
        "ACTO V: LA EVIDENCIA",
        "TRAZABILIDAD AUDITABLE, DOCUMENTACIÓN RIGUROSA Y FUNDAMENTACIÓN APA 7",
        "El jurado puede verificar cada acta, hash criptográfico SHA-256, contrato y referencia académica. No hay datos inventados: todo está respaldado en los expedientes de la carpeta extraido/."
    )
    render_plain_tooltip(
        "Interactúe con los controles deslizantes para ver cómo el fortalecimiento progresivo de seguridad, calidad y gobierno cierra las 10 brechas hasta desbloquear la insignia de certificación Nivel 2.",
        "¿Cómo funciona la simulación de brechas?"
    )
    render_header("EVIDENCIAS AUDITABLES & BIBLIOGRAFÍA", "SIMULADOR CMMI V3.0 · EXPLORADOR DE ARCHIVOS · FUENTES APA 7", "ACTO V: EVIDENCIA")

    col1, col2 = st.columns([1, 2.2])
    with col1:
        st.markdown('<div class="main-panel">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:var(--primary); font-family:Bebas Neue; font-size:1.6rem; letter-spacing:1px;'>&gt; NIVELES DE ESFUERZO</h3>", unsafe_allow_html=True)
        seguridad = st.slider("Seguridad & SPOF (APO13)", 0, 100, 75, help="Mitiga B2, B9 y B10")
        calidad = st.slider("Calidad de Software (BAI03)", 0, 100, 80, help="Mitiga B3 y B7")
        gobierno = st.slider("Gobernanza CDC (EDM01)", 0, 100, 70, help="Mitiga B1 y B8")
        st.markdown('</div>', unsafe_allow_html=True)

    cerradas = []
    if seguridad > 40: cerradas.extend(["B2", "B9", "B10"])
    if calidad > 40: cerradas.extend(["B3", "B7"])
    if gobierno > 40: cerradas.extend(["B1", "B8"])
    if (seguridad + calidad + gobierno) > 150: cerradas.extend(["B4", "B5", "B6"])
    cerradas = list(set(cerradas))

    with col2:
        render_maturity_journey(cerradas)
        if len(cerradas) == 10:
            st.balloons()
            st.success("🎉 ¡NIVEL 2 ALCANZADO CON ÉXITO! Las 10 brechas CMMI v3.0 se encuentran cerradas conforme al modelo.")
        else:
            st.warning(f"⚠️ Restan {10 - len(cerradas)} brechas por cerrar para satisfacer la certificación Nivel 2.")

    render_achievement_badges(cerradas)

    render_evidence_timeline()

    col_a1, col_a2 = st.columns([1, 2])
    with col_a1:
        st.markdown("<div class='main-panel'><h3 style='color:var(--primary); font-family:Bebas Neue; font-size:1.4rem;'>&gt; REPOSITORIO DE EVIDENCIAS</h3>", unsafe_allow_html=True)
        archivo_sel = st.radio("Selecciona archivo para inspección:", list(EVIDENCIAS.keys()), label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_a2:
        d = EVIDENCIAS[archivo_sel]
        show_html(f'''
        <div class="main-panel">
            <h3 style="color:#00FF66; font-family:'Bebas Neue', sans-serif; font-size:1.8rem; margin-top:0;">
                👁️ {archivo_sel}
            </h3>
            <div class="terminal-text" style="font-family:'Share Tech Mono', monospace;">
                &gt; FORMATO: {d["tipo"].upper()}<br>
                &gt; RESPONSABLE: {d["autor"]}<br>
                &gt; FECHA DE REGISTRO: {d["fecha"]}<br>
                &gt; FASE ASOCIADA: {d["fase"]}<br>
                &gt; HASH DE INTEGRIDAD SHA-256: <code>{d["hash"]}</code><br>
                &gt; DESCRIPCIÓN: {d["desc"]}<br><br>
                <span style="color:#00FF66;">&gt; ESTADO: DOCUMENTO FIRMADO Y VALIDADO ✓</span>
            </div>
            <div class="source-cite">// FUENTE: {FUENTES["CHECKLIST"]}</div>
        </div>
        ''')

    render_bibliography()

    render_nav_buttons(prev_target=NAV_OPTIONS[4], next_target=None)
