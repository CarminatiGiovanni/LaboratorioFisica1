import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def gauss(x,m,s):
    h = 1./s/np.sqrt(2)
    z = x-m
    return np.exp(-np.power(h*z, 2.)) *h / np.sqrt(np.pi)

# plt.style.use("fivethirtyeight")

fr = pd.read_csv('r=3mm N=100 d=10cm.csv') #fileread
data = np.array(fr['misura r=3mm d = 10cm']) #legge colonna '...'

sigma = np.std(data)
media = round(np.mean(data),2)

VALORE = "{0:.2f} ± {1:.2f}".format(media,sigma)

spacing = np.arange(min(data),max(data), sigma/2)
plt.hist(data, bins=spacing, density=True, label= 'data', color="#89c4ff")

x = np.linspace(min(data),max(data))
y = gauss(x,media,sigma)
plt.plot(x,y,label=f"$G(x;\mu,\sigma)$", color="#ff0000",linewidth='4')

plt.ylabel("Densità di frequenza")
plt.xlabel("$t_{caduta}$ (s)")

plt.legend()
plt.title("Misurazione sfera in caduta nella glicerina\n$\\bf{t_{caduta} = " + str(VALORE) + " s}$")
plt.show()

