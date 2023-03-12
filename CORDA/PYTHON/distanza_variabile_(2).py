import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from typing import Final
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misurazione_distanza_variabile.csv'

ERRORE_SENSIBILITA_OSCILLOSCOPIO = 1 #

fr = pd.read_csv(FILE, sep = ';')  # fileread

l = np.array(fr['L']) # m
f1 = np.array(fr['f1']) # prima onda stazionaria
f2 = np.array(fr['f2']) # seconda onda stazionaria (più precisa)

r1 = RettaInterpolata(1/l,f1, ERRORE_SENSIBILITA_OSCILLOSCOPIO)
plt.plot(r1.best_x,r1.best_y, label=f"f1 $\sigma_y$={round(r1.sigmaY,2)}")
plt.errorbar(r1.X,r1.Y, yerr=r1.sigmaY, fmt='o', ecolor='black', color="red", capsize=5)

r2 = RettaInterpolata(1/l,f2, ERRORE_SENSIBILITA_OSCILLOSCOPIO)
plt.plot(r2.best_x,r2.best_y,label=f"f2 $\sigma_y$={round(r2.sigmaY,2)}")
plt.errorbar(r2.X,r2.Y, yerr=r2.sigmaY, fmt='o', ecolor='black', color="red", capsize=5)

plt.title("distanza variabile e frequenza per prima e seconda armonica")
plt.xlabel('1/d ($m^(-1)$)')
plt.ylabel('frequenza (Hz)')
plt.xticks(np.round(1/l,2),rotation=40)
plt.legend()
plt.show()