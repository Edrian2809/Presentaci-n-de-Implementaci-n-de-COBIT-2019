import streamlit as st

def render_narrative_banner(acto, titulo, descripcion):
    st.markdown(f"""
    <div class="narrative-banner">
        <div class="act-badge">{acto}</div>
        <div class="act-title">{titulo}</div>
        <div class="act-desc">{descripcion}</div>
    </div>
    """, unsafe_allow_html=True)

def render_plain_tooltip(texto_llano, label="💡 EN ESPAÑOL CLARO (QUÉ SIGNIFICA ESTO)"):
    with st.expander(label):
        st.markdown(f'<div class="plain-talk">{texto_llano}</div>', unsafe_allow_html=True)
