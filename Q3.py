import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_streamflow=pd.read_excel('AH_HW7_Data_14002_basefr.xlsx',sheet_name='Streamflow')
df_rainfall=pd.read_excel('AH_HW7_Data_14002_basefr.xlsx',sheet_name='Rainfall')
# print(df_rainfall)

############### TTD = normal dist
index=2375
# Precip=df_rainfall['Rainfall mm'][0:4]
# print(Precip.sum())

# def P(t):
#     p=df_rainfall['Rainfall mm'][0:t+1]
#     return p
# print(P(4))
#
# def Q(t):
#     q=df_streamflow['flow mm/7hr'][0:t+1]
#     return q
# print(Q(4))

P=df_rainfall['Rainfall mm']
Q=df_streamflow['flow mm/7hr']

storage={}
s0=700
for i in range(0,index,1):
    # print(i)
    # print(Q[i])
    S=(P[i]-Q[i])+s0
    storage[i]=S
    s0=S
# print(storage)


prt_tr={}
t=500 #indexe pythoniye radifi ke mikhay
for t in [122,534,938]:
    for tr in range(0, t, 1):  # az 0 ya 1 ? ta t ya t+1?
        print('tr', tr)
        E = 0
        for i in range(t - tr, t, 1):  # ta t ya t+1?
            # print('i',i)
            a = P[i] / storage[i]
            # print('p',P[i])
            # print('s', storage[i])
            E += a
        # print('E',E)
        prt = (P[t - tr] / storage[t - tr]) * np.exp(-E)
        prt_tr[f'({tr},{t})'] = prt
    # print(prt_tr)
    ax = plt.subplot()
    ax.plot(prt_tr.values(), label="Simulation")
    ax.margins(x=0, y=0)
    plt.title("Residence time distribution", size=18)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    # plt.ylabel(f"Prt(tr,t={t})", size=18)
    ax.yaxis.tick_right()
    ax.set_ylabel(f"Prt(tr,t={t})",rotation=-90,labelpad=25, size=18)
    ax.yaxis.set_label_position("right")
    plt.xlabel("time step (7hr)", size=18)
    plt.legend()
    ax.invert_xaxis()
    plt.grid()
    plt.show()
