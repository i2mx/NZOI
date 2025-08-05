import itertools as it

n = int(input())
apples = list(map(int, input().split()))

S = sum(apples)
sums = set([0])

min_d = 1e100

for x in apples:
    new_sums = []
    for s in sums:
        new_sums.append(s + x)
        d = abs(S - 2*(s+x))
        min_d = min(min_d, d)
    for s in new_sums:
       sums.add(s) 

print(min_d)