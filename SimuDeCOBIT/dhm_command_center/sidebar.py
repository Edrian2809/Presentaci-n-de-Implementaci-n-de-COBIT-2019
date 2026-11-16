import streamlit as st
from dhm_command_center.config.nav import NAV_OPTIONS

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center; padding:12px 0 18px 0;">
            <h1 style="color:var(--primary); font-family:'Bebas Neue'; margin:0; font-size:2.5rem; letter-spacing:3px; text-shadow:0 0 20px rgba(0,240,255,0.8);">⚡ COBIT 2019</h1>
            <p style="color:var(--success); font-family:'Share Tech Mono'; font-size:0.75rem; letter-spacing:2px; margin-top:4px;">&gt; DHM COMMAND CENTER v4.0</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Navegación con radio sincronizado
        selected_nav = st.radio(
            "HISTORIA EN 5 ACTOS",
            NAV_OPTIONS,
            index=NAV_OPTIONS.index(st.session_state.nav_page),
            label_visibility="visible"
        )
        if selected_nav != st.session_state.nav_page:
            st.session_state.nav_page = selected_nav
            st.rerun()

        st.markdown("---")
        st.markdown("""
        <div style="font-size:0.75rem; color:var(--text-muted); line-height:1.7; font-family:'Share Tech Mono';">
            <b style="color:var(--primary);">DEFENSA ACADÉMICA:</b><br>
            Ingeniería de Software III · UNI<br><br>
            <b style="color:var(--primary);">EQUIPO DE TRABAJO:</b><br>
            • Anngelly Aleska Mejia<br>
            • Edrian Gabriel Espinoza<br>
            • Eliza Sougey Aguirre<br><br>
            <b style="color:var(--primary);">TUTOR:</b><br>
            Msc. Roberto Carlos Alfaro<br><br>
            <b style="color:var(--primary);">ESTADO AUDITORÍA:</b> <span style="color:var(--success); text-shadow:0 0 8px rgba(0,255,102,0.8);">● ONLINE</span>
        </div>
        """, unsafe_allow_html=True)
