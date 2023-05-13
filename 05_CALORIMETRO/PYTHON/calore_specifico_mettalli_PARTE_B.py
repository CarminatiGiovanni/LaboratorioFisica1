import numpy as np

me = 0.014 # kg massa equivalente
T_met = 100 + 273.15 # °K temperatura metalli
T_amb = 20 + 273.15 # temperatura acqua ambiente
m_h20 = 0.2 # kg massa di acqua
c_h20 = 4187 # calore specifico dell'acqua
sigma_T = 0.5 # °C
sigmam = 0.001 # kilogram
sigma_me = 0.007 # sigma massa equivalente

# errore
sigma_m_a = np.sqrt(sigmam**2 + sigma_me**2)  # errore nella massa di acqua
sigma_dT = np.sqrt(sigma_T ** 2 + sigma_T**2) # errore differenza tra Te e altra temperatura


## RAME 
Te_rame = 23.85 + 273.15 #°K temperatura di equilibrio raggiunta dalla massa di rame
m_rame = 0.128 # kg massa di rame
c_rame = c_h20 * (Te_rame - T_amb) * (m_h20 + me) /( (T_met - Te_rame) * m_rame) # calore specifico del rame


sigma_c_rame = c_rame * np.sqrt((sigma_dT/(Te_rame - T_amb))**2 + (sigma_m_a/(m_h20 + me))**2 + (sigma_dT/(T_met - Te_rame))**2 + (sigmam/m_rame)**2)

print('Calore specifico rame: ',int(np.round(c_rame,0)), '±' , int(np.round(sigma_c_rame,0)))

## OTTONE
Te_ottone = 23.33 + 273.15 # °K temperatura di qeuilibrio raggiunta dalla massa di ottone
m_ottone = 0.122 # Kg massa di ottone
c_ottone = c_h20 * (Te_ottone - T_amb) * (m_h20 + me) /( (T_met - Te_ottone) * m_ottone) # calore specifico dell'ottone

sigma_c_ottone = c_ottone * np.sqrt((sigma_dT/(Te_ottone - T_amb))**2 + (sigma_m_a/(m_h20 + me))**2 + (sigma_dT/(T_met - Te_ottone))**2 + (sigmam/m_ottone)**2)

print('Calore specifico ottone: ',int(np.round(c_ottone,0)), '±' , int(np.round(sigma_c_ottone,0)))

## ALLUMINIO
Te_alluminio = 22.83 + 273.15 # °K temperatura di equilibrio raggiunta dall'alluminio
m_alluminio = 0.039 # Kg massa di alluminio
c_alluminio = c_h20 * (Te_alluminio - T_amb) * (m_h20 + me) /( (T_met - Te_alluminio) * m_alluminio) # calore specifico dell'ottone

sigma_c_alluminio = c_alluminio * np.sqrt((sigma_dT/(Te_alluminio - T_amb))**2 + (sigma_m_a/(m_h20 + me))**2 + (sigma_dT/(T_met - Te_alluminio))**2 + (sigmam/m_alluminio)**2)

print('Calore specifico alluminio: ',int(np.round(c_alluminio,0)), '±' , int(np.round(sigma_c_alluminio,0)))