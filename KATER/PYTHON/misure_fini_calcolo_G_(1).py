import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misure_fini.csv'
fr = pd.read_csv(FILE)

h1 = (np.array(fr['d'])) * 0.01
#h1 = np.sqrt(h1)

def dev_std(a: np.ndarray) -> np.float64:
    mean = np.mean(a)
    return np.sqrt((np.sum(((a - mean)**2))/(len(a)-1)))/np.sqrt(len(a))

t1 =np.array(fr["t1"])
t2 =np.array(fr["t2"])
t3 =np.array(fr["t3"])
t4 =np.array(fr["t4"])
T1 =np.array(fr["T1"])
T2 =np.array(fr["T2"])
T3 =np.array(fr["T3"])
T4 =np.array(fr["T4"])

dev_stdt = np.array([dev_std(np.array([t1[i],t2[i],t3[i],t4[i]])) for i in range(0,len(h1))])
dev_stdT = np.array([dev_std(np.array([T1[i],T2[i],T3[i],T4[i]])) for i in range(0,len(h1))])
dev_stdt = np.mean(dev_stdt)
dev_stdT = np.mean(dev_stdT)

periodo1 = np.array(fr["AVG t"])
periodo2 = np.array(fr["AVG T"])
print(periodo1)
print(periodo2)

r1 = RettaInterpolata(h1,periodo1, dev_stdt)
r2 = RettaInterpolata(h1,periodo2, dev_stdT)

plt.plot(r1.best_x,r1.best_y,label="$coltello_1$")
plt.plot(r2.best_x,r2.best_y,label="$coltello_2$")
plt.errorbar(r1.X,r1.Y,fmt='o',yerr=r1.sigmaY,color="red",ecolor="black",capsize=5)
plt.errorbar(r2.X,r2.Y,fmt='o',yerr=r2.sigmaY,color="red",ecolor="black",capsize=5)

print(r1)
print(r2)

plt.legend()
plt.title("intorno nel punto di intersezione delle parabole (circa 10cm)\n")
plt.xticks(np.round(h1,3))
plt.ylabel('$T (s)$')
plt.xlabel("$\sqrt{h_1}\quad(\sqrt{m})$")
plt.show()


################# CALCOLO G

B1 = r1.B
B2 = r2.B

sigmaB1 = r1.sigmaB
sigmaB2 = r2.sigmaB

A1 = r1.A
A2 = r2.A

sigmaA1 = r1.sigmaA
sigmaA2 = r2.sigmaA

sigmaY1 = r1.sigmaY
sigmaY2 = r2.sigmaY

T1 = A1 + B1*((A2-A1)/(B1-B2))
T1 = np.round(T1,2) # 2.00

x = (A2-A1)/(B1-B2)

D = 0.994

g = 4*np.power(np.pi,2)*D/(T1**2)

sigmaA1A2 = np.sqrt(sigmaA1**2+sigmaA2**2)
sigmaB1B2 = np.sqrt(sigmaB1**2+sigmaB2**2)

sigmax = np.sqrt((sigmaA1A2/(A2-A1))**2 + (sigmaB1B2/(B1-B2)**2)) * x
sigmaProdotto = np.sqrt((sigmax/x)**2 + (sigmaB1/B1)**2) * B1 * x
sigmaT = np.sqrt(sigmaProdotto**2+sigmaA1**2)
sigmag = 2 * sigmaT * T1

print("T: ",np.round(T1,2),"±",np.round(sigmaT,2))
print("g: ",np.round(g,2),"±",np.round(sigmag,2))


# print("--------------------------------------")

# T1A = periodo1[6]
# T1B = periodo1[7]
# sigma1 = dev_stdt
# T2A = periodo2[6]
# T2B = periodo2[7]
# sigma2 = dev_stdT

# T = (T2A*T1B-T1A*T2B)/(T1B-T2B-T1A+T2A)


# pno = T2A*T1B*np.sqrt((sigma2/T2A)**2+(sigma1/T1B)**2)
# pne = T1A*T2B*np.sqrt((sigma2/T2B)**2+(sigma1/T1A)**2)
# pn = np.sqrt(pno**2+pne**2)
# ps = np.sqrt(2*sigma1**2+2*sigma2**2)
# sigmaT = T*np.sqrt((pn/(T2A*T1B-T1A*T2B))**2 + (ps/(T1B-T2B-T1A+T2A))**2)
# print(sigmaT)
# print(4*np.power(np.pi,2)*D/(T*2),2*sigmaT*T)