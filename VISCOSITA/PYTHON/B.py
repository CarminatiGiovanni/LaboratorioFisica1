import numpy as np

def calcB(X, Y) -> float:
    if len(X) != len(Y):
        raise "Non hanno la stessa lunghezza coglione"
    N = len(Y)
    X = np.array(X)
    Y = np.array(Y)
    num = N*np.sum(X*Y) - X.sum() * Y.sum()
    delta = calcDelta(X)
    B = num/delta
    return B

def calcA(X,Y) -> float:
    return ((X**2).sum()*Y.sum() - X.sum()*(Y*X).sum()) / calcDelta(X)

def calcDelta(X):
    return len(X)*np.sum(X*X)-np.power(X.sum(),2)

def calcSigmaY_y_A_BX(X, Y) -> float:
    return np.sqrt(((Y - calcA(X,Y) - calcB(X,Y) * X) ** 2).sum() / len(Y))

def calcSigmaB(X, Y) -> float:
    if len(X) != len(Y):
        raise "Non hanno la stessa lunghezza coglione"
    return np.sqrt(float(len(Y))/calcDelta(X))*calcSigmaY_y_A_BX(X, Y)

def calcSigmaY_y_Bx(X, Y) -> float:
    return np.sqrt(((Y - calcB(X, Y) * X) ** 2).sum() / len(Y))

def calcSigmaA(X, Y) -> float:
    return calcSigmaY_y_A_BX(X, Y)*np.sqrt(np.sum(X ** 2) / calcDelta(X))