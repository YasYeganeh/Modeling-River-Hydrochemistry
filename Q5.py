import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_rainfall=pd.read_excel('AH_HW7_Data_14002_basefr.xlsx',sheet_name='Rainfall')
# print(df_rainfall)
df_streamflow=pd.read_excel('AH_HW7_Data_14002_basefr.xlsx',sheet_name='Streamflow')
# print(df_streamflow)

############### MOHASEBE Ui
U=[0.06818114333333333, 0.23478078506944447, 0.15746091716290506, 0.0977051044379642, 0.08627980152220611, 0.0751523912668459, 0.06984104049785418, 0.061108593702832115, 0.059782476365797727, 0.05611594751401964]
# print(sum(U))
M = len(U)
print('M',M)
N = 2375 #83
print('N',N)
# N=20
n_max= N - M + 1 #79
n_max=2375
print('nmax',n_max)
C_in=df_rainfall[['Cl mg/l']].to_numpy()
obs=df_streamflow[['Cl mg/l']].to_numpy()
# print(C_out.shape)
# print(C_out)

U_matrix=np.zeros([N,n_max])
for n in range(0,N,1): # n namayande radife matrix hastv dar vaghe az n tooye formoola yeki kma==amtare bekhatere index python
    # print(n)
    if n+1 <= M:
        zeros=[0 for _ in range(n_max-(n+1))]
        List_Ui = U[0:n+1]
        Ui_n=[ele for ele in reversed(List_Ui)]
        U_row=Ui_n+zeros
        U_matrix[n]=U_row
    # print(zeros)
    # print(Ui_n)
    # print(Ui_n+zeros)
# print(U_matrix)

U_matrix[0:,1:]=0
# print(U_matrix)

# vector=U_matrix[:,[0]]
vector=U_matrix[:,0]
# print(vector)
# print(vector.shape)

Matrix_p=np.tile(vector, (n_max, 1))
Matrix=Matrix_p.transpose()
# print(Matrix)

c=0
for col in range(0,n_max,1):
    Matrix[:, col] = np.roll(Matrix[:, col], c)
    if col>0:
        Matrix[:c, col] = 0
    c += 1
print(Matrix)
print(Matrix.shape)
print(C_in.shape)

################ MOHASEBE U
C_out=np.dot(Matrix,C_in)
print(C_out)
print(C_out.tolist())
plt.plot(obs,'g', label="Observation")
plt.plot(C_out,'r', label="Simulation")
plt.margins(x=0, y=0)
plt.title("Chloride Prediction with Unit Hydrograph",size=18)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.ylabel("Chloride Concentration (mg/l)",size=18)
plt.xlabel("time step (7hr)",size=18)
plt.legend(fontsize=20)
plt.grid()
plt.show()


