N, K = map(int,input().split())

d = list(map(int,input().split()))
d.sort()

print(sum(d[N-K::]))

