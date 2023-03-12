import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from typing import Final
from B import calcB, calcSigmaB, calcSigmaY_y_A_BX, calcSigmaA, calcA
# from B import calcB, calcDeltaB

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misurazione_distanza_variabile.csv'

ERRORE_SNSIBILITA_OSCILLOSCOPIO = 1

fr = pd.read_csv(FILE, sep = ';')  # fileread

l = np.array(fr['L'])
f1 = np.array(fr['f1'])
f2 = np.array(fr['f2'])

# plt.plot(l,f2,'o-', label="f2")
# plt.xticks(l)

B = calcB(1/l,f2)
A = calcA(1/l,f2)
simgaA = calcSigmaA(1/l,f2)
sigmaB = calcSigmaB(1/l,f2)
sigmay = calcSigmaY_y_A_BX(1/l,f2)
sigmay = np.sqrt(sigmay ** 2 + ERRORE_SNSIBILITA_OSCILLOSCOPIO ** 2)

# plt.plot(1/l,f2,'o-', label="f2 prop inversa")
# plt.xticks(1/l)
x =np.linspace(min(1/l),max(1/l),100)
y = A + B*x
plt.plot(x,y)
plt.errorbar(1/l,f2, yerr=sigmay, fmt='o', ecolor='black', color="red", capsize=10)

plt.legend()
plt.show()