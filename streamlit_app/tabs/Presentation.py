import streamlit as st
import pandas as pd
import config

title = "Qui sommes-nous ?"
sidebar_name = "Qui sommes-nous ?"

def run():
    st.title(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Leo Ferretti", "Florian Lluch", "Alex Randrianantoandro", "Fabien Vidor"])
    with tab1:
        st.header("Contact :")
        st.write(config.TEAM_MEMBERS[0].presentation_markdown(), unsafe_allow_html=True)
        st.markdown("""
                    """)

    with tab2:
        st.header("Contact :")
        st.write(config.TEAM_MEMBERS[1].presentation_markdown(), unsafe_allow_html=True)
        st.markdown(
            """
               
            """
        )
        

    with tab3:
        st.header("Contact :")
        st.write(config.TEAM_MEMBERS[2].presentation_markdown(), unsafe_allow_html=True)
        
        st.markdown(
            """
               
            """
        )
   
        
   
    with tab4:
        st.header("Contact :")
        st.write(config.TEAM_MEMBERS[3].presentation_markdown(), unsafe_allow_html=True)
        
        st.markdown(
            """
            De formation mathématiques (licence en mathématiques option informatique) j'ai ensuite fait carrière à l'Armée de Terre en tant que sous-officier.
            Je reviens dorénavant vers mon ancien domaine en me formant en data science.
            """
        )
        st.markdown(
            """
            
            """
        )
   