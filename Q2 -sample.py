import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df_rainfall=pd.read_excel('AH_HW7_Data_14002_sample.xlsx',sheet_name='Rainfall')
# print(df_rainfall)
df_streamflow=pd.read_excel('AH_HW7_Data_14002_sample.xlsx',sheet_name='Streamflow')
# print(df_streamflow)

############### TTD = normal dist
index=14
In_sigma=df_rainfall['Cl mg/l'][1756:index+1756]
Out_obs=df_streamflow['Cl mg/l'][1756:index+1756]
# print(In_sigma)
# print(In_sigma[0])

mu=Out_obs.mean()*4.5
print('mu=',mu)
std=Out_obs.std()*1000
print('std=',std)

def TTD(mu, std, taw):
    TTD_value=(1/(std*np.sqrt(2*np.pi)))*np.exp(-0.5*((7*taw-mu)/std)**2)
    return TTD_value
print('TTD0=',TTD(mu,std,0))
print('TTD1=',TTD(mu,std,1))
print('TTD2=',TTD(mu,std,2))
print('TTD3=',TTD(mu,std,3))
print('TTD4=',TTD(mu,std,4))

# def Out_sigma(mu,std,t):
#     out=0
#     for taw in range(0,t+1,1):
#         out+= TTD(mu,std,taw)*In_sigma[t-taw]
#     return out
#
# for t in range(0,4+1,1):
#     print(Out_sigma(mu,std,t))


C_simu={}
for t in range(0,index,1):
    out_simu = 0
    for taw in range(0,t+1,1):
        out_simu+= TTD(mu,std,taw)*In_sigma[t-taw]
    C_simu[t]=[out_simu,Out_obs[t]]
print('simu & obs concentraition=',C_simu)

### NORMAL DIST CALIBRATION
# R2={}
# simulations_list=[]
# observation_list=[]
# for t in range(0,index,1):
#     simulations_list.append(C_simu[t][0])
#     observation_list.append(C_simu[t][1])
#     R2[t]=r2_score( observation_list,simulations_list)
# print('simu=',simulations_list)
# print('obs=',observation_list)
# print('R squared=',R2)


R2={}
simulations_list=[]
observation_list=[]
for t in range(0,index,1):
    simulations_list.append(C_simu[t][0])
    observation_list.append(C_simu[t][1])
    corr_matrix = np.corrcoef(observation_list, simulations_list)
    corr = corr_matrix[0, 1]
    R_sq = corr ** 2
    R2[t]=R_sq
print('simu=',simulations_list)
print('obs=',observation_list)
print('R squared=',R2)