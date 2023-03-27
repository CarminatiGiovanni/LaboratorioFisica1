import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'elicottero.csv'
fr = pd.read_csv(FILE)

alfa1 = np.mean(fr['alfa1 (1-5)'])
sigma_alfa1 = np.std(fr['alfa1 (1-5)'])

alfa2 = np.mean(fr["alfa2 (6-10)"])
sigma_alfa2 = np.std(fr["alfa2 (6-10)"])

alfa3 = np.mean(fr["alfa3"])
sigma_alfa3 = np.std(fr['alfa3'])

m = np.array([50,70,85]) * 0.001
alfa = np.array([alfa1,alfa2,alfa3]) # gr/s^2
raggio = 0.01 # m
alfa = (alfa/180) * np.pi # rad/s^2
sigma_alfa = np.array([sigma_alfa1,sigma_alfa2,sigma_alfa3])
sigma_alfa = (sigma_alfa/180)*np.pi #rad/s^2

r = RettaInterpolata(m, alfa, sigma_alfa)
plt.errorbar(m,alfa,yerr=sigma_alfa,fmt='o',color='red',ecolor='black',capsize=5)
plt.plot(r.best_x,r.best_y)
plt.xticks(m)
plt.show()

print(r)