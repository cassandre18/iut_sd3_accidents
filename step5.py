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

victime=pd.read_csv('C:/Users/cassa/Desktop/github_iut/iut_sd3_accidents/step4/gps_encoding.csv', sep=",")


y = victime['grav']

features = ['catu','sexe','trajet','secu',
            'catv','an_nais','mois',
            'occutc','obs','obsm','choc','manv',
            'lum','agg','int','atm','col','gps',
            'catr','circ','vosp','prof','plan',
            'surf','infra','situ','hrmn','geo']

X_train_data = pd.get_dummies(victime[features].astype(str))

X_train_data['grav']=y

X_train_data.to_csv("step5/one_hot_encoding.csv", index=False)