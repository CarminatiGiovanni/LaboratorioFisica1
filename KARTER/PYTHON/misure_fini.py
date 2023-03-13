import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misure_fini.csv'
fr = pd.read_csv(FILE)

l = (np.array(fr['d']) + 15) * 0.01
l = np.sqrt(l)
periodo1 = np.array(fr["AVG t"])
periodo2 = np.array(fr["AVG T"])
print(periodo1)
print(periodo2)

r1 = RettaInterpolata(l,periodo1,0.002)
r2 = RettaInterpolata(l,periodo2,0.002)

plt.plot(r1.best_x,r1.best_y,label="1000g su")
plt.plot(r2.best_x,r2.best_y,label="1000g giu")
plt.errorbar(r1.X,r1.Y,fmt='o',yerr=r1.sigmaY,color="red",ecolor="black",capsize=5)
plt.errorbar(r2.X,r2.Y,fmt='o',yerr=r2.sigmaY,color="red",ecolor="black",capsize=5)

print(r1)
print(r2)

plt.legend()
plt.xticks(l)
plt.show()