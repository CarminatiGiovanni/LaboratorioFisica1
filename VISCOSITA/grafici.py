import lablib as ll
import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('r=3mm N=100 d=10cm.csv')
mrdt = np.array(data['misura r=3mm d = 10cm']) #misura raggio 3mm distanza 10cm
mrdt.sort()

media = ll.calc_media(mrdt)
sigma = ll.calc_sigma(mrdt, media)

print(f"t = {media} ± {sigma}")

counter = Counter(mrdt)

valore = []
ripetizioni = []

for item in counter:
    valore.append(item)
    ripetizioni.append(counter[item])

x_indexes = np.arange(len(valore))

plt.bar(x_indexes,ripetizioni) # disegna l'istogramma

plt.title("r = 3mm d = 10cm N = 100 ") # aggiunge il titolo
plt.xticks(ticks=x_indexes,labels=valore) # aggiunge titoli asse x

plt.xlabel("Misurazione")
plt.ylabel("n ripetizioni")

plt.tight_layout()

plt.show()