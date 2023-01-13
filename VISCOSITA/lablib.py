import numpy as np
def calc_media(d):
    med = 0
    for i in d:
        med += i
    return med/len(d)

def calc_deviazione_standard(d, m, N):
    sum = 0
    for i in d:
        sum += pow((i - m),2)
    return np.sqrt(sum/(N-1))