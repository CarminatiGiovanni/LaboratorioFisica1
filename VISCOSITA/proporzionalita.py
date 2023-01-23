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

# plt.plot([0,2,3,4,5,6],v_medie)
# plt.show()
# plt.plot([0,4,9,16,25,36],v_medie, color="#1ff24a")
# plt.show()
# plt.plot([0,2,3,4,5,6],v_medie)
# plt.yscale('log')
# plt.xscale('log')
# plt.show()

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
plt.plot(x_exp,y_exp)
plt.plot(x,y,"o", color="#1ff24a")
plt.show()