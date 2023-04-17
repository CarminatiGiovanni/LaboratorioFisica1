from matplotlib import pyplot as plt
import numpy as np

fixed_x = [0,300,150]
fixed_y = [0,0,150*np.sqrt(3)]

x, y = list(fixed_x),list(fixed_y)

last = (150,100)

x.append(last[0])
y.append(last[1])

for n in np.random.rand(1000000):
    n = int(n*3)
    next_ = ((last[0] + fixed_x[n])/2, (last[1] + fixed_y[n])/2,)
    last = next_
    x.append(last[0])
    y.append(last[1])


plt.plot(x,y,',')
plt.show()