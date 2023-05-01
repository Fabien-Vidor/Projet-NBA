import streamlit as st
import pandas as pd

title = "Préparation des données"
sidebar_name = "Préparation des données"

code1='''# Cette fonction associe à chaque shot l'équipe adverse du shooter.
def adversaire(df):
    adv = []
    new_df = df[['Team Name','Home Team','Away Team']]
    for a in new_df.values:
        if a[0] == a[1]:
            adv.append(a[2])
        else:
            adv.append(a[1])
    return adv

def creation_pourcentage_adversaire(df,rank):
    # On remplace le nom des équipes de la colonne Team Name par leur code en 3 lettres
    new_df = df.replace(to_replace = ['New Orleans Hornets', 'Oklahoma City Thunder',
       'Golden State Warriors', 'Cleveland Cavaliers', 'Miami Heat',
       'Los Angeles Clippers', 'San Antonio Spurs', 'Houston Rockets',
       'Portland Trail Blazers', 'New Orleans Pelicans',
       'Milwaukee Bucks', 'LA Clippers', 'Toronto Raptors','New Orleans/Oklahoma City Hornets',
       'Los Angeles Lakers','Seattle SuperSonics'],
           value = ['NOP', 'OKC','GSW','CLE','MIA','LAC','SAS','HOU','POR','NOP','MIL','LAC','TOR','NOK','LAL','SEA'])
    # On applique la fonction adversaire qui crée une colonne avec l'équipe adverse pour chaque shoot.
    new_df['Adversaire'] = adversaire(new_df)
    # On remplace les noms de la colonne TEAM de ranking pour que cela corresponde avec les valeurs de la colonne 'Adversaire'.
    new_rank=rank.replace(to_replace = ['Denver', 'Memphis', 'New Orleans', 'Phoenix', 'LA Clippers',
       'Sacramento', 'Utah', 'Portland', 'Dallas', 'Minnesota',
       'Golden State', 'Oklahoma City', 'L.A. Lakers', 'San Antonio',
       'Houston', 'Milwaukee', 'Boston', 'Cleveland', 'Brooklyn',
       'Philadelphia', 'New York', 'Atlanta', 'Indiana', 'Miami',
       'Toronto', 'Chicago', 'Orlando', 'Washington', 'Charlotte',
       'Detroit', 'L.A. Clippers','New Jersey','Seattle', 'New Orleans/Oklahoma City',], 
                          value = ['DEN','MEM','NOP','PHX','LAC','SAC','UTA','POR',
                                                          'DAL','MIN','GSW','OKC','LAL','SAS','HOU','MIL',
                                                          'BOS','CLE','BKN','PHI','NYK','ATL','IND','MIA',
                                                          'TOR','CHI','ORL','WAS','CHA','DET','LAC','NJN','SEA','NOK'])
    # On joint les 2 dataframe sur la date et l'équipe adverse par une jointure gauche pour conserver tous les shoots.
    final_df = new_df.merge(new_rank,how = 'left',right_on = ['STANDINGSDATE','TEAM'],left_on = ['Game Date','Adversaire'])
    # On applique une correction à la colonne pourcentage de victoire pour gérer les valeurs extrêmes du début de saison
    final_df['W_PCT_2'] = [a if a>0.2 else final_df['W_PCT'].mean() for a in final_df['W_PCT']]
    # On enlève la colonne avec beaucoup de NaN et l'ancienne colonne 'W_PCT'
    final_df = final_df.drop(['RETURNTOPLAY','W_PCT'],axis = 1)
    return final_df'''


code2='''# On crée une fonction qui prend en entrée un type d'action 'a' et retourne le taux de réussite associé.
def find_val(df_tx_reussite,a):
    return df_tx_reussite.loc[df_tx_reussite['Action Type'] == a]['Shot Made Flag'].values[0]

# On crée une fonction qui à une valeur de taux de réussite donnée associe sa note
def find_n(val,liste):
    n = 0
    for i in liste:
        if val >= i:
            n+=1
    return n

# Cette fonction crée la colonne difficulté. Pour cela, elle prend en entrée un entier n, elle parcourt toutes les lignes de 
# notre DataFrame. Pour chaque ligne elle récupère le taux de réussite de l'Action Type et lui associe sa note.
def categ(df_tx_reussite,df,n):
    quantile = list(df_tx_reussite['Shot Made Flag'].quantile(np.linspace(1/n,1,n)))
    cat = []
    for a in df['Action Type']:
        val = find_n(find_val(df_tx_reussite,a),quantile)
        cat.append(val)
    return cat

# Création de la variable shot_difficulty
def shot_difficulty(df,n,data):
    # On crée la DataFrame qui à chaque type de shoot associe le taux de réussite. (70 types de shoot)
    df_tx_reussite = pd.DataFrame(data.groupby('Action Type')['Shot Made Flag'].mean().reset_index())
    # On trouve les quantiles d'ordre n pour ces 70 valeurs.
    quantile = list(df_tx_reussite['Shot Made Flag'].quantile(np.linspace(1/n,1,n)))
    difficulty = categ(df_tx_reussite,df,n)
    df['Shot Difficulty'] = difficulty
    df = df.drop(['Action Type'],axis=1)
    return df'''


code3='''    last_minute = [1 if a == 0 else 0 for a in final_df["Minutes Remaining"]]
    final_df['Last Minute'] = last_minute'''

code4='''def get_dummies(df,colonne):
    # Cette fonction sert juste à rendre le get_dummies plus rapide
    dummies = pd.get_dummies(df[colonne])
    new_df = pd.concat([df,dummies],axis=1)
    new_df=new_df.drop([colonne],axis=1)
    return new_df

final_df = get_dummies(new_df,'Player Name')'''

code5='''def get_dummies(df,colonne):
    # Cette fonction sert juste à rendre le get_dummies plus rapide
    dummies = pd.get_dummies(df[colonne])
    new_df = pd.concat([df,dummies],axis=1)
    new_df=new_df.drop([cofrom sklearn.model_selection import train_test_split
def final_df(df,rank,n,annee):
    # On prépare la DataFrame "NBA Shot Locations 1997 - 2020"
    shot_loc = preparation_shot_location(df,annee)
    # On prépare la DataFrame "Ranking"
    ranking = preparation_ranking(rank,annee)
    # On crée le pourcentage de l'équipe adverse
    new_df = creation_pourcentage_adversaire(shot_loc,ranking)
    # On crée les variables joueurs à l'aide d'un get_dummies
    final_df = get_dummies(new_df,'Player Name')
    # On crée la variable "Last Minute" à l'aide de la colonne "Minutes Remaining"
    last_minute = [1 if a == 0 else 0 for a in final_df["Minutes Remaining"]]
    final_df['Last Minute'] = last_minute
    # On choisit les colonnes qui nous intéresse
    dff = final_df.loc[:,['Last Minute','Action Type','W_PCT_2','Shot Made Flag','Damian Lillard','LeBron James',
                         'Kevin Durant','Chris Paul','Russell Westbrook','James Harden','Anthony Davis','Giannis Antetokounmpo',
                         'Kawhi Leonard','Stephen Curry','Shot Distance']]
    # On sépare en jeu de test et jeu d'entraînement
    target = dff['Shot Made Flag']
    data_train,data_test,y_train,y_test = train_test_split(dff,target,random_state=10,test_size=0.2)
    # On crée la variable "Shot Difficulty" calibrés sur les données de X_train et appliqués à X_test et X_train
    X_train = shot_difficulty(data_train,n,data_train)
    X_test = shot_difficulty(data_test,n,data_train)
    X_train = X_train.drop(["Shot Made Flag"],axis=1)
    X_test = X_test.drop(["Shot Made Flag"],axis=1)
    return X_train,X_test,y_train,y_testlonne],axis=1)
    return new_df

final_df = get_dummies(new_df,'Player Name')'''

def run():

    st.title(title)

    st.markdown(
        """

        ### :orange[Pourcentage de victoire de l'équipe adverse]
        Comme vu dans la partie d’exploration, on observe une baisse de réussite au tir lorsque
        l’équipe adverse du tireur a un haut taux de pourcentage de victoires. C’est pourquoi nous avons créé
        une variable qui donne le pourcentage de victoires de l’équipe adverse du tireur.
        Cela a été possible grâce à la DataFrame ranking qui à une date donnée, pour une équipe donnée,
        nous donne le pourcentage de victoires et le classement
        """
    )
    with st.expander("Afficher le code"):
        st.code(code1, language="python")

    st.markdown(
        """
        ### :orange[Difficulté du tir]

        Ce la partie « Taux de réussite en fonction de la variable « Action Type » », nous avons vu
        que la type d’action a une influence sur le taux de réussite de ce dernier. Ce qui n’est pas étonnant
        puisque même intuitivement, un dunk par exemple est beaucoup plus souvent réussi que raté tandis
        que c’est plutôt l’inverse pour un Jump Shot classique. Il était donc important de rendre le plus
        exploitable possible l’information contenue dans la variable « Action Type ». C’est une variable
        catégorielle avec plus de 70 valeurs distinctes, ce qui nous est paru être trop pour faire un simple One
        Hot Encoder.
        Nous avons décidé de regrouper les types en n catégories, où 0 correspond à un tir compliqué et n à
        un tir très simple. Cela permet à l’algorithme de considérer la variable ainsi créée comme une
        variable continue.jeu de données contient le classement NBA entre 2003 et 2020. À une date donnée, nous
        pouvons en extraire le classement et le pourcentage de victoire de chaque équipe sur la saison en
        cours. Ce jeu de données nous sera utile dans la suite.
        """
    )

    with st.expander("Afficher le code"):
        st.code(code2, language="python")

    st.markdown(
        """
        ### :orange[Dernière minute]

        Dans l’exploration de données, nous avons observé que les tirs ayant lieu dans la dernière
        minute sous plus souvent ratés que durant les 11 autres minutes d’un quart-temps. Nous avons donc
        créé une variable binaire appelée « Last Minute » en utilisant simplement la variable « Minutes
        Remaining » de la DataFrame « NBA Shot Locations 1997 – 2020 ».
        """
    )

    with st.expander("Afficher le code"):
        st.code(code3, language="python")

    st.markdown(
        """
        ### :orange[Catégoriser la variable des joueurs]

        Comme les joueurs doivent être une variable de notre algorithme, nous avons effectué un
        simple Get Dummies sur la variable « Player Name » afin d’avoir des variables binaires.
        """
    )

    with st.expander("Afficher le code"):
        st.code(code4, language="python")

    st.markdown(
        """
        ### :orange[Fonction finale]

        Enfin, la dernière étape de la préparation des données consiste en l’agrégation des étapes
        précédentes, puis sélectionner les colonnes à garder. Comme précisé dans la partie « Difficulté du
        tir », la notation de la difficulté du tir s’effectue après la séparation en jeu de test et d’entraînement,
        cela afin que le jeu de test soit calibré uniquement sur les données d’entraînement et pas sur toutes
        les données.
        """
    )

    with st.expander("Afficher le code"):
        st.code(code5, language="python")
