import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from typing import Final
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misurazione1_2.csv' # la prima misurazione il peso toccava il banco

AMPIEZZA : Final = 5 # Volt
l: Final = 1 # m

fr = pd.read_csv(FILE, sep = ';')  # fileread

masse = np.array(fr['massa']) * 0.001 #Kg
f1 = np.array(fr['f1']) #Hz
f2 = np.array(fr['f2'])
f3 = np.array(fr['f3'])
f4 = np.array(fr['f4'])

n_armonica = np.array([1,2,3,4])
ERRORE_SENSIBILITA_OSCILLOSCOPIO: Final = 1 # Hz

for i in range(0,len(masse)):
    f = np.array([f1[i],f2[i],f3[i],f4[i]])
    r = RettaInterpolata(n_armonica,f,ERRORE_SENSIBILITA_OSCILLOSCOPIO)
    print(r)
    plt.plot(r.best_x,r.best_y,label=f"massa: {int(masse[i]*1000)}g")
    plt.errorbar(r.X,r.Y,yerr=r.sigmaY,fmt='o', ecolor='black', color="red", capsize=10)

plt.title("Frequenza per armonica variando la massa")
plt.xlabel("armonica")
plt.ylabel("frequenza (Hz)")
plt.xticks(n_armonica)
plt.legend()
plt.show()
