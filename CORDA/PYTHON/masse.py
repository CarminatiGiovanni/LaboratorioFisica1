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
f1 = np.array(fr['f1']) #Hz
f2 = np.array(fr['f2'])
f3 = np.array(fr['f3'])
f4 = np.array(fr['f4'])

f = [f1,f2,f3,f4]

for i in f:
    A = calcA(masse,i)
    B = calcB(masse,i)
    sigmaA = calcSigmaA(masse,i)
    sigmaB = calcSigmaB(masse,i)
    sigmay = calcSigmaY_y_A_BX(masse,i)

    x = np.linspace(min(masse),max(masse),100)
    y = A + B*x

    print(sc.chisquare(i,B*masse + A,ddof=1))

    plt.plot(x,y)
    plt.errorbar(masse,i, yerr=sigmay, fmt='o', ecolor='black', color="red", capsize=10)

plt.xticks(masse)
plt.show()