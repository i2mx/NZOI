N, D = map(int, input().split())

lights = dict()

for _ in range(D):
    k, p = map(int, input().split())

    for i in range(k, N+1, p):
        if lights.get(i) == None:
            lights[i] = 0

        if lights.get(i) == 0:
            lights[i] = 1
        else:
            lights[i] = 0


for i in range(1, N+1):
    if lights.get(i) == None:
        print("OFF")
    else:
        if lights.get(i) % 2 == 0:
            print("OFF")
        else:
            print("ON")