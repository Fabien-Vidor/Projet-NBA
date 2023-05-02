import streamlit as st
import pandas as pd

title = "Qui sommes-nous ?"
sidebar_name = "Qui sommes-nous ?"

def run():
    st.title(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Leo Ferretti", "Florian Lluch", "Alex Randrianantoandro", "Fabien Vidor"])
    with tab1:
        st.header("Leo Ferretti")
        st.markdown("""
                    """)
    with tab2:
        st.header("Florian Lluch")
        st.markdown(
            """
               
            """
        )
   

    with tab3:
        st.header("Alex Randrianantoandro")
        st.markdown(
            """
               
            """
        )
   
   
    with tab4:
        st.header("Fabien Vidor")
        st.markdown(
            """
               
            """
        )
   