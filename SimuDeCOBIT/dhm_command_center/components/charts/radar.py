import streamlit.components.v1 as components

def render_system_health_radar():
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
        margin-top: 15px;
        color: #E2E8F0;
        font-size: 0.85rem;
        box-shadow: 0 0 15px rgba(176, 38, 255, 0.2);
    }
    .cyber-explain-violet strong { color: #B026FF; }
    </style>
    </head><body>
    <div id="chart"></div>
    <div class="cyber-explain-violet">
        <strong>&gt; DIAGNÓSTICO AS-IS vs TO-BE:</strong> El área roja representa la capacidad actual de DHM (baja madurez). El área verde es la meta a Nivel 2. La brecha visual entre ambas justifica la inversión del proyecto.
    </div>
    <script>
    var options = {
        series: [{name: 'Capacidad Actual (AS-IS)', data: [35, 40, 25, 30, 20]}, {name: 'Meta CMMI Nivel 2 (TO-BE)', data: [80, 85, 80, 80, 75]}],
        chart: {type: 'radar', height: 300, background: 'transparent', foreColor: '#00F0FF', fontFamily: 'Share Tech Mono', toolbar: {show: false}},
        xaxis: {categories: ['EDM (Gobierno)', 'APO (Alineación)', 'BAI (Construcción)', 'DSS (Entrega)', 'MEA (Monitoreo)'], labels: {style: {colors: ['#00F0FF','#00F0FF','#00F0FF','#00F0FF','#00F0FF'], fontSize: '11px'}}},
        colors: ['#FF003C', '#00FF66'],
        fill: {opacity: 0.25}, stroke: {width: 2}, markers: {size: 4},
        yaxis: {show: false, min: 0, max: 100},
        grid: {borderColor: '#1E293B'},
        legend: {position: 'bottom', labels: {colors: '#E2E8F0'}, fontFamily: 'Share Tech Mono'}
    };
    new ApexCharts(document.querySelector("#chart"), options).render();
    </script></body></html>
    """
    components.html(html, height=460)
