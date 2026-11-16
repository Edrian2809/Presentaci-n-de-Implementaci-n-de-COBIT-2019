import streamlit.components.v1 as components

def render_roadmap_timeline():
    html = """
    <!DOCTYPE html><html><head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Share+Tech+Mono&family=Inter:wght@400;600;700&display=swap');
    body{background:transparent;margin:0;font-family:'Share Tech Mono';color:#E2E8F0;}
    .roadmap-track{display:grid;grid-template-columns:repeat(4,1fr);gap:15px;position:relative;padding:15px 0;}
    .phase-card{
        background:#0D131F;border:1px solid #1E293B;border-top:4px solid #00F0FF;
        border-radius:8px;padding:18px;transition:all .3s;cursor:pointer;
    }
    .phase-card:hover{
        transform:translateY(-5px);border-color:#00F0FF;box-shadow:0 0 25px rgba(0,240,255,0.3);
    }
    .phase-q{font-family:'Bebas Neue';font-size:1.8rem;color:#00F0FF;margin:0;}
    .phase-title{font-size:0.85rem;color:#00FF66;font-weight:700;margin-bottom:10px;letter-spacing:1px;}
    .milestone-item{font-size:0.78rem;color:#CBD5E1;margin-bottom:6px;line-height:1.4;}
    .cobit-pill{display:inline-block;padding:2px 6px;border-radius:3px;background:rgba(0,240,255,0.15);color:#00F0FF;font-size:0.68rem;font-weight:700;margin-top:8px;}
    </style></head><body>
    <div class="roadmap-track">
        <div class="phase-card" style="border-top-color:#00F0FF;">
            <div class="phase-q">Q1 · FASES 1-2</div>
            <div class="phase-title">&gt; GOBERNANZA &amp; CDC</div>
            <div class="milestone-item">✓ Constitución del CDC (Acta 001-2026)</div>
            <div class="milestone-item">✓ Firma de Sponsorship Charter con Carlos Méndez</div>
            <div class="milestone-item">✓ Diagnóstico de 10 Brechas CMMI (B1-B10)</div>
            <div class="cobit-pill">EDM01 · APO06 ($5,520)</div>
        </div>

        <div class="phase-card" style="border-top-color:#00FF66;">
            <div class="phase-q">Q2 · FASES 3-4</div>
            <div class="phase-title">&gt; PLAN &amp; CAPACITACIÓN</div>
            <div class="milestone-item">✓ Setup Jira Cloud + Confluence + SonarQube</div>
            <div class="milestone-item">✓ Política de Configuración (Anexo F)</div>
            <div class="milestone-item">✓ 40h de capacitación dirigida por Ing. Marcela Rivas</div>
            <div class="cobit-pill">BAI01 · APO04 · APO07</div>
        </div>

        <div class="phase-card" style="border-top-color:#FFB800;">
            <div class="phase-q">Q3 · FASE 5</div>
            <div class="phase-title">&gt; CIERRE DE BRECHAS</div>
            <div class="milestone-item">✓ Mitigación SPOF: backup automatizado PostgreSQL</div>
            <div class="milestone-item">✓ SLAs de hosting formalizados en Precoro</div>
            <div class="milestone-item">✓ Workflows de análisis de impacto y 5 Whys</div>
            <div class="cobit-pill">APO13 (+85) · BAI03 · DSS04</div>
        </div>

        <div class="phase-card" style="border-top-color:#B026FF;">
            <div class="phase-q">Q4 · FASES 6-7</div>
            <div class="phase-title">&gt; AUDITORÍA &amp; EVALUACIÓN</div>
            <div class="milestone-item">✓ Auditorías PQA independientes (Ana Sandoval)</div>
            <div class="milestone-item">✓ Tableros de control ejecutivos en Power BI</div>
            <div class="milestone-item">✓ Evaluación formal CMMI v3.0 Nivel 2</div>
            <div class="cobit-pill">MEA03 · EDM02 · MEA01</div>
        </div>
    </div>
    </body></html>
    """
    components.html(html, height=260)
