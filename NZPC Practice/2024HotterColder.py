import numpy as np
import matplotlib.pyplot as plt

N = int(input())


def perpendicular(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (2*(x1 - x2), 2*(y1 - y2), (x1+x2)*(x2-x1) + (y1+y2)*(y2-y1))


hull = [(0, 0), (0, 10), (10, 10), (10, 10)]
previous = (0.0, 0.0)

plt.xlim(0, 10)
plt.ylim(0, 10)

for _ in range(N):
    x1, y1 = previous
    x2, y2 = map(float, input().split())

    previous = (x2, y2)

    a, b, c = perpendicular((x1, y1), (x2, y2))

    X = np.linspace(0, 10, 100)

    plt.plot(X, (c - a * X) / b)
    plt.show()
