import streamlit as st

def get_settings():
    is_presentation = st.sidebar.toggle(
        "🖥️ MODO PRESENTACIÓN (Proyector)",
        value=False,
        help="Aumenta tipografías un 30%, resalta paneles con glow pulsante cyan y simplifica controles para proyectar en el jurado."
    )
    pres_scale = "1.25" if is_presentation else "1.0"
    border_glow = "animation: pulse-border 2s infinite; border: 2px solid #00F0FF !important;" if is_presentation else ""
    return is_presentation, pres_scale, border_glow
