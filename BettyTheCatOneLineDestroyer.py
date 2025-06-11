A, B, K = map(int, input().split())
inf = 1E10
small, big = min(A, B), max(A, B)
lim = big+1
minimum = (inf, inf)

for i in range(lim):
    C = (K-i*small) // big
    lesser = abs((C*big + i*small) - K)
    larger = abs(((C+1)*big + i*small) - K)
    if lesser <= larger and C >= 0:
        minimum = min(minimum, (lesser, i+C))
    elif C+1 >= 0:
        minimum = min(minimum, (larger, i+1+C))
print(minimum[0], minimum[1])