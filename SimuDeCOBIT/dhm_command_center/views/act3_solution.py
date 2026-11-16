import streamlit as st
import streamlit.components.v1 as components
from dhm_command_center.config.nav import NAV_OPTIONS
from dhm_command_center.data.fuentes import FUENTES
from dhm_command_center.components.status_bar import live_status_bar
from dhm_command_center.components.narrative import render_narrative_banner, render_plain_tooltip
from dhm_command_center.components.header import render_header
from dhm_command_center.components.nav_buttons import render_nav_buttons
from dhm_command_center.components.charts.timeline import render_roadmap_timeline

def render_strategic_decision_tree():
    st.markdown("""
    <div class="main-panel">
        <h4 style="color:var(--primary); margin:0 0 10px 0; font-family:'Share Tech Mono';">&gt; SIMULADOR DE DECISIÓN ESTRATÉGICA // INTERACTÚA CON EL TRIBUNAL</h4>
        <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:18px;">
            El jurado puede cambiar las 3 decisiones rectoras de DHM para comprobar cómo se reconfigura la priorización de Factores de Diseño en tiempo real:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        q1 = st.selectbox("1. Orientación Competitiva (DF1):", [
            "Liderazgo en Costos (Defensor)", 
            "Diferenciación / Innovación (Prospector)", 
            "Híbrido Equilibrado (Analizador)"
        ])
    with col2:
        q2 = st.selectbox("2. Enfoque de Ciberseguridad (DF3/DF5):", [
            "Prioridad Máxima: Mitigar SPOF y Servidor Único", 
            "Tolerancia Moderada: Invertir solo en Backup Básico", 
            "Baja Inversión: Asumir Riesgo Residual"
        ])
    with col3:
        q3 = st.selectbox("3. Metodología de Implementación (DF9):", [
            "Híbrido: 50% Ágil + 40% CMMI Nivel 2", 
            "100% Cascada Tradicional", 
            "100% DevOps Continuo"
        ])

    # Síntesis calculada
    if "Costos" in q1:
        foco_df1 = "APO06 (+30) y EDM04 (+30) activados para blindar el margen. Innovación acotada a pruebas pequeñas."
    elif "Innovación" in q1:
        foco_df1 = "APO04 (+50) y APO02 (+45) disparados. Mayor presupuesto en software pero riesgo de dispersión."
    else:
        foco_df1 = "Equilibrio entre costos y vigilancia selectiva de tecnología."

    if "Máxima" in q2:
        foco_df3 = "APO13 (+85) y DSS04 (+50) en máxima alerta. Mitigación obligatoria del SPOF de la PC única."
        color_alert = "var(--success)"
        alerta_text = "✓ ESTRATEGIA ALINEADA CON EL CASO REAL DHM (Pérdida evitada: $15,000 USD)."
    else:
        foco_df3 = "Alerta: El riesgo de infraestructura (20/25) queda desprotegido, elevando la pérdida probable a $15,000."
        color_alert = "var(--danger)"
        alerta_text = "⚠️ ADVERTENCIA: Esta configuración dejaría expuesta la facturación diaria de la empresa."

    st.markdown(f"""
    <div class="main-panel" style="border-left:4px solid {color_alert};">
        <div style="font-family:'Share Tech Mono'; color:{color_alert}; font-weight:700; font-size:0.95rem; margin-bottom:8px;">
            {alerta_text}
        </div>
        <div style="font-size:0.9rem; line-height:1.7; font-family:'Share Tech Mono';">
            <b>&gt; Impacto en Factor 1:</b> {foco_df1}<br>
            <b>&gt; Impacto en Factores 3 y 5:</b> {foco_df3}<br>
            <b>&gt; Metodología recomendada:</b> {q3} sincronizada con el CDC para cerrar las 10 brechas en 6 meses.
        </div>
        <div class="source-cite">// FUENTE: {FUENTES["DF_PLANTILLAS"]} + {FUENTES["MILES_SNOW"]}</div>
    </div>
    """, unsafe_allow_html=True)


def render_toolkit_budget_simulator():
    html = """
    <!DOCTYPE html><html><head>
    <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Share+Tech+Mono&display=swap');
    body{background:transparent;margin:0;font-family:'Share Tech Mono';color:#E2E8F0;}
    .sim-panel{background:linear-gradient(180deg,#0D131F,#06090F);border:1px solid #00F0FF;border-radius:8px;padding:20px;box-shadow:0 0 20px rgba(0,240,255,0.2);}
    .slider-row{display:flex;justify-content:space-between;margin-bottom:6px;font-size:0.85rem;font-weight:600;color:#00F0FF;}
    input[type=range]{width:100%;accent-color:#00F0FF;cursor:pointer;margin-bottom:14px;}
    .budget-display{font-size:1.25rem;color:#00FF66;text-align:center;margin-bottom:16px;}
    .preset-row{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px;}
    .preset{background:#0D131F;border:1px solid #00F0FF;color:#00F0FF;padding:10px;border-radius:6px;cursor:pointer;font-family:'Share Tech Mono';font-size:0.75rem;font-weight:700;text-transform:uppercase;transition:all .3s;text-align:center;}
    .preset:hover{background:rgba(0,240,255,0.15);box-shadow:0 0 20px rgba(0,240,255,0.6);}
    .alert-warn{background:rgba(255,0,60,0.15);border:1px solid #FF003C;color:#FF003C;padding:10px;border-radius:6px;margin-top:12px;font-size:0.85rem;display:none;text-align:center;}
    .alert-warn.show{display:block;}
    .roi-badge{background:rgba(0,255,102,0.15);border:1px solid #00FF66;color:#00FF66;padding:10px;border-radius:6px;margin-top:12px;font-size:0.85rem;text-align:center;}

    /* NUEVO: Grid de 3 KPIs grandes sobre el radar */
    .kpi-radar-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin:20px 0;}
    .kpi-radar-box{border-radius:10px;padding:16px 10px;text-align:center;position:relative;overflow:hidden;}
    .kpi-radar-box::before{content:'';position:absolute;inset:0;opacity:0.08;}
    .kpi-radar-riesgo{background:rgba(255,0,60,0.08);border:1px solid #FF003C;box-shadow:0 0 20px rgba(255,0,60,0.3), inset 0 0 20px rgba(255,0,60,0.1);}
    .kpi-radar-madurez{background:rgba(0,255,102,0.08);border:1px solid #00FF66;box-shadow:0 0 20px rgba(0,255,102,0.3), inset 0 0 20px rgba(0,255,102,0.1);}
    .kpi-radar-inv{background:rgba(0,240,255,0.08);border:1px solid #00F0FF;box-shadow:0 0 20px rgba(0,240,255,0.3), inset 0 0 20px rgba(0,240,255,0.1);}
    .kpi-radar-lbl{font-family:'Share Tech Mono';font-size:0.72rem;letter-spacing:1.5px;margin-bottom:6px;text-transform:uppercase;}
    .kpi-radar-val{font-family:'Bebas Neue',sans-serif;font-size:3.4rem;line-height:1;font-weight:bold;}
    .kpi-radar-val-riesgo{color:#FF003C;text-shadow:0 0 20px rgba(255,0,60,0.8);}
    .kpi-radar-val-madurez{color:#00FF66;text-shadow:0 0 20px rgba(0,255,102,0.8);}
    .kpi-radar-val-inv{color:#00F0FF;text-shadow:0 0 20px rgba(0,240,255,0.8);}
    .kpi-radar-sub{font-family:'Share Tech Mono';font-size:0.65rem;color:#64748B;margin-top:4px;}

    .radar-container{background:radial-gradient(circle at center, rgba(0,240,255,0.06) 0%, transparent 70%);border:1px solid #1E293B;border-radius:10px;padding:10px;margin-top:10px;}
    </style></head><body>
    <div class="sim-panel">
        <div class="budget-display">&gt; PRESUPUESTO ASIGNADO: <span id="remaining">$5,520 USD</span></div>
        <div class="preset-row">
            <div class="preset" onclick="setPreset(3500,1500,520)">🛡️ Paranoico (Seguridad)</div>
            <div class="preset" onclick="setPreset(2500,2000,1020)">⚖️ Equilibrado DHM</div>
            <div class="preset" onclick="setPreset(1200,1800,2520)">🚀 Innovador Digital</div>
        </div>
        <div class="slider-row"><span>🛡️ SEGURIDAD &amp; CONTINUIDAD (APO13/DSS04)</span><span id="val-sec">$2,500</span></div>
        <input type="range" id="sec" min="500" max="4500" value="2500" step="250" oninput="updateSim()">
        <div class="slider-row"><span>⚙️ CALIDAD &amp; CMMI NIVEL 2 (BAI03/BAI01)</span><span id="val-cal">$2,000</span></div>
        <input type="range" id="cal" min="500" max="4500" value="2000" step="250" oninput="updateSim()">
        <div class="slider-row"><span>🚀 INNOVACIÓN &amp; MEJORA (APO04)</span><span id="val-inv">$1,020</span></div>
        <input type="range" id="inv" min="0" max="3000" value="1020" step="250" oninput="updateSim()">

        <!-- KPIs GRANDES -->
        <div class="kpi-radar-grid">
            <div class="kpi-radar-box kpi-radar-riesgo">
                <div class="kpi-radar-lbl" style="color:#FF003C;">▲ RIESGO RESIDUAL</div>
                <div class="kpi-radar-val kpi-radar-val-riesgo" id="display-riesgo">28%</div>
                <div class="kpi-radar-sub">↓ menor es mejor</div>
            </div>
            <div class="kpi-radar-box kpi-radar-madurez">
                <div class="kpi-radar-lbl" style="color:#00FF66;">▲ MADUREZ CMMI</div>
                <div class="kpi-radar-val kpi-radar-val-madurez" id="display-madurez">85%</div>
                <div class="kpi-radar-sub">↑ mayor es mejor</div>
            </div>
            <div class="kpi-radar-box kpi-radar-inv">
                <div class="kpi-radar-lbl" style="color:#00F0FF;">▲ INNOVACIÓN AGREGADA</div>
                <div class="kpi-radar-val kpi-radar-val-inv" id="display-inv">41%</div>
                <div class="kpi-radar-sub">↑ mayor es mejor</div>
            </div>
        </div>

        <!-- RADAR GRANDE -->
        <div class="radar-container">
            <div id="chart"></div>
        </div>

        <div class="alert-warn" id="alert">⚠️ ADVERTENCIA: INVERSIÓN INSUFICIENTE EN SEGURIDAD — RIESGO RESIDUAL DEL SERVIDOR ÚNICO &gt; 50%</div>
        <div class="roi-badge" id="roi">💰 RETORNO NETO PROYECTADO: <span id="roi-val">+$17,080 USD</span></div>
    </div>
    <script>
    var chart;
    function setPreset(s,c,i){
        document.getElementById('sec').value=s;
        document.getElementById('cal').value=c;
        document.getElementById('inv').value=i;
        updateSim();
    }
    function updateSim(){
        var sec=parseInt(document.getElementById('sec').value);
        var cal=parseInt(document.getElementById('cal').value);
        var inv=parseInt(document.getElementById('inv').value);
        var total=sec+cal+inv;
        var diff=5520-total;
        document.getElementById('remaining').innerText='$'+total.toLocaleString()+' USD (Var: '+(diff>=0?'+':'')+diff+')';
        document.getElementById('val-sec').innerText='$'+sec.toLocaleString();
        document.getElementById('val-cal').innerText='$'+cal.toLocaleString();
        document.getElementById('val-inv').innerText='$'+inv.toLocaleString();

        var riesgo=Math.max(10,Math.round(100-(sec/35)));
        var madurez=Math.min(100,Math.round((cal/30)+(sec/60)));
        var innovacion=Math.min(100,Math.round(inv/25));

        document.getElementById('display-riesgo').innerText=riesgo+'%';
        document.getElementById('display-madurez').innerText=madurez+'%';
        document.getElementById('display-inv').innerText=innovacion+'%';

        chart.updateSeries([{name:'Índice Resultante',data:[riesgo,madurez,innovacion]}]);

        var alertEl=document.getElementById('alert');
        if(riesgo>45)alertEl.classList.add('show');
        else alertEl.classList.remove('show');

        var roi=(15000*(100-riesgo)/100)+(8400*madurez/100)-total;
        document.getElementById('roi-val').innerText=(roi>=0?'+$':'-$')+Math.abs(Math.round(roi)).toLocaleString()+' USD';
    }
    var options={
        series:[{name:'Índice Resultante',data:[28,85,41]}],
        chart:{type:'radar',height:480,background:'transparent',foreColor:'#00F0FF',fontFamily:'Share Tech Mono',toolbar:{show:false}},
        xaxis:{
            categories:['RIESGO RESIDUAL','MADUREZ CMMI','INNOVACIÓN AGREGADA'],
            labels:{style:{colors:['#FF003C','#00FF66','#00F0FF'],fontSize:'15px',fontFamily:'Share Tech Mono',fontWeight:'bold'}}
        },
        colors:['#00F0FF'],
        fill:{opacity:0.35,type:'solid'},
        stroke:{width:4,colors:['#00F0FF']},
        markers:{size:9,colors:['#00FF66'],strokeColors:['#FFFFFF'],strokeWidth:2},
        yaxis:{
            show:true,min:0,max:100,
            labels:{style:{colors:'#94A3B8',fontSize:'11px',fontFamily:'Share Tech Mono'},formatter:function(v){return Math.round(v)+'%';}},
            tickAmount:4
        },
        grid:{borderColor:'#1E293B'},
        plotOptions:{
            radar:{
                polygons:{
                    strokeColors:['#1E293B','#1E293B','#1E293B','#1E293B','#1E293B'],
                    connectorColors:['#00F0FF','#00F0FF','#00F0FF','#00F0FF','#00F0FF']
                }
            }
        },
        dataLabels:{
            enabled:true,
            background:{enabled:true,borderRadius:3,foreColor:'#000',padding:5,opacity:0.95},
            style:{fontSize:'14px',fontFamily:'Share Tech Mono',fontWeight:'bold',colors:['#000']},
            formatter:function(val){return Math.round(val)+'%';}
        },
        tooltip:{theme:'dark',style:{fontFamily:'Share Tech Mono'}}
    };
    chart=new ApexCharts(document.querySelector("#chart"),options);
    chart.render();
    updateSim();
    </script></body></html>
    """
    components.html(html, height=980)


def render_acto_3():
    live_status_bar()
    render_narrative_banner(
        "ACTO III: LA SOLUCIÓN",
        "PLAN ESTRATÉGICO, HOJA DE RUTA Y ASIGNACIÓN INTELIGENTE DE RECURSOS",
        "Presentamos el Roadmap de 4 trimestres para llevar a DHM a Nivel 2, el árbol de decisión interactivo para el jurado y el simulador de presupuesto que valida la viabilidad financiera de $5,520 USD."
    )
    render_plain_tooltip(
        "Mueva los sliders del simulador o pulse en los Presets para comprobar qué sucede si la empresa gasta más en seguridad que en innovación. No hay respuestas erróneas: la herramienta demuestra la sensibilidad del gobierno de TI.",
        "¿Cómo experimentar con la solución?"
    )
    render_header("HOJA DE RUTA & ASIGNACIÓN DE CAPITAL", "ROADMAP Q1-Q4 · ÁRBOL ESTRATÉGICO · SIMULADOR DE INVERSIÓN", "ACTO III: SOLUCIÓN")

    st.markdown('<div class="main-panel"><h3 style="color:var(--primary); font-family:\'Bebas Neue\'; font-size:1.8rem; margin:0 0 8px 0;">&gt; ROADMAP VISUAL: 4 FASES DE IMPLEMENTACIÓN HACIA CMMI NIVEL 2</h3>', unsafe_allow_html=True)
    render_roadmap_timeline()
    st.markdown(f'<div class="source-cite">// FUENTE: {FUENTES["CASO_NEGOCIO"]} (Fases 1 a 7 de Implementación CMMI)</div></div>', unsafe_allow_html=True)

    render_strategic_decision_tree()

    st.markdown('<div class="main-panel"><h3 style="color:var(--primary); font-family:\'Bebas Neue\'; font-size:1.8rem; margin:0 0 8px 0;">&gt; SIMULADOR DE INVERSIÓN DINÁMICA</h3><p style="color:var(--text); font-family:\'Share Tech Mono\'; font-size:0.9rem;">Pruebe los escenarios predefinidos o balancee el presupuesto autorizado de $5,520 USD:</p>', unsafe_allow_html=True)
    render_toolkit_budget_simulator()
    st.markdown('</div>', unsafe_allow_html=True)

    render_nav_buttons(prev_target=NAV_OPTIONS[2], next_target=NAV_OPTIONS[4])

