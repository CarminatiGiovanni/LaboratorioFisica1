from numpy import ndarray
import numpy as np


def calcB(X: ndarray, Y: ndarray) -> float:
    if len(X) != len(Y):
        raise "Non hanno la stessa lunghezza coglione"
    N = len(Y)
    X = np.array(X)
    Y = np.array(Y)
    num = N * np.sum(X * Y) - X.sum() * Y.sum()
    delta = calcDelta(X)
    A = num / delta
    return A


def calcDelta(X: ndarray):
    return len(X) * np.sum(X * X) - np.power(X.sum(), 2)


def calcSigmaB(X: ndarray, Y: ndarray) -> float:
    if len(X) != len(Y):
        raise "Non hanno la stessa lunghezza coglione"
    return np.sqrt(float(len(Y)) / calcDelta(X)) * np.sqrt(((Y - calcB(X, Y) * X) ** 2).sum() / len(Y))


def calcSigmaY_y_Bx(X: ndarray, Y: ndarray) -> float:
    return np.sqrt(((Y - calcB(X, Y) * X) ** 2).sum() / len(Y))


def chiquadro_retta_interpolata(f_obs: ndarray, f_exp: ndarray | float | int, sigmaY: ndarray | float | int,
                                vincoli: int) -> float:
    chi = np.sum(((f_obs - f_exp) ** 2) / (sigmaY ** 2))
    d = (len(f_obs) - vincoli)
    chiridotto = chi / d
    return chiridotto, d
