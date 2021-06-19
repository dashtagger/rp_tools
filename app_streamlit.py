import streamlit as st
import pandas as pd
import random

import event_meaning
import session_state

session_state = session_state.get(name='', event_focus=None,event_action=None,event_subject=None)

menu_selectbox = st.sidebar.selectbox(
    'Tools',
    ('Fate Dice', 'Generate Event', 'Scene Creation','Scene Management',"Character Creation","Character Management")
)
roll_d20 = st.sidebar.button("Roll D20")
if roll_d20:
    st.sidebar.write(random.randint(1,20))
        

if menu_selectbox == "Fate Dice":
    df_fate_chart = pd.read_csv("fate_chart.csv")
    odds_dict = {'Impossible':0,'No Way':1,'Very Unlikely':2,'Unlikely':3,'50/50':4,'Somewhat Likely':5,'Likely':6,'Very Likely':7,'Near Sure Thing':8,'A Sure Thing':9,'Has To Be':10}
    odds = st.select_slider("Odds",options = ['Impossible','No Way','Very Unlikely','Unlikely','50/50','Somewhat Likely','Likely','Very Likely','Near Sure Thing','A Sure Thing','Has To Be'],value = "50/50")
    odds_val = odds_dict[odds]
    st.write("")
    chaos_val = st.slider("Chaos",min_value= 1, max_value = 9,value=5)
    modifier_input = st.number_input(label = "Modifier",value=0)
    rate = df_fate_chart.iloc[odds_val,10-chaos_val]
    st.write(rate)
    roll_d100 = st.button("Roll D100")
    if roll_d100 == True:
        rate_list = rate.split('-')
        left_prob = float(rate_list[0])
        mid_prob = float(rate_list[1])
        right_prob = float(rate_list[2])
        
        result = "Unknown"
        roll_result = random.randint(1,100) + modifier_input
        st.write("Roll Value: " + str(roll_result))
        if roll_result <= left_prob:
            result = "Exceptional Yes"
        elif roll_result <= mid_prob:
            result = "Yes"
        elif roll_result <= right_prob:
            result = "No"
        else:
            result = "Exceptional No"
        st.subheader("Result: " +str(result)+"!")
    st.write("")
    st.write(df_fate_chart)
    
    

if menu_selectbox == "Generate Event":
    st.subheader("Summary of Resolving Random Events")
    st.write("1) Determine event focus.")
    st.write("2) Determine event meaning (the action and subject).")
    st.write("3) Interpret the random event based on context, focus and meaning. Take the most logical conclusion.")
    df_event_table = pd.read_csv("event_table.csv")
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
        st.subheader("Event Focus:" + result)
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