import numpy as np

B1 = -1.055272599187094
B2 = -0.21910905266038624

sigmaB1 = 0.042996340094812145
sigmaB2 = 0.032025139553436485

A1 = 2.3376024898062306
A2 = 2.0721283483045583

sigmaA1 = 0.012898902028443645
sigmaA2 = 0.009607541866030947

sigmaY1 = 0.0027896964512156386
sigmaY2 = 0.002077860998515243

T1 = A1 + B1*((A2-A1)/(B1-B2))
T1 = np.round(T1,2)

x = (A2-A1)/(B1-B2)
l = x**2 + 0.15

D = 0.994

g = 4*np.power(np.pi,2)*D/(T1**2)
print(g)

sigmaA1A2 = np.sqrt(sigmaA1**2+sigmaA2**2)
sigmaB1B2 = np.sqrt(sigmaB1**2+sigmaB2**2)

sigmax = np.sqrt((sigmaA1A2/(A2-A1))**2 + (sigmaB1B2/(B1-B2)**2)) * ((A2-A1)/B1-B2)
sigmaProdotto = np.sqrt((sigmax/x)**2 + (sigmaB1/B1)**2) * B1 * x
sigmaT = np.sqrt(sigmaProdotto**2+sigmaA1**2)
print(sigmaT)
sigmag = T1 * 2 * (sigmaT/T1)

print(sigmag)