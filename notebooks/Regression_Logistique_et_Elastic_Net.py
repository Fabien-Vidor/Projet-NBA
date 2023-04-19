#!/usr/bin/env python
# coding: utf-8

# Nous avons téléchargé nos jeux d'entraînement et de test sous forme de csv afin de les récupérer directement sans avoir à relancer tout le preprocessing. Les paramètres choisies sont l'année 2010, 20 notes possibles pour la difficulté.

# In[7]:


import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
X_train = pd.read_csv("X_train.csv",index_col = 0)
X_test = pd.read_csv("X_test.csv",index_col = 0)
y_train = pd.read_csv("y_train.csv",index_col= 0)
y_test = pd.read_csv("y_test.csv",index_col = 0)


# ## Arbre de décision



# In[9]:


from sklearn import linear_model
clf = linear_model.LogisticRegression(C=0.1, solver = 'lbfgs')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test) 
print(classification_report(y_test, y_pred))


# ## ElasticNet


# In[11]:


from sklearn.ensemble import RandomForestClassifier
scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model_en = ElasticNetCV(cv=8, l1_ratio=(0.1, 0.25, 0.5, 0.7, 0.75, 0.8, 0.85, 0.9, 0.99), 
                        alphas=(0.001, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 0.8, 1.0))

model_en.fit(X_train, y_train)
pred_train = model_en.predict(X_train)
pred_test = model_en.predict(X_test)
print('score train :', model_en.score(X_train, y_train))
print('score test :', model_en.score(X_test, y_test))
pred = pred_test > 0.5
print(classification_report(y_test, pred))


