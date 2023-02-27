import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + "d_fissa_v_uguale_per_ogni_carica"

fr = pd.read_csv(FILE)  # fileread
V = np.array(fr["V"])
teta1 = np.array(fr["teta1"])
teta2 = np.array(fr["teta2"])
teta3 = np.array(fr["teta3"])

teta = np.array([round(np.average([teta1[i],teta2[i],teta3[i]]),0) for i in range(0,len(teta1))],dtype=np.int16)

plt.plot(V**2,teta,'o-')
plt.show()