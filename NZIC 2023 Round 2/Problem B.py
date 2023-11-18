N = int(input())
C = list(map(int, input().split()))

if sum(C) % N == 0:
    print(0)
    exit()
print(N - sum(C)%N)