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
        
def counter_centered_with_ranges(dati: list, sigma: float) -> dict[float,int]:
    max_ = max(dati)
    min_ = min(dati)
    media_ = calc_media(dati)
    media_ = round(media_,2)
    ciffre_significative = len(str(sigma)) - str(sigma).find('.') - 1
    correzione_decimale = 5 * pow(10, - (ciffre_significative + 1)) # aggiungo una ciffra significativa per non avere valori a metà tra due intervalli
    x_values = np.arange(min_ +0.01 - correzione_decimale, max_ + sigma/2, sigma)

    count = dict()
    for x in x_values:
        count[round(x,ciffre_significative +1)] = 0
    for d in dati:
        index = binarySearch(x_values,0,len(x_values)-1,d,round(sigma/2,ciffre_significative + 1))
        count[round(x_values[index],ciffre_significative+1)] += 1
    return count

def binarySearch(arr, low, high, key, r):
 
    mid = (low + high)/2
 
    if (key <= arr[int(mid)] + r and key >= arr[int(mid)] - r):
        return int(mid)
 
    if (key > arr[int(mid)]):
        return binarySearch(arr, (mid + 1), high, key, r)
 
    if (key < arr[int(mid)]):
        return binarySearch(arr, low, (mid-1), key, r)
 
    return 0