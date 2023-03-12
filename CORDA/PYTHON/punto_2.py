import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from typing import Final
import scipy.stats as sc
from B import calcB, calcSigmaB, calcSigmaY_y_A_BX, calcA, calcSigmaA

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misurazione1_2.csv'

AMPIEZZA : Final = 5 # Volt
l: Final = 1 # m

fr = pd.read_csv(FILE, sep = ';')  # fileread

masse = np.array(fr['massa']) * 0.001 #Kg
f2 = np.array(fr['f2']) # Hz

ERRORE_SENSIBILITA_OSCILLOSCOPIO = 1

print(f2)
plt.plot(masse,f2,'o-')
B = calcB(masse,f2)
A = calcA(masse,f2)
sigmaB = calcSigmaB(masse,f2)
sigmaA = calcSigmaA(masse,f2)
sigmay = np.sqrt(np.sum((f2 - B*masse - A)**2)/3)
print(sigmay)
sigmay = np.sqrt(sigmay**2 + ERRORE_SENSIBILITA_OSCILLOSCOPIO**2)
print(sc.chisquare(f2,B * masse, ddof=1))

x = np.linspace(min(masse),max(masse),100)
y = B * x + A
plt.plot(x,y)
plt.errorbar(masse,f2, yerr=sigmay, fmt='o', ecolor='black', color="red", capsize=10)
plt.xticks(masse)
plt.show()
