import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from B import calcB,calcDeltaB

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE_V_UGUALE = dir_path + '/../CSV/' + "d_fissa_v_uguale_per_ogni_carica.csv"
FILE_V_VARIABILE = dir_path + '/../CSV/' + "d_fissa_v_diversa.csv"

fr1 = pd.read_csv(FILE_V_UGUALE)  # fileread
fr2 = pd.read_csv(FILE_V_VARIABILE)

V_fissa = np.array(fr1["V"])
teta1 = np.array(fr1["teta1"])
teta2 = np.array(fr1["teta2"])
teta3 = np.array(fr1["teta3"])
v_fissa = (V_fissa*1000) ** 2 # considero il prodotto delle cariche
teta_fissa = np.array([round(np.average([teta1[i],teta2[i],teta3[i]]),0) for i in range(0,len(teta1))],dtype=np.int16)
teta_fissa = (teta_fissa/180)*np.pi


v_variabile = np.array(fr2["V2"])
teta1 = np.array(fr2["teta1"])
teta2 = np.array(fr2["teta2"])
teta3 = np.array(fr2["teta3"])
v_variabile = v_variabile * 1000 * 6000 # la seconda carica aveva valore fisso 6kV
teta_variabile = np.array([round(np.average([teta1[i],teta2[i],teta3[i]]),0) for i in range(0,len(teta1))],dtype=np.int16)
teta_variabile = (teta_variabile/180)*np.pi

todosX = np.concatenate([v_variabile,v_fissa])
todosY = np.concatenate([teta_variabile,teta_fissa])
B = calcB(todosX, todosY)
deltaB = calcDeltaB(todosX, todosY)
print(B, deltaB)

x_B = np.linspace(min(todosX), max(todosX), 100)
y_B = B * x_B

plt.title("prodotto Volt - teta(rad)")
plt.plot(v_fissa,teta_fissa,'o-', color ="brown", label="cariche uguali")
plt.plot(v_variabile,teta_variabile,'o-', color = "grey", label="cariche diverse")
plt.plot(x_B, y_B, color="#ab11f2", linewidth="4", label="retta interpolata")
plt.legend()
plt.show()


