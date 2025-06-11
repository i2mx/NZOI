# why was y9 me legit better?

import heapq

# R is the number of rocket types available, N is the number of players, and
# T is the number of tiles on the board
R, N, T = map(int, input().split())
inf = 1_000_000_000_000_000_000

# each rocket is a tuple (c,f) indicating the cost of using the rocket and the
# distance it will propel you or the "fuel" of the rocket

rockets = [tuple(map(int, input().split())) for _ in range(R)]

distances = [inf for _ in range(T)]
distances[0] = 0

visited = [False for _ in range(T)]

pq = [(0, 0)]
heapq.heapify(pq)

while pq:
    dist, x = heapq.heappop(pq)
    if visited[x]:
        continue

    visited[x] = True

    for c, f in rockets:
        if x + f < T:
            new_x = x + f
            if not visited[new_x] and dist + c < distances[new_x]:
                distances[new_x] = dist + c
                heapq.heappush(pq, (dist + c, new_x))
        if x - f < 0:
            new_x = abs(f - x)
            if not visited[new_x] and dist + c < distances[new_x]:
                distances[new_x] = dist + c
                heapq.heappush(pq, (dist + c, new_x))

# print(distances)

for _ in range(N):
    player = int(input())
    print(distances[player])

# NOTE:
# There are only a few types of rockets??? and a few tiles so this looks like dp
