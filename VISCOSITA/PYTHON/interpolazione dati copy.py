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

plt.plot(raggi, v_medie1,'o-', color="red", label="T=24.5°C")
plt.plot(raggi, v_medie2,'o-', color="blue", label="18.5°C")

plt.xscale('log')
plt.yscale('log')
plt.xlabel("$r$ [mm]")
plt.ylabel("$v$ [m/s]")
plt.title("raggio - velocità")
plt.legend()
plt.show()

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

# interpoliamo // la ringraziamo

# Costruiamo la retta che meglio descrive i nostri valori:
# y = B + Ax

y = v_medie[1:]  # rinomino per comodità
x = np.array([4, 9, 16, 25, 36], dtype=np.float16)
N = len(x)

delta = N * np.sum(np.power(x, 2)) - np.power(np.sum(x), 2)  # Δ

A = (np.sum(np.power(x, 2)) * np.sum(y) - np.sum(x) * np.sum(x * y)) / delta  # A
B = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / delta  # B

v = y - A - B * x  # v dovrebbe essere più piccola possibile
sigmaY = np.sqrt(
    (1.0 / (N - 2)) * np.sum(np.power(y - A - B * x, 2)))  # incertezza sulla Y (notare correzione bessel -2)
sigmaA = sigmaY * np.sqrt(np.sum(x * x) / delta)  # incertezza su A
sigmaB = sigmaY * np.sqrt(N / delta)  # incertezza su B
"""

# print(F"""
#     delta: {round(delta, 4)}
#     A: {round(A, 4)}
#     sigmaA: {round(sigmaA, 4)}

#     B: {round(B, 4)}
#     sigmaB: {round(sigmaB, 4)}

#     sigmaY: {round(sigmaY, 4)}

# """)

# x_exp = np.linspace(0, max(x) + 2, 100)
# y_exp = A + B * x_exp

# plt_accordo.plot(x_exp, y_exp, color='blue')
# plt_accordo.errorbar(x, y, yerr=sigmaY, fmt='o', ecolor='black', color="#1ff24a", capsize=10)
# plt_accordo.set_title('accordo punti-retta')
# plt_accordo.set_ylim(bottom=0)
# plt_accordo.set_xlim(left=0)

# # set the spacing between subplots

# plt.tight_layout()
# plt.show()
