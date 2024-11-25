import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_rainfall=pd.read_excel('AH_HW7_Data_14002_8.xlsx',sheet_name='Rainfall')
# print(df_rainfall)
df_streamflow=pd.read_excel('AH_HW7_Data_14002_8.xlsx',sheet_name='Streamflow')
# print(df_streamflow)

############### MOHASEBE Ui
M = 3
# print(M)
N = (df_streamflow['flow mm/7hr'] != 0).sum() #83
# print(N)
n_max= N - M + 1 #79
# print(n_max)
Qn=df_streamflow[['flow mm/7hr']].to_numpy()
# print(Qn.shape)
# print(Qn)

dfp=df_rainfall['Rainfall mm']
print(dfp)

# print(dfp.iloc[0:4+1, 11:12]['Rainfall mm'].to_list())


P_matrix=np.zeros([N,n_max])
for n in range(0,N,1): # n namayande radife matrix hastv dar vaghe az n tooye formoola yeki kma==amtare bekhatere index python
    print(n)
    if n+1 <= M:
        zeros=[0 for _ in range(n_max-(n+1))]
        List_Pi = dfp.iloc[0:n+1].to_list()
        Pi_n=[ele for ele in reversed(List_Pi)]
        P_row=Pi_n+zeros
        P_matrix[n]=P_row
    print(zeros)
    print(Pi_n)
    print(Pi_n+zeros)
# print(P_matrix)

P_matrix[0:,1:]=0
# print(P_matrix)

# vector=P_matrix[:,[0]]
vector=P_matrix[:,0]
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
# print(Matrix)
# print(Matrix.shape)
# print(Qn.shape)

################ MOHASEBE U

# U=np.linalg.solve(Matrix, Qn)
# print(U)

Matrix_cut=Matrix[0:n_max]
# print(Matrix_cut)
# print(Matrix_cut.shape)
Q_cut=Qn[0:n_max]
# print(Q_cut.shape)
# print(Q_cut)

# U=np.linalg.solve(Matrix_cut,Q_cut)
# print(U)

####### MOHASEBE U HAYE MOSBAT
U_positive=np.zeros([n_max])
U_positive[0]=Q_cut[0]/Matrix_cut[0][0]
# print(Q_cut[0])
# print(Matrix_cut[0][0])
# print(U_positive)

for row in range(1,n_max,1):
    # print(Q_cut[row])
    minus=0
    for col in range(0,row,1):
        minus+=Matrix_cut[row][col]*U_positive[col]
    U_positive[row]=(Q_cut[row]-minus)/Matrix_cut[0][0]
    if U_positive[row]<=0:
        U_positive[row]=0
print(U_positive)
print(U_positive.tolist())


plt.plot(U_positive,linewidth=2)
plt.margins(x=0, y=0)
plt.title("Unit Hydrograph from 15/03/2008 09:00 to 18/03/2008 07:00",size=18)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel("time step (7hr)",size=18)
plt.ylabel("U (mm/7hr)",size=18)
plt.grid()
plt.show()