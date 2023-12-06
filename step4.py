import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import normalize

from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import recall_score, f1_score

victime=pd.read_csv('C:/Users/cassa/Desktop/github_iut/iut_sd3_accidents/step3/time_encoding.csv', sep=",")

# On extrait du tableau la latitude et la longitude

X_lat = victime['lat']
X_long = victime['long']

# On définit tous nos points à classifier

X_cluster = np.array((list(zip(X_lat, X_long))))

# Kmeans nous donne pour chaque point la catégorie associée

clustering = KMeans(n_clusters=15, random_state=0)
clustering.fit(X_cluster)

# Enfin on ajoute les catégories dans la base d'entraînement

geo = pd.Series(clustering.labels_)

victime['geo'] = geo

victime.to_csv("step4/gps_encoding.csv", index=False)