import streamlit as st
import random
import pandas as pd

import attributes.event_meaning as event_meaning

def generate_event(session_state):
    st.subheader("Summary of Resolving Random Events")
    st.write("1) Determine event focus.")
    st.write("2) Determine event meaning (the action and subject).")
    st.write("3) Interpret the random event based on context, focus and meaning. Take the most logical conclusion.")
    df_event_table = pd.read_csv("tables/event_table.csv")
    bc_l,bc_r = st.beta_columns([5,5])
    roll_event_focus = bc_l.button("Roll D100 to generate event focus")
    result = "Unknown"
    if roll_event_focus:
        roll_result = random.randint(1,100)
        bc_r.write("Roll Value: " + str(roll_result))
        if roll_result<=7:
            result = "Remote event"
        elif roll_result <=28:
            result = "NPC action"
        elif roll_result <=35:
            result = "Introduce new NPC"
        elif roll_result <=45:
            result = "Move toward a thread"
        elif roll_result <=52:
            result = "Move away from a thread"
        elif roll_result <=55:
            result = "Close a thread"
        elif roll_result <=67:
            result = "PC negative"
        elif roll_result <=75:
            result = "PC positive"
        elif roll_result <=83:
            result = "Ambigous event"
        elif roll_result <=92:
            result = "NPC Negative"
        elif roll_result <=100:
            result = "NPC Positive"
        session_state.event_focus = result
        st.subheader("Event Focus: " + result)
        st.write(df_event_table[df_event_table["Event"]==result].iloc[0,1])
    elif session_state.event_focus is not None:
        st.subheader("Event Focus: " + session_state.event_focus)
        st.write(df_event_table[df_event_table["Event"]==session_state.event_focus].iloc[0,1])

    roll_event_meaning = st.button("Roll to generate event meaning")
    if roll_event_meaning or roll_event_focus:
        st.subheader("Event Meaning")
        action = random.choice(event_meaning.Action)
        subject = random.choice(event_meaning.Subject)
        st.write("Action: "+ action)
        st.write("Subject: "+ random.choice(event_meaning.Subject))
        session_state.event_action = action
        session_state.event_subject = subject
    elif session_state.event_action is not None and session_state.event_subject is not None:
        st.subheader("Event Meaning")
        st.write("Action: "+ session_state.event_action)
        st.write("Subject: "+ session_state.event_subject)

def generate_quick_event(session_state):
    df_event_table = pd.read_csv("tables/event_table.csv")
    bc_l,bc_r = st.sidebar.beta_columns([5,5])
    side_roll_event_focus = bc_l.button("Generate event focus")
    result = "Unknown"
    if side_roll_event_focus:
        roll_result = random.randint(1,100)
        bc_r.write("Roll Value: " + str(roll_result))
        if roll_result<=7:
            result = "Remote event"
        elif roll_result <=28:
            result = "NPC action"
        elif roll_result <=35:
            result = "Introduce new NPC"
        elif roll_result <=45:
            result = "Move toward a thread"
        elif roll_result <=52:
            result = "Move away from a thread"
        elif roll_result <=55:
            result = "Close a thread"
        elif roll_result <=67:
            result = "PC negative"
        elif roll_result <=75:
            result = "PC positive"
        elif roll_result <=83:
            result = "Ambigous event"
        elif roll_result <=92:
            result = "NPC Negative"
        elif roll_result <=100:
            result = "NPC Positive"
        bc_r.write("Event Focus: " + result)
        bc_r.write("Action: "+ random.choice(event_meaning.Action))
        bc_r.write("Subject: "+ random.choice(event_meaning.Subject))
       