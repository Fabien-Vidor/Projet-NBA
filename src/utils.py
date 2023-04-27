# ## Fonctions utiles

# La première fonction permet de corriger les seuils en fonction de la difficulté au tir, 
# on récupère les prédictions corrigées à partir desquelles on peut observer le classification_report pour voir les différences.
# 
def pred_corr(X_test,y_proba,seuil = (0.5,0.5),lim = 5):
    temp =[(a,b[1]) for a,b in zip(X_test['Shot Difficulty'].reset_index()['Shot Difficulty'],y_proba)]
    y_pred_corr = []
    for b in temp:
        if (b[0]<lim) & (b[1]>seuil[0]):
            y_pred_corr.append(1)
        elif (b[0]>=lim) & (b[1]>seuil[1]):
            y_pred_corr.append(1)
        else:
            y_pred_corr.append(0)
    return y_pred_corr


# Cette fonction permet de visualiser la performance du modèle en fonction de la difficulté au tir.
def performance_by_difficulty(difficulty,model):
    X_difficulty = X_test.loc[X_test["Shot Difficulty"] == difficulty]
    y_proba_diff = model.predict(X_difficulty)
    y_pred_diff = pd.Series([1 if p>0.5 else 0 for p in y_proba_diff])
    y_test_diff = y_test.loc[X_test["Shot Difficulty"] == difficulty]
    print(classification_report(y_test_diff,y_pred_diff))


# Cette fonction permet d'observer la performance par joueur
def player_performance(player,model):
    X_player = X_test.loc[X_test[player] == 1]
    y_proba_player = model.predict(X_player)
    y_pred_player = pd.Series([1 if p>0.5 else 0 for p in y_proba_player])
    y_test_player = y_test.loc[X_test[player] == 1]
    print(classification_report(y_test_player,y_pred_player))


# Cette fonction renvoie le graphique qui nous montre la proportion de tirs réussis prédits et réels en fonction de la "Shot Difficulty"
def pred_by_diff(X_test,y_test,model):
    repart_quant=pd.concat([X_test,y_test],axis=1).groupby("Shot Difficulty")['Shot Made Flag'].mean()
    repart_quant_pred=pd.concat([X_test.reset_index(),pd.Series(model.predict(X_test))],axis=1).groupby('Shot Difficulty')[0].mean()
    plt.bar(x = range(len(X_test["Shot Difficulty"].unique())),height=repart_quant.values,alpha = 0.5,label = "pourcentage réel")
    plt.bar(x = range(len(X_test["Shot Difficulty"].unique())),height=repart_quant_pred.values,alpha=0.5,label = "pourcentage prédit")
    plt.title("Pourcentage de réussite en fonction de la difficulté du tir")
    plt.legend()


# Cette dernière fonction permet de faire un get dummies sur la variable Action Type à la place de créer "Shot Difficulty". On peut utiliser cette fonction pour voir la différence des modèles en fonction du preprocessing choisi sur la variable Action Type
from sklearn.model_selection import train_test_split,GridSearchCV
def final_df_wo_shot_difficulty(df,rank,n,annee):
    shot_loc = preparation_shot_location(df,annee)
    ranking = preparation_ranking(rank,annee)
    new_df = creation_pourcentage_adversaire(shot_loc,ranking)
    final_df = get_dummies(new_df,'Player Name')
    last_minute = [1 if a == 0 else 0 for a in final_df["Minutes Remaining"]]
    final_df['Last Minute'] = last_minute
    dff = final_df.loc[:,['Last Minute','Action Type','W_PCT_2','Shot Made Flag','Damian Lillard','LeBron James',
                         'Kevin Durant','Chris Paul','Russell Westbrook','James Harden','Anthony Davis','Giannis Antetokounmpo',
                         'Kawhi Leonard','Stephen Curry','Shot Distance']]
    dff = get_dummies(dff,"Action Type")
    data = dff.drop(["Shot Made Flag"],axis=1)
    target = dff['Shot Made Flag']
    data_train,data_test,y_train,y_test = train_test_split(data,target,random_state=10,test_size=0.2)
    return data_train,data_test,y_train,y_test

