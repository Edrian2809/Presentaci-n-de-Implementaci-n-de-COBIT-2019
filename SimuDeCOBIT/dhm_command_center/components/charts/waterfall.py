import streamlit.components.v1 as components

def render_financial_waterfall():
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
        <strong>&gt; FLUJO FINANCIERO:</strong> Iniciamos en 0. Las barras rojas son egresos (inversión total $6,320 USD). Las barras verdes son ingresos por ahorro y pérdida evitada. La barra final confirma el retorno neto de <strong>+$17,080 USD</strong>.
    </div>
    <script>
    var options = {
        series: [{name: 'Impacto Financiero (USD)', data: [{x:'Inicio', y:0}, {x:'Licencias', y:-5520}, {x:'Capacitación', y:-800}, {x:'Ahorro Operativo', y:8400}, {x:'Pérdida Evitada', y:15000}, {x:'Retorno Neto', y:17080}]}],
        chart: {type: 'bar', height: 320, background: 'transparent', foreColor: '#00F0FF', fontFamily: 'Share Tech Mono', toolbar: {show: false}},
        plotOptions: {bar: {columnWidth: '55%', borderRadius: 4, colors: {ranges: [{from: -20000, to: 0, color: '#FF003C'}, {from: 0, to: 20000, color: '#00FF66'}]}}},
        dataLabels: {enabled: true, formatter: function(v) { return (v < 0 ? '-' : '+') + '$' + Math.abs(v).toLocaleString(); }, style: {fontSize: '11px', fontWeight: 'bold', colors: ['#FFF']}},
        xaxis: {labels: {style: {colors: '#00F0FF', fontSize: '10px'}}},
        yaxis: {labels: {formatter: function(v) { return '$' + v.toLocaleString(); }, style: {colors: '#94A3B8'}}},
        grid: {borderColor: '#1E293B'}, tooltip: {theme: 'dark'}
    };
    new ApexCharts(document.querySelector("#chart"), options).render();
    </script></body></html>
    """
    components.html(html, height=440)
