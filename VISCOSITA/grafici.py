import lablib as ll
import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('r=3mm N=100 d=10cm.csv')
mrdt = np.array(data['misura r=3mm d = 10cm']) #misura raggio 3mm distanza 10cm

media = (ll.calc_media(mrdt))
sigma = (ll.calc_sigma(mrdt, media))

print(f"t = {round(media,2)} ± {round(sigma,2)}")

counter = ll.counter_centered_with_ranges(mrdt,0.04)

#counter = Counter(mrdt, sorted=True)

valore = []
ripetizioni = []

for item in counter:
    valore.append(item)
    ripetizioni.append(counter[item])

y_indexes = np.arange(len(valore))

plt.barh(y_indexes,ripetizioni) # disegna l'istogramma

plt.title("r = 3mm d = 10cm N = 100 ") # aggiunge il titolo
plt.yticks(ticks=y_indexes,labels=valore) # aggiunge titoli asse x

plt.ylabel("Misurazione")
plt.xlabel("n ripetizioni")

plt.tight_layout()

plt.show()