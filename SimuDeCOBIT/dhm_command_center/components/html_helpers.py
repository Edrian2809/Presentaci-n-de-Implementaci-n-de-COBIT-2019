import streamlit as st

def show_html(html_str: str):
    """
    Renderiza HTML raw con soporte completo para estilos y scripts
    evitando que Streamlit lo interprete como Markdown.
    """
    st.markdown(html_str, unsafe_allow_html=True)
