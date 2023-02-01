import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as sc

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'T=24.5°C 100 misure d=10cm.csv'

fr = pd.read_csv(FILE) #fileread
data = np.array(fr['misura r=3mm d = 10cm']) #legge colonna 'misura r=3mm d = 10cm'

def fdp(x,m,s): # numpy.array
    h = 1./s/np.sqrt(2)
    z = x-m
    return np.exp(-np.power(h*z, 2.)) *h / np.sqrt(np.pi)

N = len(data)
sigma = np.std(data)
sigma_media = sigma/np.sqrt(N)      #sigma tmedio
min_,max_ = min(data),max(data)
media = np.mean(data)               #t medio
var = sigma*sigma                #varianza
CHIquadro = sc.chisquare(data,ddof=2)

print(

f"""
    max: {max_}
    min: {min_}
    media: {media}
    sigma: {sigma}
"""

)

VALORE: str = "{0:.3f} ± {1:.3f}".format(media,sigma_media)

m = round(media,2) #voglio che la media sia al centro di un intervallo
i = round(sigma/2,2) #voglio che ogni intervallo sia largo sigma/2
offset = round(i/2,3)
bins = np.concatenate((np.flip(np.arange(m - offset - 0.005,min_ - i,-i)),np.arange(m+offset - 0.005,max_+i,i)))

plt.figure("Analisi dati raccolti")

plt.hist(data,bins=bins, density=True, label= 'data', color="#89c4ff", edgecolor='black')
plt.xticks(bins[:-1], rotation=45)

x = np.linspace(min_,max_)
y = fdp(x,media,sigma)
plt.plot(x,y,label=f"$G(x;\mu,\sigma)$", color="#ff0000",linewidth='4')

plt.ylabel("Densità di frequenza")
plt.xlabel("$t_{caduta}$ (s)")

plt.legend()
plt.title("Misurazione sfera in caduta nella glicerina\n$\\bf{t_{caduta} = " + str(VALORE) + " s}$\n")
plt.tight_layout()
plt.show()
