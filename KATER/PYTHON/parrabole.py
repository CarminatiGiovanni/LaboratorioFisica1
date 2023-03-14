import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'parabole.csv'
fr = pd.read_csv(FILE)

d = np.array(fr['d1(cm)'])


a3 = np.array([7.0,7.5,8.0,8.5,9.0,9.5])
a1 = np.array([2.0557, 2.0511, 2.0418, 2.0305, 2.018,  2.0109])
a2 = np.array([2.0134, 2.0122, 2.0112, 2.0087, 2.0066, 2.0038])



t1 = np.array(fr['t1'])
t2 = np.array(fr['t2'])



plt.plot(d,t1,'o-',label="t1")
plt.plot(d,t2,'o-',label='t2')
plt.plot(a3,a1,'o-',color="blue")
plt.plot(a3,a2,'o-',color="lime")
plt.legend()
plt.xticks(d)
plt.show()