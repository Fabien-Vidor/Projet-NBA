import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from joblib import load

title = "Modélisation"
sidebar_name = "Modélisation"


def run():

    

    st.title(title)
    st.header("Random Forest")

    st.markdown(
        """
        Voici le rapport de classification :        
        """
    )

    with st.expander("Rapport de classification du modèle"):
        st.image("assets/classification_report.png", use_column_width='auto', width=600)
    
    

    
    st.markdown(
        """

        En regardant l'importance des différentes features, on voit que la variable 'Shot Difficulty' est importante à 80%.
        En revanche, comme les arbres de décision cherchent à gagner de l'information à chaque étape, les shoots jugés 'difficiles' 
        (Shot Difficulty = 0) sont tous classés en shoot manqués alors qu'ils sont en réalité réussis à environ 32%. 
        A contrario, les shoots jugés faciles sont tous classés en réussis.
         
        """
    )
    with st.expander("Importance des variables dans l'arbre de décision"):
        st.image("assets/Importance_var.png", use_column_width='auto', width=600)
        
    st.markdown(
        """

        Cela vient du fait qu'en séparant de cette manière à chaque noeud, l'arbre gagne beaucoup d'information. 
        Cela peut également expliquer qu'une random forest n'a pas de meilleurs résultats. 
        La répartition est tellement évidente pour l'arbre de décision que chacun des arbres de la forêt a une répartition 
        similaire aux autres, peu importe l'ensemble de données sur lequel il s'entraîne.
         
        """
    )
    
    with st.expander("Pourcentage de réussite en fonction de la difficulté du tir"):
        st.image("assets/pred_by_diff_rf.png", use_column_width='auto', width=600)
    
    st.markdown(
        """
        On observe qu'étant donné que la majorité des tirs se trouvent dans la Shot Difficulty 0 (environ 40%), 
        en les classifiant tous en tirs manqués notre algorithme augmente son accuracy 
        mais comme en réalité 32% d'entre eux sont réussis, cela fait chuter le rappel de la classe 1. 
        On observe également qu'au-delà d'une certaine note, il classifie tous les tirs en réussis malgré 
        le fait que certains d'entre eux sont ratés.

        
        """
    )

