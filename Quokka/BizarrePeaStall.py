import numpy as np

M = np.array(
    [
        [0.6, 0.6, 0.6, 0.0, 0.0],
        [0.4, 0.0, 0.0, 0.6, 0.0],
        [0.0, 0.4, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.4, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.4, 1.0],
    ]
)


def f(K):
    T = np.zeros((5, 5))
    P = np.identity(5)
    ID = np.identity(5)

    for n in range(1, K + 1):
        T += n * (P @ (M - ID))
        P @= M
        print(n, P)
    return T


def g(K):
    total = 0
    V = np.array([1, 0, 0, 0, 0])
    for n in range(1, K + 1):
        total += n * (M @ V - V)[-1]
        V = M @ V

    return total


# this is the same as doing (M-I)v + 2(M^2 - M)v + 3(M^3 - M^2) + 4(M^4-M^3)...
#
# (M-1)(1 + 2M + 3M^2 + 4M^3)
