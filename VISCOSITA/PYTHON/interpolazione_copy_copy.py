import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from B import calcB,calcDeltaB, calcDeltaY_y_A_BX, calcA, calcDeltaA

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

raggi = (np.array([0, 2, 3, 4, 5, 6])/2)*0.001

# interpoliamo // la ringraziamo

# Costruiamo la retta che meglio descrive i nostri valori:
# y = B + Ax

y1 = v_medie1[1:]  # rinomino per comodità
x1 = raggi[1:]**2

B1 = calcB(x1,y1) #(np.sum(np.power(x1, 2)) * np.sum(y1) - np.sum(x1) * np.sum(x1 * y1)) / delta1  # A
A1 = calcA(x1,y1)
deltaB1 = calcDeltaB(x1,y1)
sigmaY1 = calcDeltaY_y_A_BX(x1,y1)

x_exp1 = np.linspace(min(x1), max(x1), 100)
y_exp1 = B1 * x_exp1 + A1


# # set the spacing between subplots

y2 = v_medie2[1:]  # rinomino per comodità
x2 = raggi[1:]**2

B2 = calcB(x2,y2)
A2 = calcA(x2,y2)
deltaB2 = calcDeltaB(x2,y2)
sigmaY2 = calcDeltaY_y_A_BX(x2,y2)

x_exp2 = np.linspace(min(x2), max(x2), 100)
y_exp2 = B2*x_exp2 + A2


plt.plot(x_exp1, y_exp1, color='red', label="T=24.5°C")
plt.plot(x_exp2, y_exp2, color='blue', label="T=18.5°C")
plt.errorbar(x1, y1, yerr=sigmaY1, fmt='o', ecolor='black', color="red", capsize=10)
plt.errorbar(x2, y2, yerr=sigmaY2, fmt='o', ecolor='black', color="blue", capsize=10)
plt.xticks(x2)
plt.legend()
plt.title('accordo punti-retta')

plt.tight_layout()
plt.show()

print(f"""      
        A1: {A1}
        B1: {B1}
        DELTA Y1: {sigmaY1}

        A2: {A2}
        B2: {B2}   
        DELTA Y2: {sigmaY2}   
      """)