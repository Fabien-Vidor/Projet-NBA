import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

title = "Exploration des données"
sidebar_name = "Exploration des données"

df = pd.read_csv('./../data/NBA Shot Locations 1997 - 2020.csv')
rank = pd.read_csv('./../data/ranking.csv')

def run():

    st.title(title)

    st.markdown(
        """
        This is your app's second tab. Fill it in `tabs/second_tab.py`.
        You can and probably should rename the file.

        ## NBA Shot Locations 1997 – 2020
        Ce jeu de données est sans doute le plus important. Il contient tous les tirs de NBA entre la
        saison 1997 et 2020. Il contient 22 colonnes dont notamment le tireur, le type de tir, l’issue du tir, le
        quart-temps, la distance, la location exacte sur le terrain, l’équipe du tireur et l’équipe adverse ou
        encore les minutes et secondes restantes. 
        """
    )
    with st.expander("Afficher 5 lignes du dataframe"):
        st.dataframe(df.sample(5), use_container_width=True)

    st.markdown(
        """
        ## Ranking

        Ce jeu de données contient le classement NBA entre 2003 et 2020. À une date donnée, nous
        pouvons en extraire le classement et le pourcentage de victoire de chaque équipe sur la saison en
        cours. Ce jeu de données nous sera utile dans la suite.
        """
    )

    with st.expander("Afficher 5 lignes du dataframe"):
        st.dataframe(rank.sample(5), use_container_width=True)
