import streamlit as st

NAV_OPTIONS = [
    "🎬 PITCH: Hero Landing",
    "ACTO I: El Problema (Visión General)",
    "ACTO II: El Diagnóstico (DF1-DF11 & Riesgos)",
    "ACTO III: La Solución (Roadmap, Decisión & Inversión)",
    "ACTO IV: El Impacto (Business Case & Madurez)",
    "ACTO V: La Evidencia (Brechas CMMI & Bibliografía)"
]

def init_session_state():
    if "nav_page" not in st.session_state:
        st.session_state.nav_page = NAV_OPTIONS[0]

def set_nav_page(target: str):
    st.session_state.nav_page = target
