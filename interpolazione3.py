import numpy as np
from numpy import ndarray, float64
from scipy.optimize import curve_fit

class RettaInterpolata():
    def __init__(self, X: ndarray[float64], Y: ndarray[float64], sigmaY_strumento: ndarray[float64] | float64 = 0) -> None:
        if len(X) != len(Y):
            raise("len(X) deve essere uguale len(Y)")
        if type(sigmaY_strumento) == type(ndarray) and len(sigmaY_strumento) != len(X):
            raise("Se per ogni valore c'è un sigmaY_strumento differente len(sigmaY) deve essere uguale a len(X)")
        
        self.X = X
        self.Y = Y
        self.N = len(X)

        def f(x, A, B):
            return A + B * x
        
        AB, sigma = curve_fit(f,X,Y,p0 = [Y[0], (Y[1] - Y[0]) / (X[1] - X[0])])
        self.A, self.B = AB
        self.sigmaA, self.sigmaB = np.sqrt(np.diag(sigma))
        self.sigmaY = np.sqrt(self.__sigmaY()**2 + sigmaY_strumento**2)
        self.df = self.N - 2
        self.rchisquare = self.__rchisquare() 

        self.x_best = np.linspace(min(X),max(X),100)
        self.y_best = self.A + self.B * self.x_best

    def __sigmaY(self):
        return np.sqrt(np.sum( (self.Y - self.A - self.B * self.X)**2 ) / (self.N - 2))
        
    def __rchisquare(self):
        exp_val = self.A + self.B * self.X
        return np.round(np.sum((self.Y - exp_val)**2 / exp_val) / self.df,2)

    def __repr__(self) -> str:
        return f"""
linearità A + BX
    
A: {self.A} 
B: {self.B}
sigmaA: {self.sigmaA}
sigmaB: {self.sigmaB}

sigmaY: {self.sigmaY}
chiquadro ridotto: {self.rchisquare}
df: {self.df}
    
"""


class Interpolazione:
    def __init__(self,X: ndarray[float64], Y: ndarray[float64],f,p0 = None, sigmaY_strumento: ndarray[float64] | float64 = 0, names: list[str] = None) -> None:
        self.f = f
        self.Y = Y
        self.X = X
        self.N = len(X)

        self.bval, self.cov_matrix = curve_fit(f,X,Y,p0=p0)
        self.sigma_bval = np.sqrt(np.diag(self.cov_matrix))

        self.sigmaY = np.sqrt(self.__sigmaY()**2 + sigmaY_strumento**2)
        self.df = self.N / len(self.bval)

        self.rchisquare = self.__rchisquare()

        self.x_best = np.linspace(min(X),max(X),100)
        self.y_best = f(self.x_best,*self.bval)

        if names != None:
            self.bval = {x : y for x,y in zip(names,self.bval)}
            self.sigma_bval = {x : y for x,y in zip(names,self.sigma_bval)}

    def __sigmaY(self):
        return np.sqrt(np.sum( (self.Y - self.f(X,*self.bval))**2 ) / (self.N - len(self.bval)))

    def __rchisquare(self):
        exp_val = self.f(self.X,*self.bval)
        return np.round(np.sum((self.Y - exp_val)**2 / exp_val) / self.df, 2)

    def __repr__(self) -> str:
        return f"""   
Parameters: {self.bval} 
Sigma parameters: {self.sigma_bval}

sigmaY: {self.sigmaY}
chiquadro ridotto: {self.rchisquare}
df: {self.df}

covariance matrix: {self.cov_matrix}    
"""


def final_val(x,sigma,decimals = 2,exp = 0, udm: str = '') -> str:
    x = np.round(x*np.power(10,-exp),decimals)
    sigma = np.round(sigma*np.power(10,-exp),decimals)
    return f'{x} ± {sigma} {udm}' if exp == 0 else f'({x} ± {sigma})e{exp} {udm}'

if __name__ == '__main__':

    val = 0.51543e-12
    sigma_val = 1.543e-15
    print(final_val(val,sigma_val,exp=-14, decimals=3))


    # import matplotlib.pyplot as plt

    # X,Y = np.array([1,2,3,4,5,6,7,8], dtype=float64), np.array([1,2,4,4,7,9,10,12],dtype=float64)
    # #r = RettaInterpolata(X,Y)
    
    # def ret(x,A,B):
    #     return A + B*x
    
    # r = Interpolazione(X,Y,ret)
    # plt.errorbar(X,Y,fmt='o', yerr=r.sigmaY, capsize=7, color='red', ecolor='black')
    # plt.plot(r.x_best,r.y_best)
    # plt.show()
    # print(r)

    # def f(x,a,b,c):
    #     return a*x**2 + b*x + c
    
    # X,Y = np.array([1,2,3,4,5,6,7,8], dtype=float64), np.array([1,3,10,15,28,33,45,64],dtype=float64)

    # r = Interpolazione(X,Y,f,names=['a','b','c'])
    # # print(r)
    # plt.errorbar(X,Y,fmt='o', yerr=r.sigmaY, capsize=7, color='red', ecolor='black')
    # plt.plot(r.x_best,r.y_best)
    # plt.show()