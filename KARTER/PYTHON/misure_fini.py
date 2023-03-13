import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misure_fini.csv'
fr = pd.read_csv(FILE)

d = (np.array(fr['d']))# * 0.01
print(d)
d = np.sqrt(d)
t1 = np.array(fr['t1'])
t2 = np.array(fr['t2'])
t3 = np.array(fr['t3'])
t4 = np.array(fr['t4'])
T1 = np.array(fr['T1'])
T2 = np.array(fr['T2'])
T3 = np.array(fr['T3'])
T4 = np.array(fr['T4'])

periodo1 = np.array([round(np.average([t1[i],t2[i],t3[i],t4[i]]),4) for i in range(0,len(d))])
periodo2 = np.array([round(np.average([T1[i],T2[i],T3[i],T4[i]]),4) for i in range(0,len(d))])
print(periodo1)
print(periodo2)

r1 = RettaInterpolata(d,periodo1,0.003)
r2 = RettaInterpolata(d,periodo2,0.003)

plt.plot(r1.best_x,r1.best_y,label="1000g su")
plt.plot(r2.best_x,r2.best_y,label="1000g giu")
plt.errorbar(r1.X,r1.Y,fmt='o',yerr=r1.sigmaY,color="red",ecolor="black",capsize=5)
plt.errorbar(r2.X,r2.Y,fmt='o',yerr=r2.sigmaY,color="red",ecolor="black",capsize=5)

print(r1)
print(r2)

plt.legend()
plt.xticks(d)
plt.show()