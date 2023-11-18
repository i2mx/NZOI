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

from heapq import heappop, heappush

n = len(points)

queue = [(0, (xR, yR))]
while queue:
    path_len, v = heappop(queue)
    
    if path_len == point_dist[v]:
    
        if v == (xL, yL):
            print(path_len)
            exit()
    
        for w in points:
            if w == v:
                continue
            d = dist_shaded(w,v)

            if d + path_len < point_dist[w]:
                point_dist[w] = d + path_len
                heappush(queue, (d + path_len, w))

# print(point_dist[(xL, yL)])
