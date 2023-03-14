import numpy as np
from numpy import ndarray, float64

class RettaInterpolata():
    def __init__(self, X: ndarray[float64], Y: ndarray[float64], sigmaY_strumento: ndarray[float64] | float64 = 0) -> None:
        if len(X) != len(Y):
            raise("len(X) deve essere uguale len(Y)")
        if type(sigmaY_strumento) == type(ndarray) and len(sigmaY_strumento) != len(X):
            raise("Se per ogni valore c'è un sigmaY_strumento differente len(sigmaY) deve essere uguale a len(X)")
        self.X = X
        self.Y = Y
        self.N = len(X)
        self.delta = self.__calcDelta()
        self.B = self.__calcB()
        self.best_x = np.linspace(min(self.X), max(self.X), 100)
        self.A = self.__calcA()
        self.sigmaY = self.__calcSigmaY_A_BX()
        self.sigmaY = np.sqrt(self.sigmaY**2 + sigmaY_strumento**2) # propaga errore
        self.sigmaA = self.__calcSigmaA()
        self.t_test = self.__t_test()
        self.linearita = 'BX' if self.t_test else 'A+BX'

        if self.t_test:
            self.sigmaY = self.__calcSigmaY_BX() # ricalcola sigmaY
            self.sigmaY = np.sqrt(self.sigmaY**2 + sigmaY_strumento**2)

            self.best_y = self.B*self.best_x
            self.ddof = 1
        else:
            self.A = self.__calcA()
            self.best_y = self.B*self.best_x + self.A
            self.ddof = 2

        self.sigmaB = self.__calcSigmaB()
        self.df = self.N - self.ddof # gradi di libertà

        self.chiquadro_osservato = self.__chiquadro()
        self.chiquadro_osservato_ridotto = self.chiquadro_osservato / self.df
    
    def __calcDelta(self):
        return self.N*np.sum(self.X**2)-np.power(self.X.sum(),2)
    
    def __calcB(self) -> float64:
        return (self.N*np.sum(self.X*self.Y) - self.X.sum() * self.Y.sum()) / self.delta
    
    def __calcA(self) -> float64:
        return ((self.X**2).sum()*self.Y.sum() - self.X.sum()*(self.Y*self.X).sum()) / self.delta
    
    def __calcSigmaY_A_BX(self) -> float64:
        return np.sqrt(((self.Y - self.A - self.B * self.X) ** 2).sum() / self.N)
    
    def __calcSigmaY_BX(self) -> float64:
        return np.sqrt(((self.Y - self.B * self.X) ** 2).sum() / self.N)
    
    def __calcSigmaB(self) -> float64:
        return np.sqrt(self.N/self.delta) * self.sigmaY
    
    def __calcSigmaA(self) -> float64:
        return np.sqrt(np.sum(self.X ** 2) / self.delta) * self.sigmaY
    
    def __chiquadro(self) -> float64:
        return np.sum(((self.Y - self.B*self.X)/self.sigmaY)**2) if self.t_test else np.sum(((self.Y - self.A - self.B*self.X)/self.sigmaY)**2)
    
    def __t_test(self) -> bool:
        return 0>= self.A - 2*self.sigmaA.all() and 0 <= self.A + 2*self.sigmaA.all()
    
    def __repr__(self) -> str:
        a = f"A: {self.A}\nsigmaA: {self.sigmaA}" if not self.t_test else ""
        return f"""
linearità: {self.linearita}
B: {self.B}
sigmaB: {self.sigmaB}
{a}
sigmaY: {self.sigmaY}

chiquadro osservato: {self.chiquadro_osservato}
chiquadro ridotto: {self.chiquadro_osservato_ridotto}
gradi di libertà: {self.df}
vincoli: {self.ddof}
        """
    
def main():
    X,Y = np.array([1,2,3,4]), np.array([1,2,4,4])
    r = RettaInterpolata(X,Y)
    print(r)


if __name__ == '__main__':
    main()