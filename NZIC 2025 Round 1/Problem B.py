N = int(input())
K = int(input())

T = 0
for _ in range(N):
    x = int(input())
    if x >= K:
        T += x

print(T)