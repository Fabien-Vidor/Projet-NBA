import streamlit as st
import pandas as pd
from member import Member

title = "Qui sommes-nous ?"
sidebar_name = "Qui sommes-nous ?"

def run():
    st.title(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Leo Ferretti", "Florian Lluch", "Alex Randrianantoandro", "Fabien Vidor"])
    with tab1:
        st.markdown("""
                    """)
        
    with tab2:
        st.markdown(
            """
               
            """
        )
        
   

    with tab3:
        st.markdown(
            """
               
            """
        )
   
   
    with tab4:
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
   