import streamlit as st
import pandas as pd
from src.utils import shot_location


title = "Exploration des données"
sidebar_name = "Exploration des données"

df = pd.read_csv('./../data/df_bokeh.csv')
rank = pd.read_csv('./../data/ranking.csv')

def run():

    st.image("assets/intro_white.gif", use_column_width='auto', width=900)

    st.title(title)
    st.header("Les jeux de données")

    st.markdown(
        """

        ### :orange[NBA Shot Locations 1997 – 2020]
        Ce jeu de données est sans doute le plus important. Il contient tous les tirs de NBA entre la
        saison 1997 et 2020. Il contient 22 colonnes dont notamment le tireur, le type de tir, l’issue du tir, le
        quart-temps, la distance, la location exacte sur le terrain, l’équipe du tireur ou
        encore les minutes et secondes restantes. 
        """
    )
    with st.expander("Afficher 5 lignes du dataframe"):
        st.dataframe(df.sample(5), use_container_width=True)

    st.markdown(
        """
        ### :orange[Ranking]

        Ce jeu de données contient le classement NBA entre 2003 et 2020. À une date donnée, nous
        pouvons en extraire le classement et le pourcentage de victoire de chaque équipe sur la saison en
        cours. Ce jeu de données nous sera utile dans la suite.
        """
    )

    with st.expander("Afficher 5 lignes du dataframe"):
        st.dataframe(rank.sample(5), use_container_width=True)

    st.header("Visualisation des données")
    
    # Ajout du bokeh après sélection du joueur 
    option = st.selectbox(
        'Choisissez le joueur',
        ('James Harden', 'LeBron James', 'Chris Paul', 'Kevin Durant', 'Russell Westbrook', 'Stephen Curry', 'Kawhi Leonard', 'Anthony Davis', 'Damian Lillard', 'Giannis Antetokounmpo'))

    st.write('Vous avez selectionné:', option)    

    p = shot_location(option, df)

    st.bokeh_chart(p, use_container_width=True)

