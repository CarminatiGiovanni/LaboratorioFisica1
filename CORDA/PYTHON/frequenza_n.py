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

# masse = np.array(fr['massa']) * 0.001 #Kg
f1 = np.array(fr['f1']) #Hz
f2 = np.array(fr['f2'])
f3 = np.array(fr['f3'])
f4 = np.array(fr['f4'])

n_armonica = np.array([1,2,3,4])
ERRORE_SNSIBILITA_OSCILLOSCOPIO = 1

    # A = calcA(n_armonica,i)
    # B = calcB(n_armonica,i)
    # sigmaA = calcSigmaA(n_armonica,i)
    # sigmaB = calcSigmaB(n_armonica,i)
    # sigmay = calcSigmaY_y_A_BX(n_armonica,i)

    # x = np.linspace(min(n_armonica),max(n_armonica),100)
    # y = A + B*x

    # print(sc.chisquare(i,B*n_armonica + A,ddof=1))

    # plt.plot(x,y)
# plt.errorbar(n_armonica,i, yerr=sigmay, fmt='o', ecolor='black', color="red", capsize=10)

# for i in range(0,4):

# TROPPA PRECISIONE !!!

f = np.array([f1[0],f2[0],f3[0],f4[0]])
plt.plot(n_armonica,f,'o-')
B = calcB(n_armonica,f)
sigmaB = calcSigmaB(n_armonica,f)
sigmay = np.sqrt(np.sum((f - B*n_armonica)**2)/3)
sigmay = np.sqrt(sigmay**2 + ERRORE_SNSIBILITA_OSCILLOSCOPIO**2)

print(sc.chisquare(f,B * n_armonica, ddof=1))

x = np.linspace(0,4,100)
y = B * x
plt.plot(x,y)
plt.errorbar(n_armonica,f, yerr=sigmay, fmt='o', ecolor='black', color="red", capsize=10)
plt.xticks(n_armonica)
plt.show()
