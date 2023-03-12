import numpy as np
from matplotlib import pyplot as plt
f_FINE = np.array([89,183,275])
f_GROSSA = np.array([27,54,81])

massa_GROSSA = 4.3 * 0.001 #kg
massa_FINE = 0.3 * 0.001 # kg

l_GROSSA = 2 # m
l_FINE = 1.23 # m

d_lin_GROSSA = massa_GROSSA/l_GROSSA
d_lin_FIE = massa_FINE/l_FINE

n = np.array([1,2,3])

plt.plot(n,f_FINE,'o-')
plt.plot(n,f_GROSSA,'o-')
plt.xticks(n)
plt.show()