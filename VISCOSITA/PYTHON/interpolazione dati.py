import numpy as np
from mpl_toolkits.axisartist.axislines import AxesZero
import pandas as pd
from matplotlib import pyplot as plt

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'T=24.5°C.csv'


fr = pd.read_csv(FILE) #fileread
mm2 = np.array(fr["2"])
mm3 = np.array(fr["3"])
mm4 = np.array(fr["4"])
mm5 = np.array(fr["5"])
mm6 = np.array(fr["6"])

data = np.array([mm2,mm3,mm4,mm5,mm6])

t_medie = np.array(list(np.mean(i) for i in data)) # calcola le medie dei tempi per ogni diametro
v_medie = np.concatenate(([0],0.2/t_medie)) # calcola le medie delle velocità per ogni diametro (primo valore 0)

#k = (plt.style.available)
#plt.style.use(stile)

plt.figure("studio misure sfere di raggio variabile",figsize=(15,8)) # set titolo grafici

# costruisce gli spazi in cui dividere i grafici
plt_retta = plt.subplot2grid((3, 3), (0, 0))
plt_parabola = plt.subplot2grid((3, 3), (1, 0))
plt_log = plt.subplot2grid((3, 3), (2, 0))
plt_accordo = plt.subplot2grid((3, 3), (0, 1), colspan=2,rowspan=3)

plt_retta.plot([0,2,3,4,5,6],v_medie, color="red")
plt_retta.set_title("raggio-velocità")
plt_retta.set_ylim(bottom = 0)
plt_retta.set_xlim(left=0)

plt_parabola.plot([0,4,9,16,25,36],v_medie, color="orange")
plt_parabola.set_title("$raggio^{2}$-velocità")
plt_parabola.set_ylim(bottom = 0)
plt_parabola.set_xlim(left=0)

plt_log.plot([0,2,3,4,5,6],v_medie, color="purple")
plt_log.set_xscale('log')
plt_log.set_yscale('log')
plt_log.set_title("raggio-velocità (log)")
plt_log.set_ylim(bottom = 0)
plt_log.set_xlim(left=0)

# interpoliamo // la ringraziamo

# Costruiamo la retta che meglio descrive i nostri valori:
# y = B + Ax

y = v_medie[1:] # rinomino per comodità
x = np.array([4,9,16,25,36], dtype=np.float16)
N = len(x)

delta = N * np.sum(np.power(x,2)) - np.power(np.sum(x),2) # Δ

A = (np.sum(np.power(x,2))*np.sum(y)-np.sum(x)*np.sum(x*y))/delta # A
B = (N*np.sum(x*y)-np.sum(x)*np.sum(y))/delta #B

v = y - A - B * x # v dovrebbe essere più piccola possibile
sigmaY = np.sqrt((1.0/(N-2)) * np.sum(np.power(y - A - B * x,2))) # incertezza sulla Y (notare correzione bessel -2)
sigmaA = sigmaY * np.sqrt(np.sum(x*x)/delta) # incertezza su A
sigmaB = sigmaY * np.sqrt(N/delta) # incertezza su B

print(F"""
    delta: {round(delta,4)}
    A: {round(A,4)}
    sigmaA: {round(sigmaA,4)}

    B: {round(B,4)}
    sigmaB: {round(sigmaB,4)}

    sigmaY: {round(sigmaY,4)}

""")


x_exp = np.linspace(0,max(x) + 2,100)
y_exp = A + B * x_exp

plt_accordo.plot(x_exp,y_exp, color='blue')
plt_accordo.errorbar(x,y,yerr=sigmaY,fmt='o',ecolor='black',color="#1ff24a",capsize=10)
plt_accordo.set_title('accordo punti-retta')
plt_accordo.set_ylim(bottom = 0)
plt_accordo.set_xlim(left=0)

# set the spacing between subplots

plt.tight_layout()
plt.show()