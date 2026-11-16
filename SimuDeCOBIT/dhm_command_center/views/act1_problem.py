import streamlit as st
from dhm_command_center.config.nav import NAV_OPTIONS
from dhm_command_center.data.fuentes import FUENTES
from dhm_command_center.components.status_bar import live_status_bar
from dhm_command_center.components.narrative import render_narrative_banner, render_plain_tooltip
from dhm_command_center.components.header import render_header
from dhm_command_center.components.nav_buttons import render_nav_buttons
from dhm_command_center.components.charts.radar import render_system_health_radar

def render_pulse_indicators():
    kpis = [
        ("PERSONAL TOTAL", "38.0 FTE", "primary", "🏢", "extraido/Plantillas (DF11)"),
        ("BRECHAS CMMI", "10 Gaps", "danger", "🧩", "extraido/Implementación7Fases"),
        ("MÁXIMA PRIORIDAD", "+85 APO13", "warning", "🚨", "extraido/DocumentoFinal (DF3)"),
        ("ROI ESTIMADO", "+$17,080", "success", "💰", "extraido/Implementación7Fases")
    ]
    cols = st.columns(4)
    for i, (label, value, color, icon, src) in enumerate(kpis):
        with cols[i]:
            st.markdown(f"""
            <div class="main-panel" style="text-align:center; border-top:3px solid var(--{color}); margin-bottom:0;">
                <div style="font-size:1.6rem; margin-bottom:4px;">{icon}</div>
                <div style="font-size:2.2rem; font-weight:700; color:var(--{color}); font-family:'Bebas Neue'; text-shadow:0 0 15px var(--{color});">{value}</div>
                <div style="font-size:0.75rem; color:var(--text-muted); font-family:'Share Tech Mono'; letter-spacing:1px;">{label}</div>
            </div>
            """, unsafe_allow_html=True)


def render_acto_1():
    live_status_bar()
    render_narrative_banner(
        "ACTO I: EL PROBLEMA",
        "LA FRAGILIDAD DE UNA OPERACIÓN MANUAL EN CRECIMIENTO",
        "DHM cuenta con 38 empleados que distribuyen miles de huevos diarios, pero toda su facturación y base de datos dependen de una única computadora de escritorio sin respaldo automatizado ni firewall. Una avería paraliza la empresa por completo."
    )
    render_plain_tooltip(
        "Aquí verá la fotografía completa del estado de salud actual de la empresa versus la meta requerida para certificar el Nivel 2 de madurez en gobernanza de tecnología.",
        "¿De qué trata esta sección?"
    )
    render_header("DHM COMMAND CENTER", "SISTEMA DE GOBIERNO DE I&T // COBIT 2019 · CMMI v3.0", "ACTO I: RESUMEN EJECUTIVO")
    render_pulse_indicators()

    col1, col2 = st.columns([1.6, 1.4])
    with col1:
        st.markdown('<div class="main-panel"><h4 style="color:var(--primary); margin:0 0 12px 0; font-family:\'Share Tech Mono\';">&gt; SALUD ORGANIZACIONAL POR DOMINIO COBIT</h4>', unsafe_allow_html=True)
        render_system_health_radar()
        st.markdown(f'<div class="source-cite">// FUENTE: {FUENTES["ISACA_TOOLKIT"]} + {FUENTES["CMMI_BRECHAS"]}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="main-panel">
            <h4 style="color:var(--primary); margin:0 0 12px 0; font-family:'Share Tech Mono';">&gt; ANÁLISIS DE SITUACIÓN AS-IS (DIAGNÓSTICO)</h4>
            <div class="terminal-text" style="font-size:0.85rem;">
                &gt; ORGANIZACIÓN: Distribuidora Huevos Méndez (38.0 FTE)<br>
                &gt; SISTEMA BASE: Python/Django + PostgreSQL on-premise<br>
                &gt; PUNTO CRÍTICO: 10 Brechas CMMI abiertas (B1 a B10)<br>
                &gt; RIESGO SPOF: PC de escritorio actúa como servidor sin backup<br>
                &gt; COSTO IMPLEMENTACIÓN: $6,320 USD ($5,520 Lic. + $800 Cap.)<br>
                &gt; PÉRDIDA ESTIMADA EVITADA: $15,000 USD anuales<br>
                &gt; META AUDITORÍA: Alcanzar CMMI v3.0 Nivel 2 Gestionado<br>
                &gt; <span class="cursor-blink">█</span>
            </div>
            <div class="source-cite">// FUENTE: {FUENTES["CASO_NEGOCIO"]}</div>
        </div>
        """, unsafe_allow_html=True)

    render_nav_buttons(prev_target=NAV_OPTIONS[0], next_target=NAV_OPTIONS[2])

