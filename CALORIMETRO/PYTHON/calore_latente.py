T_h20 = 85.5 + 273.15 # °K
T_ice = -17 + 273.15 # °K
T_fus = 273.15 # °k
m_ice = 0.05 # kg
m_h20 = 0.3 # kg


me_200 = 0.014 # massa equivalente per 200g di h20
me = me_200 * 0.3 / 0.2 # massa equivalente per 300g di h20
Te = 57.5 + 273.15 # °K
c_ice = 2051
c_h20 = 4181

calore_latente = ((m_h20 + me) * c_h20 * (T_h20 - Te) - m_ice * c_ice * (T_fus - T_ice) - m_ice * c_h20 * (Te - T_fus))/m_ice

print("calore latente: ",calore_latente)


