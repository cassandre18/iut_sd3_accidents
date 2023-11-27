import pandas as pd
carac=pd.read_csv('c:\Users\cassa\Desktop\github_iut\iut_sd3_accidents\data\carac.csv', encoding='latin1')
lieux=pd.read_csv('c:\Users\cassa\Desktop\github_iut\iut_sd3_accidents\data\data/lieux.csv' , encoding='latin1')
veh=pd.read_csv('c:\Users\cassa\Desktop\github_iut\iut_sd3_accidents\data\data/veh.csv' , encoding='latin1')
vict=pd.read_csv('c:\Users\cassa\Desktop\github_iut\iut_sd3_accidents\data\data/carac.csv' , encoding='latin1')

data=pd.merge(carac,lieux,on='Num_Acc', how='inner')
data=pd.merge(data,veh,on='Num_Acc', how='inner')
data=pd.merge(data,vict,on='Num_Acc', how='inner')

data.to_csv(data.csv,index=False, encoding='utf-8')

print("Fusion terminéé, le fichier data.csv à été crée.")