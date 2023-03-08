import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE_V1_COST_A2 = dir_path + '/../CSV/' + "d_cost_v1_cost_A2.csv"
FILE_V_EQ_A1 = dir_path + '/../CSV/' + "d_cost_v1_eq_v2_A1.csv"

fr1 = pd.read_csv(FILE_V_EQ_A1)
fr2 = pd.read_csv(FILE_V1_COST_A2)

V_fissa = np.array(fr1["V"])
teta1 = np.array(fr1["teta1"])
teta2 = np.array(fr1["teta2"])
teta3 = np.array(fr1["teta3"])
v_fissa = (V_fissa*1000) ** 2  # considero il prodotto delle cariche
teta_fissa = np.array([round(np.average([teta1[i], teta2[i], teta3[i]]), 0) for i in range(0, len(teta1))], dtype=np.float_)
teta_fissa = (teta_fissa/180)*np.pi

v_variabile = np.array(fr2["V2"])
teta1 = np.array(fr2["teta1"])
teta2 = np.array(fr2["teta2"])
teta3 = np.array(fr2["teta3"])
v_variabile = v_variabile * 1000 * 6000  # la seconda carica aveva valore fisso 6kV
teta_variabile = np.array([round(np.average([teta1[i], teta2[i], teta3[i]]), 0) for i in range(0, len(teta1))], dtype=np.float_)
teta_variabile = (teta_variabile/180)*np.pi

V_times_V = np.concatenate([v_variabile, v_fissa])
thetas = np.concatenate([teta_variabile, teta_fissa])

r = RettaInterpolata(V_times_V,thetas,(1/180)*np.pi,'BX')

plt.title("PARTE A: ($V_1V_2$ - $\\bar{\\theta}$)")
plt.plot(r.best_x, r.best_y, color="#ab11f2", linewidth="3", label="retta interpolata")
plt.errorbar(v_fissa, teta_fissa, fmt='o', yerr=r.sigmay, color="brown", label="A.1", ecolor='black', capsize=5)
plt.errorbar(v_variabile, teta_variabile, fmt='o', yerr=r.sigmay, color="grey", label="A.2", ecolor='black', capsize=5)
plt.xticks(r.X, rotation=40)
plt.xlabel('$V_1V_2 \quad (V)$')
plt.ylabel("$\\bar{\\theta}\quad (rad)$")
plt.legend()
plt.show()

print(f"""
    B: {r.B}
    sigmaB: {r.sigmaB}
    sigmaY: {r.sigmay}
    
    chiquadro: {r.chiquadro_osservato}
    chiquadro ridotto: {r.chiquadro_osservato_ridotto}
    df: {r.df}
""")


