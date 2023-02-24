import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE1 = dir_path + '/../CSV/' + 'T=24.5°C.csv'
FILE2 = dir_path + '/../CSV/' + 'T=18.5°C.csv'

fr1 = pd.read_csv(FILE1)  # fileread
fr2 = pd.read_csv(FILE2)

data1 = np.array([np.array(fr1[str(i)]) for i in range(2,7)])
data2 = np.array([np.array(fr2[str(i)]) for i in range(2,7)])

t_medie1 = np.array(list(np.mean(i) for i in data1))  # calcola le medie dei tempi per ogni diametro
v_medie1 = np.concatenate(([0], 0.2 / t_medie1))  # calcola le medie delle velocità per ogni diametro (primo valore 0)

t_medie2 = np.array(list(np.mean(i) for i in data2))  # calcola le medie dei tempi per ogni diametro
v_medie2 = np.concatenate(([0], 0.2 / t_medie2))  # calcola le medie delle velocità per ogni diametro (primo valore 0)

#  k = (plt.style.available)
#  plt.style.use(stile)

# plt.figure("studio misure sfere di raggio variabile", figsize=(15, 8))  # set titolo grafici

# costruisce gli spazi in cui dividere i grafici
#plt_retta = plt.subplot2grid((3, 3), (0, 0))
#plt_parabola = plt.subplot2grid((3, 3), (1, 0))
#plt_log = plt.subplot2grid((3, 3), (2, 0))
#plt_accordo = plt.subplot2grid((3, 3), (0, 1), colspan=2, rowspan=3)

raggi = np.array([0, 2, 3, 4, 5, 6])/2

# plt.figure(figsize=(4,6))
# plt.plot(raggi**2, v_medie1,'o-', color="red", label="T=24.5°C")
# plt.plot(raggi**2, v_medie2,'o-', color="blue", label="18.5°C")
# plt.xticks(raggi**2)
# # plt.xscale('log')
# # plt.yscale('log')
# plt.xlabel("$r$ [mm]")
# plt.ylabel("$v$ [m/s]")
# plt.title("raggio$^2$ - velocità (log)")
# plt.legend()
# plt.show()

"""

plt_parabola.plot([0, 4, 9, 16, 25, 36], v_medie, color="orange")
plt_parabola.set_title("$raggio^{2}$-velocità")
plt_parabola.set_ylim(bottom=0)
plt_parabola.set_xlim(left=0)

plt_log.plot([0, 2, 3, 4, 5, 6], v_medie, color="purple")
plt_log.set_xscale('log')
plt_log.set_yscale('log')
plt_log.set_title("raggio-velocità (log)")
plt_log.set_ylim(bottom=0)
plt_log.set_xlim(left=0)

"""

# interpoliamo // la ringraziamo

# Costruiamo la retta che meglio descrive i nostri valori:
# y = B + Ax

y1 = v_medie1[1:]  # rinomino per comodità
x1 = raggi[1:]**2
N1 = len(x1)

delta1 = N1 * np.sum(np.power(x1, 2)) - np.power(np.sum(x1), 2)  # Δ

A1 = (np.sum(np.power(x1, 2)) * np.sum(y1) - np.sum(x1) * np.sum(x1 * y1)) / delta1  # A
B1 = (N1 * np.sum(x1 * y1) - np.sum(x1) * np.sum(y1)) / delta1  # B

v1 = y1 - A1 - B1 * x1  # v dovrebbe essere più piccola possibile
sigmaY1 = np.sqrt((1.0 / (N1 - 2)) * np.sum(np.power(y1 - A1 - B1 * x1, 2)))  # incertezza sulla Y (notare correzione bessel -2)
sigmaA1 = sigmaY1 * np.sqrt(np.sum(x1 * x1) / delta1)  # incertezza su A
sigmaB1 = sigmaY1 * np.sqrt(N1 / delta1)  # incertezza su B

x_exp1 = np.linspace(0.8, max(x1) + 0.2, 100)
y_exp1 = A1 + B1 * x_exp1

# # set the spacing between subplots

y2 = v_medie2[1:]  # rinomino per comodità
x2 = raggi[1:]**2
N2 = len(x2)

delta2 = N2 * np.sum(np.power(x2, 2)) - np.power(np.sum(x2), 2)  # Δ

A2 = (np.sum(np.power(x2, 2)) * np.sum(y2) - np.sum(x2) * np.sum(x2 * y2)) / delta2  # A
B2 = (N2 * np.sum(x2 * y2) - np.sum(x2) * np.sum(y2)) / delta2  # B

v2 = y2 - A2 - B2 * x2  # v dovrebbe essere più piccola possibile
sigmaY2 = np.sqrt((1.0 / (N2 - 2)) * np.sum(np.power(y2 - A2 - B2 * x2, 2)))  # incertezza sulla Y (notare correzione bessel -2)
sigmaA2 = sigmaY2 * np.sqrt(np.sum(x2 * x2) / delta2)  # incertezza su A
sigmaB2 = sigmaY2 * np.sqrt(N2 / delta2)  # incertezza su B

x_exp2 = np.linspace(0.8, max(x2) + 0.2, 100)
y_exp2 = A2 + B2 * x_exp2


plt.plot(x_exp1, y_exp1, color='red', label="T=24.5°C")
plt.plot(x_exp2, y_exp2, color='blue', label="T=18.5°C")
plt.errorbar(x1, y1, yerr=sigmaY1, fmt='o', ecolor='black', color="red", capsize=10)
plt.errorbar(x2, y2, yerr=sigmaY2, fmt='o', ecolor='black', color="blue", capsize=10)
plt.xticks(x2)
plt.legend()
plt.title('accordo punti-retta')

plt.tight_layout()
# plt.show()

print(F"""
    delta1: {round(delta1, 4)}
    A1: {round(A1, 4)}
    sigmaA1: {round(sigmaA1, 4)}

    B1: {round(B1, 4)}
    sigmaB1: {round(sigmaB1, 4)}

    sigmaY1: {round(sigmaY1, 4)}

    --------------------------------------

    delta2: {round(delta2, 4)}
    A2: {round(A2, 4)}
    sigmaA2: {round(sigmaA2, 4)}

    B2: {round(B2, 4)}
    sigmaB2: {round(sigmaB2, 4)}

    sigmaY2: {round(sigmaY2, 4)}

""")
