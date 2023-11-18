import collections
from functools import reduce
import itertools

N, K = map(int, input().split())

points = list(map(int, input().split()))
count_points = collections.Counter(points)

classes = len(count_points)

total = 0


for i in itertools.combinations(count_points, K):
    total += reduce(lambda x,y : x*y ,[ count_points.get(j) for j in i ])


print(total)