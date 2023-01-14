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


# istogramma
x_indexes = np.arange(len(valore))
plt.bar(x_indexes,ripetizioni) # disegna l'istogramma
plt.yticks(ticks=np.arange(0,max(counter.values())+2,2))
plt.xticks(ticks=x_indexes,labels=valore, rotation=45) # aggiunge titoli asse x

#gaussiana

n = len(valore) * 3
x_val = np.linspace(valore[0],valore[len(valore)-1])
print(x_val)
x = np.arange(n)
#y = np.arange(len(x_val))
y_exp = np.array((1/(np.sqrt(2*np.pi)*sigma)) * np.exp(-(np.power(x_val - media,2)/(2*sigma*sigma))))
#print(y_exp)

plt.plot(x_val,y_exp, color = "#ff0000")

plt.title("r = 3mm d = 10cm N = 100 ") # aggiunge il titolo
plt.xlabel("Misurazione")
plt.ylabel("n ripetizioni")
plt.tight_layout()

plt.show()