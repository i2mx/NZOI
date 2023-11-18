N, M = map(int, input().split())
edges = dict([ (i, []) for i in range(1, N+1) ])

swaps_required = [ 0 for i in range(N)]
color = [ 1 for i in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)