import collections

N, K = map(int, input().split())
points = list(map(int, input().split()))

point_counts = list(collections.Counter(points).values())
n_points = len(point_counts)

def find_combinations(k,i):
    if k > n_points-i:
        return 0
    if k == 0:
        return 1
    return point_counts[i] * find_combinations(k-1, i+1) + find_combinations(k, i+1)

print(find_combinations(K,0))