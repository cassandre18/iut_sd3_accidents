import pandas as pd

carac=pd.read_csv('c:/Users/cassa/Desktop/github_iut/iut_sd3_accidents/data/carac.csv', sep=";")
lieux=pd.read_csv('c:/Users/cassa/Desktop/github_iut/iut_sd3_accidents/data/lieux.csv' , sep=";", low_memory=False)
veh=pd.read_csv('c:/Users/cassa/Desktop/github_iut/iut_sd3_accidents/data/veh.csv' ,sep=";")
vict=pd.read_csv('c:/Users/cassa/Desktop/github_iut/iut_sd3_accidents/data/vict.csv' , sep=";")

victime = vict.merge(veh, on=['Num_Acc','num_veh'])
accident = carac.merge(lieux, on="Num_Acc")
victime = victime.merge(accident, on="Num_Acc")

victime.to_csv("merged_data.csv", index=False)

print("Fusion terminéé, le fichier data.csv à été crée.")