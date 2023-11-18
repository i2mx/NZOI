import math


xhome, yhome, xuni, yuni, N = map(int, input().split())

def distance(P1, P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2) 

points = [(xhome, yhome), (xuni, yuni)]
points[0] = 0

express_paths = set()

for _ in range(N):
    subway = list(map(int, input().split()))[:-2]
    prev = (subway[0], subway[1])

    points.append(prev)

    for i in range(1, len(subway) // 2):
        next_point = (subway[2*i], subway[2*i+1])
        points.append(next_point)
        express_paths.add(tuple(sorted((next_point, prev))))

        prev = next_point

pointsDistance = [10000000000000000000000 for _ in points]

while pointsDistance[1] == 10000000000000000000000:
    min_dist = min(pointsDistance)
    min_point = pointsDistance.index(min_dist)

    for index, point in enumerate(points):
        if point == min_point:
            continue
        if tuple(sorted((point, min_point))) in express_paths:
            pointsDistance[index] = min(pointsDistance[index], min_dist + distance(point, min_point) / 4)
        else:
            pointsDistance[index] = min(pointsDistance[index], min_dist + distance(point, min_point))

print(pointsDistance[1])