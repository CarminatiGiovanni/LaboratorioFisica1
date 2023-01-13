import numpy as np
import lablib as ll
import matplotlib.pyplot as plt

dati = np.array([3.16,3.08,2.92,3.17,2.90,3.01,3.06,3.00,2.88,2.84,2.87,2.92,3.01,2.84,2.87,3.02,3.04,3.05,2.93,2.95,2.90,2.95,2.90,2.96,3.09,2.96,3.02,3.04,3.01,2.91,2.92,2.91,3.00,3.00,2.96,3.05,2.93,2.98,3.03,2.96,2.99,2.90,2.91,2.99,3.02,2.93,2.91,2.90,2.94,2.87,2.90,2.99,2.93,3.05,3.05,2.98,2.97,2.98,3.09,2.93,3.00,3.00,2.90,2.96,3.05,3.02,3.02,2.93,3.07,2.98,2.96,3.06,3.10,3.06,2.92,3.12,3.07,3.00,2.92,3.10,3.07,3.02,2.97,3.08,3.15,2.89,2.98,3.05,3.09,3.03,2.89,2.93,2.99,2.90,3.06,2.95,3.02,2.89,2.95,2.91])

dati.sort()

N = len(dati)
media = ll.calc_media(dati)
dev_standard = ll.calc_deviazione_standard(dati, media, N)
errore_standard = dev_standard/np.sqrt(N)

print("N: ",len(dati))
print("media: ", media)
print("deviazione standard: ", dev_standard)
print("errore standard: ", errore_standard)

counts, bins = np.histogram(dati)
plt.stairs(counts, bins)
plt.show()
# plt.hist(bins[:-1], bins, weights=counts)
