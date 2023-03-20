import numpy as np

Te_ = np.array([34,33,35,34,34])

Te = np.mean(Te_)
sigmaT = 1
sigmam = 0.001 
sigma_Te = np.sqrt(np.std(Te_)**2 + sigmaT**2)

m = 0.1 #kg m1 = m2
T1 = 20 #°C
T2 = 50 #°C

me = (m*(T2-Te))/(Te-T1) - m

print(np.round(me,3), 0.002)
