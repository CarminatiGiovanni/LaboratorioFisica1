import numpy as np

Te_ = np.array([34, 33, 35, 34, 34])  # temperature
m = 0.1  # kg m1 = m2
T1 = 20  # °C
T2 = 50  # °C

Te = np.mean(Te_)  # temperatura di equilibrio media
sigmaT = 0.5  # incertezza sulla temperatura dovuta alla sensibilità del termometro
sigmam = 0.001  # incertezza sulla massa dovuta alla sensibilità della bilancia

# incertezza su Te propagato con errore nella lettura
sigma_Te = np.sqrt(np.std(Te_)**2 + sigmaT**2)
sigma_Te_medio = sigma_Te / np.sqrt(len(Te_) - 1)

me = (m*(T2-Te))/(Te-T1) - m

# calcolo propagazione errore su massa equivalente
e1 = np.sqrt(sigma_Te_medio**2 + sigmaT**2)
sigma_prodotto = (me + m) * np.sqrt((sigmam/m)**2 + (e1/(T2-Te))**2 + (e1/(Te-T1))**2)

sigmame = np.sqrt(sigma_prodotto**2 + sigmam**2)

print(np.round(me, 3), np.round(sigmame, 3))
