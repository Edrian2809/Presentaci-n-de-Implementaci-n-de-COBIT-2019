import streamlit as st
from dhm_command_center.config.nav import set_nav_page

def render_nav_buttons(prev_target=None, next_target=None):
    col_p, col_m, col_n = st.columns([1, 2, 1])
    if prev_target and col_p.button(f"⬅️ {prev_target.split(':')[0]}", use_container_width=True):
        set_nav_page(prev_target)
        st.rerun()
    if next_target and col_n.button(f"{next_target.split(':')[0]} ➡️", use_container_width=True):
        set_nav_page(next_target)
        st.rerun()
