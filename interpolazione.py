import numpy as np
from numpy import ndarray

class RettaInterpolata():
    def __init__(self, X: ndarray, Y: ndarray, sigmaY_strumento: ndarray | float, relazione: str) -> None:
        if len(X) != len(Y):
            raise("len(X) deve essere uguale len(Y)")
        if relazione != 'A+BX' and relazione != 'BX':
            raise("relazione deve essere o 'A+BX' o 'BX'")
        if type(sigmaY_strumento) == type(ndarray) and len(sigmaY_strumento) != len(X):
            raise("Se per ogni valore c'è un sigmaY_strumento differente len(sigmaY) deve essere uguale a len(X)")
        self.X = X
        self.Y = Y
        self.N = len(X)
        self.delta = self.__calcDelta()
        self.B = self.__calcB()
        self.best_x = np.linspace(min(self.X), max(self.X), 100)
        self.relazione = relazione

        if relazione == 'BX':
            self.sigmay = self.__calcSigmaY_BX()
            self.best_y = self.B*self.best_x
            self.ddof = 1
        else:
            self.A = self.__calcA()
            self.sigmay = self.__calcSigmaY_A_BX()
            self.sigmaA = self.__calcSigmaA()
            self.best_y = self.B*self.best_x + self.A
            self.ddof = 2

        self.sigmaB = self.__calcSigmaB()
        self.sigmay = np.sqrt(self.sigmay**2 + sigmaY_strumento**2)
        self.df = self.N - self.ddof # gradi di libertà

        self.chiquadro_osservato = self.__chiquadro()
        self.chiquadro_osservato_ridotto = self.chiquadro_osservato / self.df
    
    def __calcDelta(self):
        return self.N*np.sum(self.X**2)-np.power(self.X.sum(),2)
    
    def __calcB(self) -> float:
        return (self.N*np.sum(self.X*self.Y) - self.X.sum() * self.Y.sum()) / self.delta
    
    def __calcA(self) -> float:
        return ((self.X**2).sum()*self.Y.sum() - self.X.sum()*(self.Y*self.X).sum()) / self.delta
    
    def __calcSigmaY_A_BX(self) -> float:
        return np.sqrt(((self.Y - self.A - self.B * self.X) ** 2).sum() / self.N)
    
    def __calcSigmaY_BX(self) -> float:
        return np.sqrt(((self.Y - self.B * self.X) ** 2).sum() / self.N)
    
    def __calcSigmaB(self) -> float:
        return np.sqrt(self.N/self.delta) * self.sigmay
    
    def __calcSigmaA(self) -> float:
        return np.sqrt(np.sum(self.X ** 2) / self.delta) * self.sigmay
    
    def __chiquadro(self) -> float:
        if self.relazione == 'BX':
            return np.sum(((self.Y - self.B*self.X)/self.sigmay)**2)
        if self.relazione == 'A+BX':
            return np.sum(((self.Y - self.A - self.B*self.X)/self.sigmay)**2)