print("Bon courage pour la suite")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"importation du dataframe"
victime=pd.read_csv('merged_data.csv', sep=",")


"Traitement des valeurs manquantes"
nan_values = victime.isna().sum()

nan_values = nan_values.sort_values(ascending=True)*100/127951

ax = nan_values.plot(kind='barh', 
                     figsize=(8, 10), 
                     color='#AF7AC5',
                     zorder=2,
                     width=0.85)

ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.tick_params(axis="both", 
               which="both", 
               bottom="off", 
               top="off", 
               labelbottom="on", 
               left="off", 
               right="off", 
               labelleft="on")

vals = ax.get_xticks()

for tick in vals:
  ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

nans = ['v1','v2','lartpc',
       'larrout','locp','etatp',
       'actp','voie','pr1',
       'pr','place']

victime = victime.drop(columns = nans)
victime = victime.dropna()

victime.to_csv("step2/missing_values_deleted.csv", index=False)