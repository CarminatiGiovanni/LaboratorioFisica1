import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

def dev_std(a: np.ndarray) -> np.float64:
    mean = np.mean(a)
    return np.sqrt((np.sum(((a - mean)**2))/(len(a)-1)))

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'caduta_libera.csv'
fr = pd.read_csv(FILE)

h = np.array(fr['h'])*0.01
t = np.array(fr['AVG t']) * 0.001

columns = list(fr.columns[1:4])
buffer_std = []
for i in range(0,len(h)):
    buffer = []
    for c in columns:
        buffer.append(fr[c][i] * 0.001)
    buffer_std.append(dev_std(np.array(buffer,dtype=np.float64))/np.sqrt(len(columns)))

sigmaYmisurati = np.round(np.array(buffer_std,dtype=np.float64),2)

sigmaY_propagati = 2*sigmaYmisurati*t
sigmayy = np.mean(sigmaY_propagati)

r = RettaInterpolata(h,t**2, sigmayy)
plt.plot(t,h)
plt.plot(r.best_x,r.best_y)
plt.errorbar(r.X,r.Y,fmt='o',yerr=r.sigmaY,color="red",ecolor="black",capsize=5)

g = 2/r.B
sigmag = g * (r.sigmaB / r.B)

print(g,sigmag)
plt.show()

r = RettaInterpolata(t**2,h)
g = 2*r.B
sigmag = r.sigmaB * 2

print(g,sigmag)





