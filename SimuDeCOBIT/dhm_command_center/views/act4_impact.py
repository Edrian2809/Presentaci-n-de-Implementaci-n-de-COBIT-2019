import streamlit as st
from dhm_command_center.config.nav import NAV_OPTIONS
from dhm_command_center.data.fuentes import FUENTES
from dhm_command_center.components.status_bar import live_status_bar
from dhm_command_center.components.narrative import render_narrative_banner, render_plain_tooltip
from dhm_command_center.components.header import render_header
from dhm_command_center.components.nav_buttons import render_nav_buttons
from dhm_command_center.components.html_helpers import show_html
from dhm_command_center.components.charts.waterfall import render_financial_waterfall
from dhm_command_center.components.charts.roi import render_roi_evolution
from dhm_command_center.components.charts.gauges import render_cobit_maturity_gauges

def render_acto_4():
    live_status_bar()
    render_narrative_banner(
        "ACTO IV: EL IMPACTO",
        "JUSTIFICACIÓN FINANCIERA IRREFUTABLE Y RETORNO DE LA INVERSIÓN (ROI)",
        "Demostramos con números auditables cómo una inversión de $6,320 USD genera $23,400 USD de beneficios anuales brutos, recuperando cada dólar invertido a partir del 4º mes de operación."
    )
    render_plain_tooltip(
        "Aquí observará el gráfico de cascada (Waterfall) de costos vs ganancias y la curva que demuestra el punto de equilibrio donde la inversión en COBIT se paga sola.",
        "¿Cómo leer los gráficos financieros?"
    )
    render_header("BUSINESS CASE & MEDIDORES COBIT", "RETORNO FINANCIERO DEMOSTRABLE (ROI +270%) & NIVELES DE CAPACIDAD", "ACTO IV: IMPACTO")

    c_w1, c_w2 = st.columns([1.5, 1.5])
    with c_w1:
        st.markdown('<div class="main-panel"><h4 style="color:var(--primary); margin:0 0 10px 0; font-family:\'Share Tech Mono\';">&gt; CASCADA DE BENEFICIOS NETOS (WATERFALL)</h4>', unsafe_allow_html=True)
        render_financial_waterfall()
        st.markdown(f'<div class="source-cite">// FUENTE: {FUENTES["CASO_NEGOCIO"]} (Anexo C y Contratos)</div></div>', unsafe_allow_html=True)
    with c_w2:
        st.markdown('<div class="main-panel"><h4 style="color:var(--success); margin:0 0 10px 0; font-family:\'Share Tech Mono\';">&gt; EVOLUCIÓN ACUMULADA DEL ROI (BREAK-EVEN EN M4)</h4>', unsafe_allow_html=True)
        render_roi_evolution()
        st.markdown(f'<div class="source-cite">// FUENTE: {FUENTES["CASO_NEGOCIO"]} (Flujo de Caja Anual)</div></div>', unsafe_allow_html=True)

    # AQUÍ ESTÁ EL FIX: Usamos show_html para evitar el error de Markdown
    show_html(f"""
<div class="main-panel">
<h4 style="color:var(--primary); margin-top:0; font-family:'Share Tech Mono';">&gt; DESGLOSE MATEMÁTICO AUDITABLE</h4>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
<div style="background: rgba(255,0,60,0.1); border-left: 3px solid var(--danger); padding: 15px;">
<h5 style="color: var(--danger); margin-top:0; font-family:'Share Tech Mono';">INVERSIÓN TOTAL: $6,320 USD</h5>
<ul style="color: var(--text); font-family:'Share Tech Mono'; font-size: 0.85rem; line-height: 1.6;">
<li>Licencias de Software (Jira, Power BI, SonarQube, Precoro): <b>$5,520</b></li>
<li>Capacitación del personal (APO07): <b>$800</b></li>
</ul>
</div>
<div style="background: rgba(0,255,102,0.1); border-left: 3px solid var(--success); padding: 15px;">
<h5 style="color: var(--success); margin-top:0; font-family:'Share Tech Mono';">BENEFICIOS BRUTOS: $23,400 USD</h5>
<ul style="color: var(--text); font-family:'Share Tech Mono'; font-size: 0.85rem; line-height: 1.6;">
<li>Ahorro Operativo (Eliminación de reprocesos, 120h/mes): <b>+$8,400</b></li>
<li>Pérdida Evitada (Mitigación del Riesgo R2 - 16/25): <b>+$15,000</b></li>
</ul>
</div>
</div>
<table style="width:100%; border-collapse:collapse; font-family:'Share Tech Mono'; font-size:0.88rem;">
<thead>
<tr style="border-bottom:2px solid var(--primary);">
<th style="text-align:left; padding:10px; color:var(--primary);">MÉTRICA FINANCIERA</th>
<th style="text-align:center; padding:10px; color:var(--danger);">SIN COBIT</th>
<th style="text-align:center; padding:10px; color:var(--success);">CON COBIT</th>
<th style="text-align:left; padding:10px; color:var(--warning);">IMPACTO EN NEGOCIO</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #1E293B;">
<td style="padding:10px;">Riesgo de parálisis por servidor único</td>
<td style="text-align:center; color:var(--danger);">Muy Alto (20/25)</td>
<td style="text-align:center; color:var(--success);">Mitigado (Backup + SLA)</td>
<td style="color:#E2E8F0;">Protege facturación diaria (R2)</td>
</tr>
<tr style="border-bottom:1px solid #1E293B;">
<td style="padding:10px;">Brechas de procesos CMMI abiertas</td>
<td style="text-align:center; color:var(--danger);">10 Brechas (B1-B10)</td>
<td style="text-align:center; color:var(--success);">0 Brechas (Nivel 2)</td>
<td style="color:#E2E8F0;">Estandarización operativa</td>
</tr>
<tr style="border-bottom:1px solid #1E293B;">
<td style="padding:10px;">Costo de incidentes y reprocesos</td>
<td style="text-align:center; color:var(--danger);">~$23,400 USD/año</td>
<td style="text-align:center; color:var(--success);">$6,320 USD inversión</td>
<td style="color:#00FF66; font-weight:bold;">Retorno Neto: +$17,080</td>
</tr>
<tr>
<td style="padding:10px;">Gobernanza y supervisión gerencial</td>
<td style="text-align:center; color:var(--danger);">Informal / Verbal (B8)</td>
<td style="text-align:center; color:var(--success);">CDC Institucionalizado</td>
<td style="color:#E2E8F0;">Decisiones basadas en Power BI</td>
</tr>
</tbody>
</table>
<div class="source-cite">// FUENTE: {FUENTES["CASO_NEGOCIO"]} + {FUENTES["MATRIZ_RIESGOS"]}</div>
</div>
""")

    st.markdown('<div class="main-panel"><h3 style="color:var(--primary); font-family:\'Bebas Neue\'; font-size:1.8rem; margin:0 0 10px 0;">&gt; MEDIDORES DE MADUREZ COBIT (CAPACIDAD ACTUAL vs TO-BE NIVEL 2)</h3>', unsafe_allow_html=True)
    render_cobit_maturity_gauges()
    st.markdown('</div>', unsafe_allow_html=True)

    render_nav_buttons(prev_target=NAV_OPTIONS[3], next_target=NAV_OPTIONS[5])

