import numpy as np
import pandas as pd
from typing import Final as const
from matplotlib import pyplot as plt
import scipy.stats as sc
import os
Array = np.array

dir_path = os.path.dirname(os.path.realpath(__file__))
FILE = dir_path + '/../CSV/' + 'T=24.5°C 100 misure d=10cm.csv'

fr = pd.read_csv(FILE)                          #fileread
data = np.array(fr['misura r=3mm d = 10cm'])    #legge colonna 'misura r=3mm d = 10cm'

N:              const = len(data)               # numero di misure
sigma:          const = np.std(data)            # sigma
sigma_media:    const = sigma/np.sqrt(N)        # sigma tmedio
min_,max_             = min(data),max(data)     # massimo e minimo valore
media:          const = np.mean(data)           # t medio
var:            const = sigma*sigma             # varianza (sigma quadro)
CHIquadro:      const = sc.chisquare(data,ddof=2).pvalue       # test del chiquadro

VALORE: str = "{0:.3f} ± {1:.3f}".format(media,sigma_media)

m = round(media,2)      # voglio che la media sia al centro di un intervallo
i = round(sigma/2,2)    # voglio che ogni intervallo sia largo sigma/2
offset = round(i/2,3)   # per avere i valori del tipo 0.005 per far si che ogni misura cada in un preciso intervallo
bins = np.concatenate((np.flip(np.arange(m - offset - 0.005,min_ - i,-i)),np.arange(m+offset - 0.005,max_+i,i))) # crea una lista di valori centrata

plt.figure("Analisi dati raccolti") # da il nome al pannello

plt.hist(data,bins=bins, density=True, label= 'data', color="#89c4ff", edgecolor='black') # disegna istogramma
plt.xticks(bins[:-1], rotation=45)

x: Array = np.linspace(min_,max_)    # array ad alta densità
y: Array = sc.norm.pdf(x,media,sigma) # y della distribuzione normale ad alta densità
plt.plot(x,y,label=f"$G(x;\mu,\sigma)$", color="#ff0000",linewidth='4') # sovrappone al hist la gaussiana
""
description: str = "" + "$\\bar{t}$ = " + str(round(media,3)) + ", $\sigma$ = " + str(round(sigma,2)) + ", $\sigma^2$ = " + str(round(var,2)) + ", pvalue($\\tilde{\\chi}^2$) = " + str(CHIquadro * 100) + '%'

plt.ylabel("Densità di frequenza")
plt.xlabel("$t_{caduta}$ (s)" + '\n\n' + description)

plt.legend()
plt.title("Misurazione sfera in caduta nella glicerina\n$\\bf{t_{caduta} = " + str(VALORE) + " s}$\n")
plt.tight_layout()
plt.show()
