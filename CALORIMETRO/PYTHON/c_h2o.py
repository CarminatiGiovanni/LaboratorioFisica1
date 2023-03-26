import numpy as np
import matplotlib.pyplot as plt
from interpolazione2 import RettaInterpolata

T = np.array([21.5,22,22.5,23,23.5,24,24.5,25,26,27,28,29.5,30.5,32,34,35.5])
t = np.arange(0,21*60,60)


misure_buone = 10
r = RettaInterpolata(t[:misure_buone],T[:misure_buone],0.5)

plt.errorbar(r.X,r.Y,fmt='o',yerr=r.sigmaY,ecolor='black',capsize=5,color='red')
plt.plot(r.best_x,r.best_y)
plt.show()

print(r)


I = 3.5 # A
V = 15 # V
c_h20 = 4187 
m_h20 = 0.3 # kg
me = 0.014 #kg

J = (I*V)/(c_h20 * r.B * (m_h20 + me))
sigmaJ = J * r.sigmaB / r.B
print(np.round(J,2), np.round(sigmaJ,2))

