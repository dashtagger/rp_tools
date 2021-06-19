import streamlit as st
import pandas as pd
import random

def generate_fate(session_state,location):
    df_fate_chart = pd.read_csv("tables/fate_chart.csv")
    odds_dict = {'Impossible':0,'No Way':1,'Very Unlikely':2,'Unlikely':3,'50/50':4,'Somewhat Likely':5,'Likely':6,'Very Likely':7,'Near Sure Thing':8,'A Sure Thing':9,'Has To Be':10}
    odds = location.select_slider("Odds",options = ['Impossible','No Way','Very Unlikely','Unlikely','50/50','Somewhat Likely','Likely','Very Likely','Near Sure Thing','A Sure Thing','Has To Be'],value = "50/50")
    odds_val = odds_dict[odds]
    location.write("")
    chaos_val = location.slider("Chaos",min_value= 1, max_value = 9,value=5)
    modifier_input = location.number_input(label = "Modifier",value=0)
    rate = df_fate_chart.iloc[odds_val,10-chaos_val]
    #location.write(rate)
    roll_d100 = location.button("Roll D100")
    if roll_d100 == True:
        rate_list = rate.split('-')
        left_prob = float(rate_list[0])
        mid_prob = float(rate_list[1])
        right_prob = float(rate_list[2])
        
        result = "Unknown"
        roll_result = random.randint(1,100) + modifier_input
        location.write("Roll Value: " + str(roll_result))
        if roll_result <= left_prob:
            result = "Exceptional Yes"
        elif roll_result <= mid_prob:
            result = "Yes"
        elif roll_result <= right_prob:
            result = "No"
        else:
            result = "Exceptional No"
        location.subheader("Result: " +str(result)+"!")
    #st.write(df_fate_chart)