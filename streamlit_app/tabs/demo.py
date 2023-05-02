import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from joblib import load


title = "Démo"
sidebar_name = "Démo"
rf = load('../data/saved_model.joblib')
data_dict = {'Last Minute':[0],'W_PCT_2': [0],'Damian Lillard':[0],'LeBron James': [0],'Kevin Durant': [0],'Chris Paul': [0],'Russell Westbrook': [0],'James Harden': [0],'Anthony Davis': [0],'Giannis Antetokounmpo': [0],'Kawhi Leonard': [0],'Stephen Curry': [0],'Shot Distance': [0],'Shot Difficulty': [0]}
df_tx_reussite = pd.read_csv("../data/df_tx_reussite_distance.csv")

def run():

    st.image("assets/intro_white.gif", use_column_width='auto', width=900)

    st.title(title)

    st.write("Choisissez les variables :")

    shot_distance = st.slider("Distance du tir", max_value=35)

    with st.form("modélisation"):

        # Sélection du joueur 
        player = st.selectbox(
            'Choisissez le joueur',
            ('James Harden', 'LeBron James', 'Chris Paul', 'Kevin Durant', 'Russell Westbrook', 'Stephen Curry', 'Kawhi Leonard', 'Anthony Davis', 'Damian Lillard', 'Giannis Antetokounmpo'))

        type_de_tir = st.selectbox("Choisissez le type de tir",list(df_tx_reussite.loc[df_tx_reussite["Distance max"]>=shot_distance]["Action Type"]))
        # Création des variables nécessaires
        W_PCT = st.slider("Pourcentage de victoires de l'équipe adverse",min_value = 0.0,max_value = 1.0)
        last_minute = st.checkbox("Dernière minute")
        shot_difficulty = df_tx_reussite.loc[df_tx_reussite["Action Type"] == type_de_tir]["Note"]

        # Every form must have a submit button.
        submitted = st.form_submit_button("Envoyer")
        if submitted:

            # Création du DataFrame
            df_dict = pd.DataFrame.from_dict(data_dict)

            # Ajout des paramètres
            df_dict.loc[0, 'Last Minute'] = 1 if last_minute == True else 0
            df_dict.loc[0, player] = 1
            df_dict.loc[0, 'Shot Difficulty'] = shot_difficulty.values[0]   
            df_dict.loc[0, 'Shot Distance'] = shot_distance 
            df_dict.loc[0,"W_PCT_2"] = W_PCT

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
            
            # Ajout du gif si réussi
            if pred == 1:
                st.image("assets/lebron.gif",use_column_width=True)



