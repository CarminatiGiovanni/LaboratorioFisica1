import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from interpolazione2 import RettaInterpolata

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'caduta_libera.csv'
fr = pd.read_csv(FILE)

d = np.array(fr['h'])*0.01
t = np.array(fr['AVG t']) * 0.001


