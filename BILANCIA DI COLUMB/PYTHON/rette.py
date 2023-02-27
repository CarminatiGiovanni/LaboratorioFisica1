import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from A import calcA

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'distanza_varia.csv'

fr = pd.read_csv(FILE)  # fileread
distanze = np.array(fr["d(cm)"])/ 100 #distanze in metri
teta1 = np.array(fr["teta1"])
teta2 = np.array(fr["teta2"])
teta3 = np.array(fr["teta3"])
raggio = 0.017

B = 1-((4*np.power(raggio,3))/distanze**3)

teta = np.array([round(np.average([teta1[i],teta2[i],teta3[i]]),0) for i in range(0,len(teta1))],dtype=np.float32)
tetaRad = (teta/180) * np.pi

tetaRadB = tetaRad/B

x = 1/(distanze**2)
A = calcA(x,tetaRadB)
print(A)
x_A = np.linspace(min(x),max(x),100)
y_A = A*x_A

plt.plot(x_A,y_A,color="green")
plt.plot(x,tetaRad, color="red")
plt.plot(x,tetaRadB)
plt.xticks(x)
plt.show()