# the plan is precomputing + binary search
# as we fail when Q > 1 we must find a way to preserve useful information

from collections import Counter
import bisect
from math import inf
# lol based on a true story

N, Q = map(int, input().split())
H = list(map(int, input().split()))

C = Counter()
C.update(H)

throws = list(C.items())
throws.insert(0, (0,0))
throws.sort()

    
# uses, height, number_avaliable, current height
build = [(0,0,0,throws[-1][0])]

for i in range(len(throws) - 1, 0, -1):
    height, number = throws[i]
    next_height, _ = throws[i-1]

    last_uses, last_height, last_number, _ = build[-1]
    added_height = (last_number + number) * (height-next_height) * (height + next_height + 1) // 2
    added_use = (height - next_height) * (last_number + number)

    build.append((last_uses + added_use, (last_height + added_height)%1_000_000_007 , number + last_number, next_height))

for i in range(0, len(build) - 2):
    a,b,c,d = build[i]
    build[i] = (a,b,build[i+1][2],d)

for _ in range(Q):
    T = int(input())

    # building ontp of the pre calculated value
    build_i = bisect.bisect_left(build, (T, inf, inf, inf)) - 1
    uses, total_height, number, height = build[build_i]
    
    if build_i == len(build) -1:
        print(total_height)
        continue

    uses = T - uses

    triangles = uses // number
    singles = uses % number

    total_height += number * triangles * (2 * height - triangles + 1) // 2
    total_height += singles * (height - triangles)

    print(total_height)
