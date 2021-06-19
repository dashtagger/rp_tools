import streamlit as st
import pandas as pd
import os


def manage_scenes(session_state):
    lc,mc,rc = st.beta_columns([2,2,2])
    show_all_scenes= lc.radio("View all scenes",options=["Hide","Show"])
    show_scene_creation= mc.radio("Scene Creation",options=["Hide","Show"])
    show_scene_editor = rc.radio("Scene Editor",options=["Hide","Show"],index=1)
    scene_file =""
    df_scenes = None
    scene_file = st.selectbox("Select scene file",os.listdir("session/scenes"))
    df_scenes = pd.read_csv("session/scenes/"+scene_file)
    
    if show_all_scenes =="Show":
        st.write(df_scenes)

    if show_scene_creation=="Show":
        st.subheader("Scene Creation")
        scene_name = st.text_input(label="Scene Name",value="Default Scene Name")
        setting = st.text_area(label="Setting",value=" ")
        character_list = st.text_area(label="Character List",value=" ")
        chaos_factor = st.text_input(label="Chaos Factor",value=5)
        threads = st.text_area(label="Threads",value=" ")
        Notes = st.text_area(label="Notes",value=" ",height=500)
        add_scene = st.button("Add Scene to file")
        if add_scene:
            if len(df_scenes[df_scenes['Scene Name']==scene_name])>0:
                st.warning("Scene Name Exists! Use a different name")
            else:
                row = pd.DataFrame([[scene_name,setting,character_list,chaos_factor,threads,Notes]],columns=df_scenes.columns.values.tolist())
                df_scenes=pd.concat([df_scenes,row])
                df_scenes.to_csv("session/scenes/"+scene_file,index=False)
                st.success('Updated!')
                st.button("Refresh")

    if show_scene_editor=="Show":
        selected_scene_name = st.selectbox("Select Scene to modify",df_scenes['Scene Name'].tolist())
        st.subheader("Modify Scene")
        index_list= df_scenes.index
        index=index_list[df_scenes['Scene Name']==selected_scene_name].tolist()[0]
        scene_name = st.text_input(label="Scene Name",value=selected_scene_name)
        setting = st.text_area(label="Setting",value=df_scenes.at[index,'Setting'])
        character_list = st.text_area(label="Character List",value=df_scenes.at[index,'Character List'])
        chaos_factor = st.text_input(label="Chaos Factor",value=df_scenes.at[index,'Chaos Factor'])
        threads = st.text_area(label="Threads",value=df_scenes.at[index,'Threads'])
        Notes = st.text_area(label="Notes",value=df_scenes.at[index,'Notes'],height=500)
        save_updates = st.button("Save to file")
        if save_updates:
            df_scenes.at[index,'Scene Name']=scene_name
            df_scenes.at[index,'Setting']=setting
            df_scenes.at[index,'Character List']= character_list
            df_scenes.at[index,'Chaos Factor']=chaos_factor
            df_scenes.at[index,'Threads']=threads
            df_scenes.at[index,'Notes']=Notes
            df_scenes.to_csv("session/scenes/"+scene_file,index=False)
            st.success('Updated!')
            st.button("Refresh")