import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE_su = dir_path + '/../CSV/' + '10su.csv'
FILE_giu = dir_path + '/../CSV/' + '10giu.csv'

ERRORE_SENSIBILITA_OSCILLOSCOPIO = 1 #

fr_su = pd.read_csv(FILE_su)  # fileread
fr_giu = pd.read_csv(FILE_giu) 

d_su = (np.array(fr_su["h (cm) (massa 1.4kg)"]) + 5) * 0.01
d_giu = (np.array(fr_giu["h (cm) (massa 1.4kg)"]) + 5) * 0.01
# d_su = np.sqrt(d_su)
# d_giu = np.sqrt(d_giu)

t1 = np.array(fr_su["t1"])
t2 = np.array(fr_su["t2"])
t3 = np.array(fr_su["t3"])
t_su = np.array([round(np.average([t1[i],t2[i],t3[i]]),4) for i in range(0,len(d_su))],dtype=np.float64)

t4 = np.array(fr_giu["t1"])
t5 = np.array(fr_giu["t2"])
t6 = np.array(fr_giu["t3"])
t_giu = np.array([round(np.average([t4[i],t5[i],t6[i]]),4) for i in range(0,len(d_giu))],dtype=np.float64)

print(t_su)
print(t_giu)

r_su = RettaInterpolata(d_su,t_su)
r_giu = RettaInterpolata(d_su,t_giu)

plt.plot(r_su.X,r_su.Y)
plt.plot(r_giu.X,r_giu.Y)

plt.show()