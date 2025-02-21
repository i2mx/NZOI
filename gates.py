# https://train.nzoi.org.nz/problems/795

# import bisect

G = int(input())
P = int(input())

gates = [False for _ in range(G)]

for count in range(P):
    gi = int(input())
    i = gi - 1
    while gates[i]:
        i -= 1
        if i < 0:
            print(count)
            exit()
    gates[i] = True
print(count)