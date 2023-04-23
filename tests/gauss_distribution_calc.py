import matplotlib.pyplot as plt
import numpy as np

def gauss_dist(x,m,s):
    coeff = 1 / (s*np.sqrt(2*np.pi))
    exp = np.exp(-0.5*((m-x)/s)**2)
    return coeff * exp

media = 0
sigma = 2

valore_vero = 1

t = np.abs(media - valore_vero) / sigma

x = np.linspace(media - 3 * sigma, media + 3 * sigma,1000)
y = gauss_dist(x,media,sigma)

plt.plot(x,y)
plt.fill_between(
    x= x,y1= y,where= (media - t < x)&(x < media + t),
    color= "b",alpha= 0.2)

plt.show()
