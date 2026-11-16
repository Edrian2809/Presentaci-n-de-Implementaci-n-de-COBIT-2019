import streamlit.components.v1 as components

def render_roi_evolution():
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
        <strong>&gt; PUNTO DE EQUILIBRIO (BREAK-EVEN):</strong> La línea verde muestra el retorno acumulado. Cruza el eje cero exactamente en el <strong>Mes 4</strong>, momento en el que se recupera cada dólar invertido y comienza la generación de ganancias netas.
    </div>
    <script>
    var options = {
        series: [{name: 'Retorno Neto Acumulado (USD)', data: [0, -6320, -4370, -2420, 1480, 3430, 5380, 7330, 9280, 11230, 13180, 17080]}, {name: 'Línea de Equilibrio ($0)', data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}],
        chart: {type: 'line', height: 280, background: 'transparent', foreColor: '#00F0FF', fontFamily: 'Share Tech Mono', toolbar: {show: false}},
        stroke: {curve: 'smooth', width: [3, 1], dashArray: [0, 4]},
        colors: ['#00FF66', '#FFB800'],
        markers: {size: 4, colors: ['#00FF66']},
        xaxis: {categories: ['M0','M1','M2','M3','M4 (Break-even)','M5','M6','M7','M8','M9','M10','M12'], labels: {style: {colors: '#00F0FF', fontSize: '9px'}}},
        yaxis: {labels: {formatter: function(v) { return '$' + v.toLocaleString(); }, style: {colors: '#94A3B8'}}},
        grid: {borderColor: '#1E293B'},
        annotations: {points: [{x: 'M4 (Break-even)', y: 1480, marker: {size: 6, fillColor: '#00FF66', strokeColor: '#FFF'}, label: {borderColor: '#00FF66', style: {color: '#000', background: '#00FF66'}, text: 'BREAK-EVEN'}}]},
        tooltip: {theme: 'dark'}
    };
    new ApexCharts(document.querySelector("#chart"), options).render();
    </script></body></html>
    """
    components.html(html, height=400)
