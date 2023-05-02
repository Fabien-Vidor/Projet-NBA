import streamlit as st
import pandas as pd
import config

title = "Qui sommes-nous ?"
sidebar_name = "Qui sommes-nous ?"

def run():
    st.title(title)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Leo Ferretti", "Florian Lluch", "Alex Randrianantoandro", "Fabien Vidor"])
    with tab1:
        
        st.markdown("""A 23 ans et après un master 1 en mathématiques, je me forme actuellement en data science.
                    """)
        st.write(config.TEAM_MEMBERS[0].presentation_markdown(), unsafe_allow_html=True)

    with tab2:
        
        st.markdown(
            """Après une Licence en économie et un Master en école de commerce (Kedge Business School) je me suis tourné vers la en DataScience.
               
            """
        )
        st.write(config.TEAM_MEMBERS[1].presentation_markdown(), unsafe_allow_html=True)
        

    with tab3:
        
        
        st.markdown(
            """
            Après avoir obtenu ma license lors de ma reconversion en tant que Concepteur Développeur d'applications, j'ai fait ma première expérience de 2 ans dans une entreprise de Data.
            Polyvalent, j'ai occupé le poste de développeur, d'administrateur système et j'ai découvert le poste de Data Analyst, c'est pour cela
            qu'aujourd'hui je continue ma formation en me formant pour être Data Scientist.
            """
        )
        st.write(config.TEAM_MEMBERS[2].presentation_markdown(), unsafe_allow_html=True)
   
        
   
    with tab4:
        
        
        st.markdown(
            """
            De formation mathématique (licence en mathématiques option informatique) j'ai ensuite fait carrière à l'Armée de Terre en tant que sous-officier.
            Je reviens dorénavant vers mon ancien domaine en me formant en data science.
            """
        )
        st.write(config.TEAM_MEMBERS[3].presentation_markdown(), unsafe_allow_html=True)
   