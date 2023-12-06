import pandas as pd


victime=pd.read_csv('C:/Users/cassa/Desktop/github_iut/iut_sd3_accidents/step2/missing_values_deleted.csv', sep=",")

hrmn=pd.cut(victime['hrmn'],24,labels=[str(i) for i in range(0,24)])

victime['hrmn']=hrmn.values

victime.to_csv("step3/time_encoding.csv", index=False)
