import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

massa_5sferette_5mm = 0.0025494 #kg
massa_sferetta_5mm = massa_5sferette_5mm / 5
volume_sferetta_5mm = (4.0/3)*np.pi*np.power(0.005,3)
densita_sferetta = round(massa_sferetta_5mm / volume_sferetta_5mm,1)

print(densita_sferetta)