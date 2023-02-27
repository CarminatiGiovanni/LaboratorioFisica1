import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misure.csv'

fr = pd.read_csv(FILE)  # fileread
distanze = np.array(fr["d(cm)"])
teta1 = np.array(fr["teta1"])
teta2 = np.array(fr["teta2"])
teta3 = np.array(fr["teta3"])

B = 1-((4*np.power(1.7,3))/distanze**3)

teta = np.array([round(np.average([teta1[i],teta2[i],teta3[i]]),0) for i in range(0,len(teta1))],dtype=np.int16)

tetaB = teta/B

x = 1/(distanze**2)
plt.plot(x,teta, color="red")
plt.plot(x,tetaB)
plt.xticks(x)
plt.show()