import numpy as np
from typing import Final as const

# raggio_sferetta: const = 0.005 / 2  # TODO: pesare sferette 3mm per una maggiore precisione
# massa_5sferette_5mm: const = 0.0025494  # kg
# massa_sferetta_5mm: const = massa_5sferette_5mm / 5
# volume_sferetta_5mm: const = (4.0/3)*np.pi*np.power(raggio_sferetta, 3)
# densita_sferetta: const = round(massa_sferetta_5mm / volume_sferetta_5mm, 0)

# densita_glicerina: const = 1249  # kg/m3
# temperatura: const = 24.5  # °C

# v_limite_misurata = 0.2/2.32  # spazio/tempo misurato in misure ed errori

# viscosita = (2 * 9.81 * np.power(raggio_sferetta,2) * (densita_sferetta - densita_glicerina)) / (9 * v_limite_misurata)

# print(f"viscosità misurata: {viscosita}")
# aspettazione = np.exp(-2.18-0.099*temperatura)

# print(f"viscosità aspettata: {aspettazione} Pa/s")  # 1.256

raggio = 0.0015
diff_densita = 7799 - 1249
v = 0.1 / 2.98
T = 24.5

viscosita = (2 * 9.81 * diff_densita * (raggio**2))/ (9*v)
print(viscosita)
print(np.exp(-2.18-0.099*T)* 100)


A = 0.0032

viscosita = (2*9.81*diff_densita)/(9*A)

print(viscosita)
