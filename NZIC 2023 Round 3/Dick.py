import math
import bisect

xR, yR, xL, yL = map(float, input().split())
N = int(input())

def dist(p1, p2):
    x1,y1 = p1
    x2,y2 = p2

    dx = x1-x2
    dy = y1-y2

    return math.sqrt(dx**2 + dy**2)

def dist_shaded(p1,p2):
    return max(dist(p1,p2) - point_radius[p1] - point_radius[p2], 0)

points = [(xR,yR)]

point_dist = {(xR, yR): 0, (xL, yL): math.inf}
point_radius = {(xR, yR): 0, (xL, yL): 0}
path_queue = {}

for _ in range(N):
    x,y,r = map(float, input().split())
    point_dist[(x,y)] = math.inf
    point_radius[(x,y)] = r
    
    points.append((x,y))

points.append((xL, yL))

# print(points)

# path_queue = [(0, (xR, yR))]

# while len(path_queue) > 0:
#     if len(path_queue) > 10000:
#         1/0


#     distance, point = path_queue.pop(0)
#     if distance > point_dist[point]:
#         continue

    
#     for newpoint in point_dist:
#         if newpoint != point:
#             if distance + dist(point, newpoint) - point_radius[newpoint] - point_radius[point] < point_dist[newpoint]:
#                 point_dist[newpoint] = distance + dist_shaded(point, newpoint) 

#                 bisect.insort(path_queue, (point_dist[newpoint], newpoint))
    
# print(point_dist[(xL, yL)])

from heapq import heappop, heappush

# def dijkstra(graph, start):
    # """ 
        # Uses Dijkstra's algortihm to find the shortest path from node start
        # to all other nodes in a directed weighted graph.
    # """
n = len(points)
dist[start] = 0

queue = [(0, start)]
while queue:
    path_len, v = heappop(queue)
    if path_len == dist[v]:
        for w, edge_len in graph[v]:
            if edge_len + path_len < dist[w]:
                dist[w], parents[w] = edge_len + path_len, v
                heappush(queue, (edge_len + path_len, w))

return dist, parents

