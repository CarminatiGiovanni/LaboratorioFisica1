import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as sc

def fdp(x,m,s):
    h = 1./s/np.sqrt(2)
    z = x-m
    return np.exp(-np.power(h*z, 2.)) *h / np.sqrt(np.pi)

fr = pd.read_csv('r=3mm N=100 d=10cm.csv') #fileread
data = np.array(fr['misura r=3mm d = 10cm']) #legge colonna 'misura r=3mm d = 10cm'

N = len(data)
sigma = np.std(data)
sigma_media = sigma/np.sqrt(N)      #sigma tmedio
min_,max_ = min(data),max(data)
media = np.mean(data)               #t medio
var = sigma*sigma                   #varianza

VALORE = "{0:.3f} ± {1:.3f}".format(media,sigma_media)

m = round(media,2) #voglio che la media sia al centro di un intervallo
i = round(sigma/2,2) #voglio che ogni intervallo sia largo sigma/2
offset = round(i/2,3)
bins = np.concatenate((np.flip(np.arange(m - offset - 0.005,min_ - i,-i)),np.arange(m+offset - 0.005,max_,i)))

plt.hist(data,bins=bins, density=True, label= 'data', color="#89c4ff", edgecolor='black')
plt.xticks(bins, rotation=45)

x = np.linspace(min(data),max(data))
y = fdp(x,media,sigma)
plt.plot(x,y,label=f"$G(x;\mu,\sigma)$", color="#ff0000",linewidth='4')

plt.ylabel("Densità di frequenza")
plt.xlabel("$t_{caduta}$ (s)")

plt.legend()
plt.title("Misurazione sfera in caduta nella glicerina\n$\\bf{t_{caduta} = " + str(VALORE) + " s}$\n")
plt.tight_layout()
plt.show()

print(sc.chisquare(data))
