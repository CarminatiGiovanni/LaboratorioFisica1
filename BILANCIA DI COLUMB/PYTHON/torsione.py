import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'torsione.csv'

fr = pd.read_csv(FILE)  # fileread
m = np.array(fr["mg"])
teta1 = np.array(fr["teta1"])
teta2 = np.array(fr["teta2"])
teta3 = np.array(fr["teta3"])
teta4 = np.array(fr["teta4"])
teta5 = np.array(fr["teta5"])

teta = np.array([round(np.average([teta1[i],teta2[i],teta3[i],teta4[i],teta5[i]]),0) for i in range(0,len(teta1))],dtype=np.int16)

plt.plot(m,teta,'o-',color="red")
plt.xticks(m)
# plt.show()

k_tanti = (0.000001*m*9.81)/((teta/180)*np.pi)
k = np.mean(k_tanti)
delta_k = np.std(k_tanti)

print("costante torsione: ",k)
print("deviazione: ",delta_k)


forze = k * teta

CONSTANTE_DIELETTRICA_ASSOLUTA = (k*(72/180)*np.pi*0.01)/(4*np.pi*np.power(0.017,2)*np.power(6000,2))
print("CONSTANTE_DIELETTRICA_ASSOLUTA: ",CONSTANTE_DIELETTRICA_ASSOLUTA)



