import streamlit as st


title = "Projet NBA"
sidebar_name = "Introduction"


def run():

    # TODO: choose between one of these GIFs
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.image("assets/intro.gif")
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")

    st.title(title)

    st.markdown("---")

    st.markdown(
        """
                Dans le cadre de notre formation en Data science chez Data Scientest, nous avons travaillé sur
        un projet nécessitant une solution de machine learning. Notre projet a pour objectif de prédire l’issue
        des tirs de 10 des meilleurs joueurs actifs en NBA. Nous avions la consigne de n’avoir qu’un seul
        algorithme final où le joueur serait une variable.
        Comme toutes les ligues des sports populaires américains, la NBA donne une grande
        importance à la donnée. Cela nous a permis d’avoir accès à des données pertinentes. Certaines
        étaient déjà exploitables, tandis que d’autres ont nécessité des étapes de preprocessing que nous
        détaillerons dans la suite. Cependant, le basketball étant un jeu de précision, prédire l’issue d’un tir
        reste une tâche très compliquée. En effet, deux tirs qui sont à première vue identiques peuvent avoir
        une issue différente pour des raisons inconnues même pour des experts du sujet. Il suffit de voir par
        exemple le concours de tirs à 3 points pour comprendre ce problème. Parallèlement à cela, des
        facteurs exerçant une influence non négligeable sur l’issue du tir comme par exemple la fatigue, la
        pression défensive, l’importance plus ou moins grande du tir ou encore l’état de forme du joueur ne
        sont parfois pas quantifiables ou partiellement voire complètement inaccessible.
        Dans la suite, nous aurons dans un premier temps une étape d’exploration de données où des
        graphes montreront les tendances que nous avons tiré des données qui nous étaient accessibles. Cela
        sera suivie des étapes de preprocessing, où nous traduirons les tendances captées en des données
        exploitables pour des algorithmes de machine learning. Troisièmement, nous présenterons l’étape de
        modélisation où nous avons testé et analysé les résultats de différents algorithmes, d’abord basiques
        puis plus poussés. Enfin, nous conclurons par une analyse de notre travail et les axes d’amélioration à
        explorer.
        """
    )
