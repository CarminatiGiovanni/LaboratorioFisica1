from typing import Final as const
import numpy as np

COSTANTE_DI_TORSIONE: const = 8.617290052022186e-05
raggio: const = 0.017 # m

distanza_variabile_A:const = 0.0125 #A1
delta_distanza_variabile_A: const = 0.0005 #deltaA1

voltaggio_variabile_A: const = 3.59e-08 #A2
delta_voltaggio_variabile_A: const = 0.11e-08 #deltaA2

########################### CASO A1 ##########################

EPSILON = (COSTANTE_DI_TORSIONE * distanza_variabile_A) / (4*np.pi*6000*6000*np.power(raggio,2))
print(EPSILON)


########################### CASO A2 ############################

EPSILON = (voltaggio_variabile_A * COSTANTE_DI_TORSIONE * 0.01)/(4*np.pi*np.power(raggio,2))
print(EPSILON)