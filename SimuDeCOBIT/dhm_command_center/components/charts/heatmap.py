import json
import streamlit.components.v1 as components
from dhm_command_center.data.riesgos import RIESGOS_MATRIZ

def render_risk_heatmap_interactive():
    SELECCIONADOS = {6, 11, 2, 4, 19} 
    
    riesgos_dict = {}
    for r in RIESGOS_MATRIZ:
        r_copy = r.copy()
        r_copy["selected"] = r["num"] in SELECCIONADOS
        riesgos_dict[str(r["num"])] = r_copy
        
    riesgos_json = json.dumps(riesgos_dict)

    html = f"""
    <!DOCTYPE html><html><head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Share+Tech+Mono&display=swap');
    body {{ background: transparent; margin: 0; font-family: 'Share Tech Mono'; color: #E2E8F0; }}
    .heatmap-layout {{ display: grid; grid-template-columns: 1fr 340px; gap: 20px; }}
    .grid-wrap {{ background: #070C16; border: 1px solid #1E293B; border-radius: 8px; padding: 20px; }}
    .grid-5x5 {{ display: grid; grid-template-columns: repeat(5, 1fr); grid-template-rows: repeat(5, 1fr); gap: 8px; height: 420px; }}

    /* ESTRUCTURA BASE DE LA CELDA */
    .cell-base {{
        border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center;
        cursor: pointer; font-weight: bold; transition: all 0.25s; position: relative; padding: 6px 4px; text-align: center;
        box-sizing: border-box;
    }}

    /* 1. LOS 5 CRÍTICOS (Brillantes) */
    .cell-crit-red {{ background: rgba(255, 0, 60, 0.4) !important; border: 2px solid #FF003C !important; box-shadow: 0 0 20px rgba(255,0,60,0.6) !important; }}
    .cell-crit-red:hover {{ transform: scale(1.08); z-index: 10; box-shadow: 0 0 35px rgba(255,0,60,1) !important; }}
    
    .cell-crit-amber {{ background: rgba(255, 184, 0, 0.4) !important; border: 2px solid #FFB800 !important; box-shadow: 0 0 20px rgba(255,184,0,0.6) !important; }}
    .cell-crit-amber:hover {{ transform: scale(1.08); z-index: 10; box-shadow: 0 0 35px rgba(255,184,0,1) !important; }}

    /* 2. LOS OTROS RIESGOS (Atenuados) */
    .cell-other-amber {{ background: rgba(255, 184, 0, 0.08) !important; border: 1px solid rgba(255, 184, 0, 0.4) !important; }}
    .cell-other-cyan {{ background: rgba(0, 240, 255, 0.05) !important; border: 1px solid rgba(0, 240, 255, 0.3) !important; }}
    .cell-other-green {{ background: rgba(0, 255, 102, 0.05) !important; border: 1px solid rgba(0, 255, 102, 0.3) !important; }}
    
    .cell-other-amber:hover, .cell-other-cyan:hover, .cell-other-green:hover {{ 
        transform: scale(1.03); z-index: 10; background: rgba(255,255,255,0.15) !important; border-color: #FFF !important; 
    }}

    /* 3. CELDAS VACÍAS (Ocultas por completo, pero mantienen el espacio en el grid) */
    .cell-empty {{ 
        visibility: hidden !important; 
        pointer-events: none !important;
    }}

    /* TIPOGRAFÍA */
    .val {{ font-size: 1.9rem; font-family: 'Bebas Neue'; line-height: 1; color: #FFF; }}
    .lbl {{ font-size: 0.55rem; letter-spacing: 1px; margin-top: 1px; text-transform: uppercase; }}
    .scr {{ font-size: 0.6rem; margin-top: 4px; padding-top: 4px; border-top: 1px solid rgba(255,255,255,0.1); width: 80%; }}
    
    .cell-crit-red .val {{ text-shadow: 0 0 12px #FF003C; color: #FFF !important; }}
    .cell-crit-amber .val {{ text-shadow: 0 0 12px #FFB800; color: #FFF !important; }}
    .cell-crit-red .lbl, .cell-crit-amber .lbl {{ color: #FFF !important; font-weight: bold; }}
    
    .cell-other-amber .val, .cell-other-amber .lbl {{ color: #FFB800 !important; opacity: 0.8; }}
    .cell-other-cyan .val, .cell-other-cyan .lbl {{ color: #00F0FF !important; opacity: 0.8; }}
    .cell-other-green .val, .cell-other-green .lbl {{ color: #00FF66 !important; opacity: 0.8; }}
    .cell-other-amber .scr, .cell-other-cyan .scr, .cell-other-green .scr {{ color: #64748B !important; }}

    /* PANEL DERECHO */
    .detail-panel {{
        background: #0D131F; border: 1px solid #00F0FF; border-radius: 8px; padding: 20px;
        box-shadow: 0 0 25px rgba(0, 240, 255, 0.15); display: flex; flex-direction: column; justify-content: space-between;
    }}
    .risk-badge {{ display: inline-block; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; }}
    .axis-label {{ font-size: 0.75rem; color: #94A3B8; text-align: center; letter-spacing: 1px; }}
    
    .risk-item {{ padding: 8px 10px; margin-bottom: 8px; background: rgba(255,255,255,0.03); border-radius: 4px; border-left: 3px solid #64748B; }}
    .risk-item.is-sel {{ background: rgba(255, 0, 60, 0.08); border-left-color: #FF003C; }}
    .risk-item .rt {{ font-weight: bold; font-size: 0.85rem; color: #FFF; display: flex; justify-content: space-between; }}
    .risk-item .rd {{ font-size: 0.75rem; color: #94A3B8; line-height: 1.4; margin-top: 4px; }}
    .risk-item .rc {{ font-size: 0.7rem; color: #00F0FF; margin-top: 6px; }}
    .star {{ color: #FFB800; font-size: 0.9rem; margin-left: 5px; font-weight: bold; }}
    </style></head><body>
    
    <div class="heatmap-layout">
        <div class="grid-wrap">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span class="axis-label">▲ IMPACTO (1 a 5)</span>
                <span class="axis-label">PROBABILIDAD (1 a 5) ▶</span>
            </div>
            <div class="grid-5x5">
    """
    
    for imp in range(5, 0, -1):
        for prob in range(1, 6):
            score = prob * imp
            risks_in_cell = [r for r in RIESGOS_MATRIZ if r["prob"] == prob and r["imp"] == imp]
            count = len(risks_in_cell)
            
            # ASIGNACIÓN ESTRICTA DE CLASES
            if count == 0:
                cls = "cell-base cell-empty"
                onclick = ""
                val = "0"
                lbl = "SIN RIESGO"
            else:
                has_selected = any(r["num"] in SELECCIONADOS for r in risks_in_cell)
                selected_count = sum(1 for r in risks_in_cell if r["num"] in SELECCIONADOS)
                
                if has_selected:
                    cls = "cell-base cell-crit-red" if score >= 20 else "cell-base cell-crit-amber"
                    val = str(selected_count) if selected_count > 0 else str(count)
                    lbl = "★ CRÍTICO" if selected_count == 1 else "★ CRÍTICOS"
                else:
                    if score >= 12: cls = "cell-base cell-other-amber"
                    elif score >= 6: cls = "cell-base cell-other-cyan"
                    else: cls = "cell-base cell-other-green"
                    val = str(count)
                    lbl = "OTRO" if count == 1 else "OTROS"
                
                risk_ids = ",".join(str(r["num"]) for r in risks_in_cell)
                onclick = f'onclick="showCellRisks([{risk_ids}], {score}, {prob}, {imp})"'
            
            html += f"""
                <div class="{cls}" {onclick}>
                    <div class="val">{val}</div>
                    <div class="lbl">{lbl}</div>
                    <div class="scr">P{prob}×I{imp}={score}</div>
                </div>
            """
    
    html += f"""
            </div>
            <div style="display: flex; justify-content: center; gap: 15px; margin-top: 14px; font-size: 0.75rem; flex-wrap: wrap;">
                <span style="color: #FF003C;">★ Seleccionados</span>
                <span style="color: #FFB800; opacity: 0.7;">■ Otros (Alto)</span>
                <span style="color: #00F0FF; opacity: 0.7;">■ Otros (Normal)</span>
                <span style="color: #00FF66; opacity: 0.7;">■ Otros (Bajo)</span>
            </div>
        </div>

        <div class="detail-panel" id="detail-box">
            <div>
                <div style="font-family: 'Bebas Neue'; font-size: 1.7rem; color: #00F0FF; letter-spacing: 1px; line-height: 1.1;" id="r-title">SELECCIONA UN CUADRANTE</div>
                <div style="margin: 8px 0;">
                    <span class="risk-badge" style="background: #334155; color: #FFF;" id="r-clas">HAZ CLIC EN LA MATRIZ</span>
                </div>
                <div id="r-desc" style="font-size: 0.85rem; line-height: 1.5; color: #CBD5E1;">
                    Las celdas <b style="color:#FF003C;">brillantes con ★</b> son los 5 riesgos críticos. Las celdas <b style="color:#94A3B8;">palidas</b> son los evaluados de menor prioridad.
                </div>
            </div>
            <div style="font-size: 0.7rem; color: #64748B; font-style: italic; margin-top: 10px;">
                // FUENTE: extraido/DocumentoFinalCobit2019.txt (Anexo 1 y 2, pp. 361-365)
            </div>
        </div>
    </div>

    <script>
    var risksDB = {riesgos_json};

    function showCellRisks(ids, score, prob, imp) {{
        var badge = document.getElementById('r-clas');
        var title = document.getElementById('r-title');
        var desc = document.getElementById('r-desc');
        
        var selectedCount = ids.filter(id => risksDB[id] && risksDB[id].selected).length;
        var titleText = 'P' + prob + '×I' + imp + ' = ' + score;
        
        if (selectedCount > 0) {{
            titleText += ' · ' + selectedCount + ' SELECCIONADO(S)';
            badge.style.background = score >= 20 ? '#FF003C' : '#FFB800';
        }} else {{
            titleText += ' · SECUNDARIOS';
            badge.style.background = '#64748B';
        }}
        
        badge.innerText = titleText;
        title.innerText = ids.length + (ids.length === 1 ? ' RIESGO ENCONTRADO' : ' RIESGOS ENCONTRADOS');
        
        var html = '';
        ids.sort((a, b) => (risksDB[b].selected ? 1 : 0) - (risksDB[a].selected ? 1 : 0));
        
        ids.forEach(function(id) {{
            var r = risksDB[id];
            if(!r) return;
            
            var isSel = r.selected;
            var cls = isSel ? 'is-sel' : '';
            var star = isSel ? '<span class="star">★ SELECCIONADO</span>' : '<span style="color:#64748B;font-size:0.7rem;">(No priorizado)</span>';
            
            html += '<div class="risk-item ' + cls + '">';
            html += '<div class="rt">' + r.cat + ' ' + star + '</div>';
            html += '<div class="rd">' + r.desc + '</div>';
            html += '<div class="rc">→ COBIT: ' + r.cobit + '</div>';
            html += '</div>';
        }});
        
        desc.innerHTML = html;
    }}
    </script></body></html>
    """
    components.html(html, height=520)
