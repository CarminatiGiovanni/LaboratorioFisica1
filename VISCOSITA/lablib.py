import numpy as np
def calc_media(dati: list) -> float:
    med = 0
    for i in dati:
        med += i
    return med/len(dati)

def calc_sigma_quadro(dati: list, media: float) -> float:
    sum = 0
    for i in dati:
        sum += pow((i - media),2)
    return sum/(len(dati)-1)

def calc_sigma(dati: list,media: float) -> float:
    return np.sqrt(calc_sigma_quadro(dati,media)/np.sqrt(len(dati)))
