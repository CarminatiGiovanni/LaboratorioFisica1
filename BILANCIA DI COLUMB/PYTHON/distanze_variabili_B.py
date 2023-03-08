import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'v_cost_B.csv'

fr = pd.read_csv(FILE)  # fileread
distanze = np.array(fr["d(cm)"])/ 100 #distanze in metri
teta1 = np.array(fr["teta1"])
teta2 = np.array(fr["teta2"])
teta3 = np.array(fr["teta3"])
raggio = 0.017

correzione_per_diametro = 1 - ((4 * np.power(raggio, 3)) / distanze ** 3)

teta = np.array([round(np.average([teta1[i],teta2[i],teta3[i]]),0) for i in range(0,len(teta1))],dtype=np.float32)
tetaRad = (teta/180) * np.pi

tetaRadConCorrezione = tetaRad / correzione_per_diametro

x = 1/(distanze**2)

r = RettaInterpolata(x, tetaRadConCorrezione, (1/180)*np.pi,'BX')

plt.title("$1/d^2$ - $\\bar{\\theta}$ (rad)")
plt.plot(r.best_x, r.best_y, color="red", label="retta interpolata", linewidth="3")
plt.errorbar(x, tetaRadConCorrezione,yerr=r.sigmay,ecolor='black',capsize=5,fmt='o', color="blue", label="distanze - angoli corretti")
plt.xticks(x, rotation=40)
plt.xlabel("$1/d^2$")
plt.ylabel("$\\bar{\\theta}$")
plt.legend()
plt.show()

print(f"""
    B: {r.B}
    sigmaB: {r.sigmaB}
    sigmaY: {r.sigmay}
    chi: {r.chiquadro_osservato}
    chi ridotto: {r.chiquadro_osservato_ridotto}
    df: {r.df}
""")