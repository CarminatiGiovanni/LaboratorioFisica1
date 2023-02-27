import numpy as np

def calcA(X, Y) -> float:
    if len(X) != len(Y):
        raise "Non hanno la stessa lunghezza coglione"
    N = len(Y)
    X = np.array(X)
    Y = np.array(Y)
    num = N*np.sum(X*Y) - X.sum() * Y.sum()
    delta = N*np.sum(X*X)-np.power(X.sum(),2)
    A = num/delta
    return A