import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'misure.csv'

fr = pd.read_csv(FILE)  # fileread