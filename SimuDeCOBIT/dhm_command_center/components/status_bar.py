import datetime
import streamlit as st

def live_status_bar(riesgo="ALTO (20/25)", presupuesto="$5,520 USD", madurez="NIVEL 1 → 2"):
    st.markdown(f"""
    <div class="live-status">
        <div class="stat-item"><span class="dot dot-green"></span> SISTEMA: ONLINE</div>
        <div class="stat-item"><span class="dot dot-red"></span> RIESGO RESIDUAL: {riesgo}</div>
        <div class="stat-item"><span class="dot dot-cyan"></span> PRESUPUESTO I&amp;T: {presupuesto}</div>
        <div class="stat-item"><span class="dot dot-purple"></span> OBJETIVO CMMI: {madurez}</div>
        <div class="stat-item" style="margin-left:auto; color:var(--text-muted); font-size:0.75rem;">TIMESTAMP: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
    </div>
    """, unsafe_allow_html=True)
