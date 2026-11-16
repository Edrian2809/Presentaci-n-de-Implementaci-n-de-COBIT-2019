import streamlit.components.v1 as components

def render_cobit_maturity_gauges():
    html = """
    <!DOCTYPE html><html><head>
    <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    body { background: transparent; margin: 0; font-family: 'Share Tech Mono'; }
    .cyber-explain-violet {
        background: rgba(176, 38, 255, 0.08);
        border-left: 4px solid #B026FF;
        border-top: 1px solid rgba(176, 38, 255, 0.3);
        border-right: 1px solid rgba(176, 38, 255, 0.3);
        border-bottom: 1px solid rgba(176, 38, 255, 0.3);
        border-radius: 0 8px 8px 0;
        padding: 12px 18px;
        margin-top: 10px;
        color: #E2E8F0;
        font-size: 0.85rem;
        box-shadow: 0 0 15px rgba(176, 38, 255, 0.2);
    }
    .cyber-explain-violet strong { color: #B026FF; }
    </style>
    </head><body>
    <div id="chart"></div>
    <div class="cyber-explain-violet">
        <strong>&gt; ANÁLISIS DE BRECHAS (GAP):</strong> Las barras naranjas indican el nivel actual de capacidad por dominio. Las verdes son la meta Nivel 2. La distancia entre ambas es la hoja de ruta que justifica la asignación presupuestal.
    </div>
    <script>
    var options = {
        series: [{name: 'Situación Actual (AS-IS)', data: [35, 40, 25, 30, 20]}, {name: 'Meta Nivel 2 (TO-BE)', data: [80, 85, 80, 80, 75]}],
        chart: {type: 'bar', height: 300, background: 'transparent', foreColor: '#00F0FF', fontFamily: 'Share Tech Mono', toolbar: {show: false}},
        plotOptions: {bar: {horizontal: true, columnWidth: '55%', borderRadius: 4, dataLabels: {position: 'top'}}},
        colors: ['#FFB800', '#00FF66'],
        dataLabels: {enabled: true, formatter: function(val) { return val + '%'; }, style: {fontSize: '11px', fontWeight: 'bold'}, offsetX: 25},
        stroke: {show: true, width: 2, colors: ['transparent']},
        xaxis: {categories: ['EDM (Gobierno)', 'APO (Alineación)', 'BAI (Construcción)', 'DSS (Entrega)', 'MEA (Monitoreo)'], labels: {style: {colors: '#94A3B8', fontSize: '10px'}, formatter: function(val) { return val + '%'; }}, max: 100},
        yaxis: {labels: {style: {colors: '#00F0FF', fontSize: '11px', fontWeight: 'bold'}}},
        grid: {borderColor: '#1E293B', xaxis: {lines: {show: true}}},
        legend: {position: 'top', labels: {colors: '#E2E8F0'}, markers: {radius: 2}},
        tooltip: {theme: 'dark', y: {formatter: function(val) { return val + '% de Madurez'; }}}
    };
    new ApexCharts(document.querySelector("#chart"), options).render();
    </script></body></html>
    """
    components.html(html, height=400)
