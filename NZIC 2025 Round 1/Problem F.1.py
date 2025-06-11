from collections import Counter
import sys


# for the tree case there probably is a way to do this with the lowest common ancestor?
# overcooked that bridge stuff for nothing brah

sys.setrecursionlimit(2**31 - 1)


N, M = map(int, input().split())

if M == N-1:
    from collections import Counter
    import sys


    # for the tree case there probably is a way to do this with the lowest common ancestor?
    # overcooked that bridge stuff for nothing brah

    sys.setrecursionlimit(2**31 - 1)


    # N, M = map(int, input().split())
    inf = 1e69
    # N lakes connected by M channels
    # GRAPH THEORY
    # connected, undirected graph

    # this is a list denoting the `type' of each lake
    lure = list(map(int, input().split()))
    cc = Counter(lure)
    og_pairs = 0
    for k, v in cc.items():
        og_pairs += v * (v - 1) // 2
    # print(og_pairs)

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [-1 for _ in range(N)]
    parent[0] = 0
    stack = [0]
    depth = [0 for _ in range(N)]

    while len(stack) > 0:
        cur = stack.pop()
        for nei in graph[cur]:
            if parent[nei] == -1:
                parent[nei] = cur
                stack.append(nei)
                depth[nei] = depth[cur] + 1

    jumps = [[None for _ in range(N)] for _ in range(40)]
    for i in range(N):
        jumps[0][i] = parent[i]

    for i in range(1, 40):
        for j in range(N):
            jumps[i][j] = jumps[i - 1][jumps[i - 1][j]]


    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a

        diff = depth[a] - depth[b]
        for i in range(20):
            if (diff >> i) & 1:
                a = jumps[i][a]

        if a == b:
            return a

        for i in range(19, -1, -1):
            if jumps[i][a] != jumps[i][b]:
                a = jumps[i][a]
                b = jumps[i][b]

        return parent[a]


    # check if a,b is on the path from u to v
    def is_edge_on_path(u, v, a, b):
        if lca(a, b) != a:
            a, b = b, a
        return lca(u, v) == b or (lca(u, b) == b and lca(v, b) == b)

    max_ans = 0
    for a in range(N):
        for b in graph[a]:
            pairs = 0
            # a,b is removed
            for u in range(N):
                for v in range(N):
                    if lure[u] != lure[v] or u > v:
                        continue

                    # if is_edge_on_path(u, v, a, b):
                    #     pairs += 1
                    lc = lca(u, v)
                    if (
                        lca(a, lc) == lc
                        and lca(b, lc) == lc
                        and (
                            (lca(a, u) == a or lca(a, v) == a)
                            and (lca(b, v) == b and lca(b, v) == b)
                        )
                    ):
                        pairs += 1
            max_ans = max(max_ans, pairs)
    print(max_ans)
    exit()
inf = 1e69
# N lakes connected by M channels
# GRAPH THEORY
# connected, undirected graph

# this is a list denoting the `type' of each lake
lure = list(map(int, input().split()))
cc = Counter(lure)
og_pairs = 0
for k, v in cc.items():
    og_pairs += v * (v - 1) // 2
# print(og_pairs)

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bridge finding
# -------------------------------------------------------------
do_bridge = False

if do_bridge:
    time = 0
    visited = [False for _ in range(N)]
    dis = [inf for _ in range(N)]
    low = [inf for _ in range(N)]
    parent = [-1 for _ in range(N)]
    bridges = []

    def dfs(cur):
        global visited
        global dis
        global low
        global parent
        global time

        visited[cur] = True
        dis[cur] = time
        low[cur] = time
        time += 1

        for nei in graph[cur]:
            if not visited[nei]:
                parent[nei] = cur
                dfs(nei)
                low[cur] = min(low[cur], low[nei])
                if low[nei] > dis[cur]:
                    bridges.append((cur, nei))
            elif nei != parent[cur]:
                low[cur] = min(low[cur], dis[nei])

    for i in range(N):
        if not visited[i]:
            dfs(i)


def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)

    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[-node - 1] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(-node - 1)
            stack += graph[node]
    return SCC[::-1]


# print(bridges)
min_pairs = inf
# -------------------------------------------------------------

if do_bridge is True:
    for bridge in bridges:
        a, b = bridge
        graph[a].remove(b)
        graph[b].remove(a)

        scc = find_SCC(graph)

        pairs = 0
        for component in scc:
            lure_types = list(map(lambda x: lure[x], component))
            c = Counter(lure_types)
            # find the number of pairs of the same type
            for k, v in c.items():
                pairs += v * (v - 1) // 2
        # print(pairs)
        min_pairs = min(min_pairs, pairs)

        graph[a].append(b)
        graph[b].append(a)
else:
    for a in range(N):
        for b in graph[a]:
            graph[a].remove(b)
            graph[b].remove(a)

            scc = find_SCC(graph)

            pairs = 0
            for component in scc:
                lure_types = list(map(lambda x: lure[x], component))
                c = Counter(lure_types)
                # find the number of pairs of the same type
                for k, v in c.items():
                    pairs += v * (v - 1) // 2
            # print(pairs)
            min_pairs = min(min_pairs, pairs)

            graph[a].append(b)
            graph[b].append(a)


print(og_pairs - min_pairs)
