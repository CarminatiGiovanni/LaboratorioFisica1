import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

fr = pd.read_csv('T=18,5.csv') #fileread

mm2 = np.array(fr["2"])
mm3 = np.array(fr["3"])
mm4 = np.array(fr["4"])
mm5 = np.array(fr["5"])
mm6 = np.array(fr["6"])

data = np.array([mm2,mm3,mm4,mm5,mm6])

t_medie = np.array([])

for i in data:
    t_medie = np.append(t_medie,round(np.mean(i),5))

v_medie = 0.2/t_medie

print(v_medie)


plt.plot([2,3,4,5,6],v_medie, 'ro')
plt.plot([4,9,16,25,36],v_medie, 'go', color="#1ff24a")
plt.show()


