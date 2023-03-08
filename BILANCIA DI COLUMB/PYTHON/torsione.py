import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'massa_teta_C.csv'

fr = pd.read_csv(FILE)  # fileread
m = np.array(fr["mg"]) * 0.000001 # kg
teta1 = np.array(fr["teta1"])
teta2 = np.array(fr["teta2"])
teta3 = np.array(fr["teta3"])
teta4 = np.array(fr["teta4"])
teta5 = np.array(fr["teta5"])

teta = np.array([round(np.average([teta1[i],teta2[i],teta3[i],teta4[i],teta5[i]]),0) for i in range(0,len(teta1))],dtype=np.int16)
teta = (teta/180)*np.pi # rad
F = m * 9.81

r = RettaInterpolata(F,teta,(1/180)*np.pi,'BX')

plt.title("peso (N) - teta (rad) \nTORSIONE")
plt.plot(r.best_x, r.best_y, color="green", linewidth="4", label="retta interpolata")
plt.errorbar(r.X,r.Y,fmt='o',yerr=r.sigmay, ecolor='black', capsize=5, color="red", label="peso - teta")
plt.legend()
plt.xticks(r.X)
plt.show()

K = 1 / r.B
deltaK = (r.sigmaB / (r.B ** 2))

print(K, deltaK)