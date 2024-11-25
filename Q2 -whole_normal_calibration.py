import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df_original=pd.read_excel('AH_HW7_Data_14002_original.xlsx',sheet_name='Streamflow')
df_rainfall=pd.read_excel('AH_HW7_Data_14002_basefr.xlsx',sheet_name='Rainfall')
# print(df_rainfall)
df_streamflow=pd.read_excel('AH_HW7_Data_14002_basefr.xlsx',sheet_name='Streamflow')
# print(df_streamflow)


############### TTD = normal dist
index=2375
In_sigma=df_rainfall['Cl mg/l']
Out_obs=df_streamflow['Cl mg/l']
# print(In_sigma)
# print(In_sigma[0])

# mu=50
# std=50


def TTD(mu, std, taw):
    TTD_value=(1/(std*np.sqrt(2*np.pi)))*np.exp(-0.5*((7*taw-mu)/std)**2)
    return TTD_value
# print('TTD0=',TTD(mu,std,0))
# print('TTD1=',TTD(mu,std,1))
# print('TTD2=',TTD(mu,std,2))
# print('TTD3=',TTD(mu,std,3))
# print('TTD4=',TTD(mu,std,4))


R2={}
for mu in range(20,70+1,10):
    for std in range(20,70+1,10):
        C_simu={}
        simulation_list = []
        observation_list = []
        for t in range(0,index,1):
            out_simu = 0
            for taw in range(0,t+1,1):
                out_simu+= TTD(mu,std,taw)*In_sigma[t-taw]
            C_simu[t]=[out_simu,Out_obs[t]]
            simulation_list.append(C_simu[t][0])
            observation_list.append(C_simu[t][1])
        corr_matrix = np.corrcoef(observation_list, simulation_list)
        corr = corr_matrix[0, 1]
        R_sq = corr ** 2
        R2[f'({mu},{std})'] = R_sq
print(R2)

