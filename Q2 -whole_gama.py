import numpy as np
import pandas as pd
import scipy as sp
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
print(In_sigma)
# print(In_sigma[0])

mu=Out_obs.mean()
print('mu=',mu)

a=3
b=0.07
# f=lambda x:(x**(a-1))*np.exp(-x)
# gama=sp.integrate.quad(f, 0, np.inf)
# print(gama[0])
def TTD(a,b,taw):
    f=lambda x:(x**(a-1))*np.exp(-x)
    gama=sp.integrate.quad(f, 0, np.inf)
    TTD_value=((b**a)/gama[0])*((7*taw)**(a-1))*np.exp(-b*7*taw)
    return TTD_value
# ttd=[]
# for taw in range(0,index,1):
#     ttd.append(TTD(a,b,taw))
# print(ttd)


C_simu={}
for t in range(0,index,1):
    print(t)
    out_simu = 0
    for taw in range(0,t+1,1):
        out_simu+= TTD(a,b,taw)*In_sigma[t-taw]
    C_simu[t]=[out_simu,Out_obs[t]]
print('simu & obs concentraition=',C_simu)

### NORMAL DIST CALIBRATION

simulation_list=[]
observation_list=[]
for t in range(0,index,1):
    simulation_list.append(C_simu[t][0])
    observation_list.append(C_simu[t][1])
corr_matrix = np.corrcoef(observation_list, simulation_list)
corr = corr_matrix[0, 1]
R_sq = corr ** 2
print('simu=',simulation_list)
print('obs=',observation_list)
print('R squared=',R_sq)

plt.figure()
plt.plot(simulation_list,'b', label="Simulation")
plt.plot(df_original['Cl mg/l'].to_numpy(),'g', label="Observation")
plt.margins(x=0, y=0)
plt.title("Chloride Prediction with Gama Distribution TTD",size=18)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.ylabel("Chloride Concentration (mg/l)",size=18)
plt.xlabel("time step (7hr)",size=18)
plt.legend(fontsize=20)
plt.grid()
plt.show()
