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
print(In_sigma)
# print(In_sigma[0])

# mu=Out_obs.mean()
# print('mu=',mu)
# std=Out_obs.std()
# print('std=',std)

R2={'(20,20)': 0.020493378522805344, '(20,30)': 0.023029126028763933, '(20,40)': 0.02502945780102113, '(20,50)': 0.026661722552504957, '(20,60)': 0.02816119286552478, '(20,70)': 0.029690996555244202, '(30,20)': 0.02130064564210243, '(30,30)': 0.023908596445894666, '(30,40)': 0.025703454883541935, '(30,50)': 0.02717970139086203, '(30,60)': 0.02862923335015858, '(30,70)': 0.030175873765680438, '(40,20)': 0.02100632438513153, '(40,30)': 0.024199802245254354, '(40,40)': 0.02602029706083793, '(40,50)': 0.02748518829898616, '(40,60)': 0.028983086285451466, '(40,70)': 0.030606913891138583, '(50,20)': 0.020035247206178806, '(50,30)': 0.023826967927982865, '(50,40)': 0.025904326652941585, '(50,50)': 0.027544358607279138, '(50,60)': 0.029211003292132425, '(50,70)': 0.030980371176082804, '(60,20)': 0.018830420777600325, '(60,30)': 0.0228284862979215, '(60,40)': 0.02533249524090843, '(60,50)': 0.027346777021324008, '(60,60)': 0.029311341169270894, '(60,70)': 0.031296506151281316, '(70,20)': 0.017484191332461173, '(70,30)': 0.021338472366831694, '(70,40)': 0.02435615969763139, '(70,50)': 0.026915291063018144, '(70,60)': 0.02929591480989125, '(70,70)': 0.031560592485337685}
max_value = max(R2, key=R2.get)
print(max_value)
mu=70
std=70

def TTD(mu, std, taw):
    TTD_value=(1/(std*np.sqrt(2*np.pi)))*np.exp(-0.5*((7*taw-mu)/std)**2)
    return TTD_value

# ttd=[]
# for taw in range(0,index,1):
#     ttd.append(TTD(mu, std, taw))
# print(ttd)

C_simu={}
for t in range(0,index,1):
    out_simu = 0
    for taw in range(0,t+1,1):
        out_simu+= TTD(mu,std,taw)*In_sigma[t-taw]
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

# plt.plot(observation_list,'r')
plt.figure()
plt.plot(df_original['Cl mg/l'].to_numpy(),'g', label="Observation")
plt.plot(simulation_list,'b', label="Simulation")
plt.margins(x=0, y=0)
plt.title("Chloride Prediction with Normal Distribution TTD",size=18)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.ylabel("Chloride Concentration (mg/l)",size=18)
plt.xlabel("time step (7hr)",size=18)
plt.legend(fontsize=20)
plt.grid()
plt.show()
