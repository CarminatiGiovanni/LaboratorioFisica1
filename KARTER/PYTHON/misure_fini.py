import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misure_fini.csv'
fr = pd.read_csv(FILE)

l = (np.array(fr['d'])) * 0.01
l = np.sqrt(l)
periodo1 = np.array(fr["AVG t"])
periodo2 = np.array(fr["AVG T"])
print(periodo1)
print(periodo2)

#TODO: errori con correzione di bessel
r1 = RettaInterpolata(l,periodo1)
r2 = RettaInterpolata(l,periodo2)

plt.plot(r1.best_x,r1.best_y,label="1000g su")
plt.plot(r2.best_x,r2.best_y,label="1000g giu")
plt.errorbar(r1.X,r1.Y,fmt='o',yerr=r1.sigmaY,color="red",ecolor="black",capsize=5)
plt.errorbar(r2.X,r2.Y,fmt='o',yerr=r2.sigmaY,color="red",ecolor="black",capsize=5)

print(r1)
print(r2)

plt.legend()
plt.xticks(np.round(l,4))
plt.show()


################# CALCOLO G

B1 = r1.B
B2 = r2.B

sigmaB1 = r1.sigmaB
sigmaB2 = r2.sigmaB

A1 = r1.A
A2 = r2.A

sigmaA1 = r1.sigmaA
sigmaA2 = r2.sigmaA

sigmaY1 = r1.sigmaY
sigmaY2 = r2.sigmaY

T1 = A1 + B1*((A2-A1)/(B1-B2))
T1 = np.round(T1,2) # 2.00

x = (A2-A1)/(B1-B2)
l = x**2 + 0.15

D = 0.994

g = 4*np.power(np.pi,2)*D/(T1**2)
print(g)

sigmaA1A2 = np.sqrt(sigmaA1**2+sigmaA2**2)
sigmaB1B2 = np.sqrt(sigmaB1**2+sigmaB2**2)

sigmax = np.sqrt((sigmaA1A2/(A2-A1))**2 + (sigmaB1B2/(B1-B2)**2)) * ((A2-A1)/B1-B2)
sigmaProdotto = np.sqrt((sigmax/x)**2 + (sigmaB1/B1)**2) * B1 * x
sigmaT = np.sqrt(sigmaProdotto**2+sigmaA1**2)
sigmag = T1 * 2 * (sigmaT/T1)

print(sigmag)