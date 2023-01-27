import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

fr = pd.read_csv('T=18,5.csv') #fileread

mm2 = np.array(fr["2"])
mm3 = np.array(fr["3"])
mm4 = np.array(fr["4"])
mm5 = np.array(fr["5"])
mm6 = np.array(fr["6"])

data = np.array([mm2,mm3,mm4,mm5,mm6])

t_medie = np.array([])

for i in data:
    t_medie = np.append(t_medie,round(np.mean(i),5))

v_medie = 0.2/t_medie

v_medie = np.concatenate(([0],v_medie))

print(plt.style.available)
plt.style.use('tableau-colorblind10')

plt.figure("accordo dati")

plt_retta = plt.subplot2grid((3, 3), (0, 0))
plt_parabola = plt.subplot2grid((3, 3), (1, 0))
plt_log = plt.subplot2grid((3, 3), (2, 0))
plt_accordo = plt.subplot2grid((3, 3), (0, 1), colspan=2,rowspan=3)

plt_retta.plot([0,2,3,4,5,6],v_medie)
plt_retta.set_title("raggio-velocità")

plt_parabola.plot([0,4,9,16,25,36],v_medie, color="#1ff24a")
plt_parabola.set_title("$raggio^{2}$-velocità")

plt_log.plot([0,2,3,4,5,6],v_medie, scalex='log', scaley='log')
plt_log.set_title("raggio-velocità (log)")

# interpoliamo // la ringraziamo

y = v_medie
x = np.array([0.0,4.0,9.0,16.0,25.0,36.0])
N = len(x)

delta = N * np.sum(np.power(x,2)) - np.power(np.sum(x),2)

A = (np.sum(np.power(x,2))*np.sum(y)-np.sum(x)*np.sum(x*y))/delta
B = (N*np.sum(x*y)-np.sum(x)*np.sum(y))/delta

v = y - A - B * x
sigmaY = np.sqrt((1.0/N) * np.sum(np.power(y - A - B * x,2)))
sigmaA = sigmaY * np.sqrt(np.sum(x*x)/delta)
sigmaB = sigmaY * np.sqrt(N/delta)

print(F"""
    delta: {delta}
    A: {A}
    sigmaA: {sigmaA}

    B: {B}
    sigmaB: {sigmaB}

    sigmaY: {sigmaY}

""")


x_exp = np.linspace(min(x),max(x),100)
y_exp = A + B * x_exp

plt_accordo.plot(x_exp,y_exp)
plt_accordo.plot(x,y,"o", color="#1ff24a")
plt_accordo.set_title('accordo punti-retta')

# set the spacing between subplots
#plt.axes(rect, projection=None, polar=False, **kwargs)
plt.tight_layout()
plt.show()