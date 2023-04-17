from matplotlib import pyplot as plt
import numpy as np

MAX_ITER = 80

def mandelbrot(c: complex,x,y):
    z = 0
    n = 0
    x_, y_ = [],[]
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        x_.append(z.real)
        y_.append(z.imag)
        n += 1
    if n == MAX_ITER:
        x.extend(x_)
        y.extend(y_)


x, y = [],[]

if __name__ == "__main__":
    for a in np.linspace(-1,1,200):
        for b in np.linspace(-1,1,200):
            c = complex(a, b)
            mandelbrot(c,x, y)
    
    plt.plot(x,y,',')
    plt.show()