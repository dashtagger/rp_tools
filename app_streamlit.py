import streamlit as st
import random

import utils.session_state as session_state
from generate.generate_event import generate_event
from generate.generate_fate import generate_fate
from manage.manage_scenes import manage_scenes

session_state = session_state.get(name='', event_focus=None,event_action=None,event_subject=None)

menu_selectbox = st.sidebar.selectbox(
    'Tools',
    ('Fate Dice', 'Generate Event', 'Adventure Creation','Scene Management',"Character Management")
)

roll_d20 = st.sidebar.button("Roll D20")
if roll_d20:
    st.sidebar.write(random.randint(1,20))
        

if menu_selectbox == "Fate Dice":
    generate_fate(session_state)

if menu_selectbox == "Generate Event":
    generate_event(session_state)

if menu_selectbox == "Scene Management":
    manage_scenes(session_state)