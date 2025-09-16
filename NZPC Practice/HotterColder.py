def perpendicular(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (2*(x2 - x1), 2*(y2 - y1), (x1+x2)*(x2-x1) + (y1+y2)*(y2-y1))

def intersection(p1, p2, lines):
    x1, y1 = p1
    x2, y2 = p2m
    a, b, c = lines

    bottom = a * (x2 - x1) + b * (y2 - y1)
    if bottom == 0:
        return -1

    top = c - a * x1 - b * y1

    return top / bottom

def sign(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    if x > 0:
        return 1

def area(hull):
    A = 0
    N = len(hull)
    for i in range(N):
        A += 1/2 * hull[i][0] * hull[(i + 1) % N][1]
        A -= 1/2 * hull[i][1] * hull[(i + 1) % N][0]

    return abs(A)

N = int(input())

hull = [(0, 0), (0, 10), (10, 10), (10, 0)]
previous = (0.0, 0.0)

for _ in range(N):
    x1, y1 = previous
    x2, y2, direction = input().split()
    x2, y2 = map(float, (x2, y2))

    a, b, c = perpendicular((x1, y1), (x2, y2))

    s = None
    if direction[0] == "C":
        s = sign(a * x1 + b * y1 - c)
    elif direction[0] == "H":
        s = sign(a * x2 + b * y2 - c)
    else:
        ...

    new_points = []

    for i in range(len(hull)):
        xx1, yy1 = hull[i]
        xx2, yy2 = hull[(i + 1) % len(hull)]

        t = intersection((xx1, yy1), (xx2, yy2), (a, b, c))

        ss = a*xx1 + b*yy1 - c
        if sign(ss) == s or abs(ss) < 1e-1:
            new_points.append((xx1, yy1))

        if 0 < t and t < 1:  # an intersection takes place
            xi, yi = xx1*(1-t) + xx2*t, yy1*(1-t) + yy2*t
            new_points.append((xi, yi))

    hull = new_points
    A = area(hull)
    print(f"{A:.2f}")
    previous = (x2, y2)

