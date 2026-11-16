import streamlit as st

def render_header(title, subtitle, tag=""):
    st.markdown(f"""
    <div class="main-header">
        <h1>{title}</h1>
        <p>{subtitle}</p>
        {f'<div class="tag-badge">{tag}</div>' if tag else ''}
    </div>
    """, unsafe_allow_html=True)
