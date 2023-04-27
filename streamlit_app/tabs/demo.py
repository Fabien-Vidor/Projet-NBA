import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from joblib import load


title = "Démo"
sidebar_name = "Démo"
rf = load('../data/saved_model.joblib')
data_dict = {'Last Minute':[0],'W_PCT_2': [0],'Damian Lillard':[0],'LeBron James': [0],'Kevin Durant': [0],'Chris Paul': [0],'Russell Westbrook': [0],'James Harden': [0],'Anthony Davis': [0],'Giannis Antetokounmpo': [0],'Kawhi Leonard': [0],'Stephen Curry': [0],'Shot Distance': [0],'Shot Difficulty': [0]}

def run():

    st.title(title)

    with st.form("modélisation"):
        st.write("Choisissez les variables :")

        # Sélection du joueur 
        player = st.selectbox(
            'Choisissez le joueur',
            ('James Harden', 'LeBron James', 'Chris Paul', 'Kevin Durant', 'Russell Westbrook', 'Stephen Curry', 'Kawhi Leonard', 'Anthony Davis', 'Damian Lillard', 'Giannis Antetokounmpo'))

        # Création des variables nécessaires
        shot_difficulty = st.slider("Difficulté du tir", max_value=4)
        shot_distance = st.slider("Distance du tir", max_value=35)
        last_minute = st.checkbox("Dernière minute")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Envoyer")
        if submitted:

            # Création du DataFrame
            df_dict = pd.DataFrame.from_dict(data_dict)

            # Ajout des paramètres
            df_dict.loc[0, 'Last Minute'] = 1 if last_minute == True else 0
            df_dict.loc[0, player] = 1
            df_dict.loc[0, 'Shot Difficulty'] = shot_difficulty    
            df_dict.loc[0, 'Shot Distance'] = shot_distance 

            # Affichage du DataFrame modifié        
            st.write('Affichage des paramètres')
            st.dataframe(df_dict, use_container_width=True)

            # Prédiction du tir
            pred = rf.predict(df_dict)

            # Affichage du résultat
            st.write('Le tir est', 'réussi' if pred == 1 else 'raté')

            # Ajout du gif si raté
            if pred == 0:
                st.image("assets/rate.gif")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=list("abc"))

    st.line_chart(chart_data)

