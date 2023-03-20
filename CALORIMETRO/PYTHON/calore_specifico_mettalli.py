import numpy as np

me = 0.014 # kg
T_met = 100 + 273.15 # °K
T_amb = 20 + 273.15
m_h20 = 0.2 # kg
c_h20 = 4187


## RAME 
Te_rame = 23.85 + 273.15 #°K
m_rame = 0.128 # kg
c_rame = c_h20 * (Te_rame - T_amb) * (m_h20 + me) /( (T_met - Te_rame) * m_rame)
print('Calore specifico rame: ',int(np.round(c_rame,0)))

## OTTONE
Te_ottone = 23.33 + 273.15 # °K
m_ottone = 0.122 # Kg
c_ottone = c_h20 * (Te_ottone - T_amb) * (m_h20 + me) /( (T_met - Te_ottone) * m_ottone)
print('Calore specifico ottone: ',int(np.round(c_ottone,0)))

## ALLUMINIO
Te_al = 22.83 + 273.15 # °K
m_al = 0.039 # Kg
c_ottone = c_h20 * (Te_al - T_amb) * (m_h20 + me) /( (T_met - Te_al) * m_al)
print('Calore specifico alluminio: ',int(np.round(c_ottone,0)))
