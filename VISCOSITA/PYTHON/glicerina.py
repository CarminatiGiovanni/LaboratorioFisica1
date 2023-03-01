import numpy as np
from typing import Final as const

rho_sferetta: const = 7800
rho_glicerina: const = 1260
diff_densita: const = rho_sferetta - rho_glicerina
g :const = 9.81
B1 = 11564
sigmaB1 = 608
B2 =7302
sigmaB2 = 154
T1 = 24.5
T2 = 15.5

viscosita1 = (2 * g * diff_densita)/ (9*B1)
sigma_viscosita1 = viscosita1 * sigmaB1 / B1
print("viscosità 24.5°C: ",viscosita1, sigma_viscosita1)
print("aspettati: ",np.exp(-2.18-0.099*T1)* 100)

viscosita2 = (2 * g * diff_densita)/ (9*B2)
sigma_viscosita2 = viscosita2 * sigmaB2 / B2
print("viscosità 18.5°C",viscosita2, sigma_viscosita2)
print("aspettati: ",np.exp(-2.18-0.099*T2)* 100)
