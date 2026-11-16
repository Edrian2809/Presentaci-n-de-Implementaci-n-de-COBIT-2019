import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import streamlit as st
from dhm_command_center.config.nav import NAV_OPTIONS, init_session_state
from dhm_command_center.config.settings import get_settings
from dhm_command_center.styles.cyberpunk import inject_styles
from dhm_command_center.sidebar import render_sidebar
from dhm_command_center.views.act0_pitch import render_acto_0
from dhm_command_center.views.act1_problem import render_acto_1
from dhm_command_center.views.act2_diagnostic import render_acto_2
from dhm_command_center.views.act3_solution import render_acto_3
from dhm_command_center.views.act4_impact import render_acto_4
from dhm_command_center.views.act5_evidence import render_acto_5

st.set_page_config(
    page_title="DHM Command Center v4.0 | COBIT 2019 · CMMI v3.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

is_presentation, pres_scale, border_glow = get_settings()
inject_styles(pres_scale, border_glow)

init_session_state()
render_sidebar()

current_act = st.session_state.nav_page

if current_act == NAV_OPTIONS[0]:
    render_acto_0()
elif current_act == NAV_OPTIONS[1]:
    render_acto_1()
elif current_act == NAV_OPTIONS[2]:
    render_acto_2()
elif current_act == NAV_OPTIONS[3]:
    render_acto_3()
elif current_act == NAV_OPTIONS[4]:
    render_acto_4()
elif current_act == NAV_OPTIONS[5]:
    render_acto_5()
