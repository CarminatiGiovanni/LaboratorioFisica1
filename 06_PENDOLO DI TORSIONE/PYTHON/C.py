import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

T2 = np.array([1.46,1.47,1.47,1.45,1.48,1.46,1.46,1.48,1.48,1.44,1.47,1.47,1.46,1.48,1.47])

I_elicottero = 2.76e-3  # inerzia misurata dalla formula
T_medio2 = np.mean(T2)
sigma_T2 = np.std(T2)
sigma_media_T2 = sigma_T2/np.sqrt(len(T2)) 

C2 = 4*(np.pi**2)*I_elicottero/(T_medio2**2)
sigmaC2 = 2 * (sigma_media_T2 / T_medio2) * C2
print("C2",C2,sigmaC2)


T3 = np.array([1.04,1.04,1.04,1.04,1.04,1.04,1.04,1.04,1.03,1.03,1.05,1.04,1.04,1.03,1.03])

T_medio3 = np.mean(T3)
sigma_T3 = np.std(T3)
sigma_media_T3 = sigma_T3/np.sqrt(len(T3)) 

C3 = 4*(np.pi**3)*I_elicottero/(T_medio3**3)
sigmaC3 = 3 * (sigma_media_T3 / T_medio3) * C3
print("C3",C3,sigmaC3)