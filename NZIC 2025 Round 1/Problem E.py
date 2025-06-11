# NO WRONG ANSWERS YES
# - [x] ADD MEMO
# - [ ] ADD BISECT
# - [x] GREED OPTIMIZATION (PRUNING!!!)
#   - [ ] THERE MIGHT BE MORE OPTIMIZATION?
# - [x] I AM ASSUMING THE RUNTIME ERROR IS FROM RECURSION SO INCREASE THIS
# LOL NO WAY THIS WORK HAHAHAHAHH


import bisect
import sys

sys.setrecursionlimit(2**31 - 1)

N, M = map(int, input().split())
# list of lanes, where each lane contains where the gaps are
lanes = [[] for _ in range(M)]
for _ in range(N):
    ln, s, e = map(int, input().split())
    lanes[ln - 1].append((s, e))

memo = {}


def max_safety(ln, start, end):
    if (ln, start, end) in memo:
        return memo[(ln, start, end)]

    if end <= start:  # our gap is not valid
        return 0

    if ln >= M:  # we are in the last lane
        return end - start

    # this is not in python 3.6
    # left = bisect.bisect_left(lanes[ln], start, key=lambda x: x[1])
    # right = bisect.bisect_right(lanes[ln], end, key=lambda x: x[0])
    # left = bisect.bisect_left(lanes_end[ln], start)
    # right = bisect.bisect_right(lanes_start[ln], end)

    # WHAT WE WANT IS TO FIND THE FIRST GAP THAT IS GREATER THAN OR EQUAL TO START + 2
    left = bisect.bisect_left(lanes_end[ln], start - 1)

    max_sub_safety = 0
    # check if we can cross into any gap in the next jane
    for gi in range(left, len(lanes[ln])):
        # check if its actually valid at all
        gap_start, gap_end = lanes[ln][gi]

        if gap_end - 1 < start + 1:
            continue

        # THIS MEANS THAT WE ARE ASSUMING
        # gap_end !< start + 2
        # gap_end >= start + 2

        if gap_start > end:
            break

        gap_start = max(gap_start, start + 1)
        gap_end = gap_end

        next_safety = max_safety(ln + 1, gap_start, gap_end)
        new_sub_safety = min(end - gap_start + 1, next_safety)
        max_sub_safety = max(max_sub_safety, new_sub_safety)

        # IF THE BOTTLE NECK IS THE CURRENT LANE, WE CAN JUST MOVE ON (I THINK?)
        # because that part is just gonna keep getting smaller
        if end - gap_start + 1 <= next_safety:
            break

    # print("returning", max_sub_safety)
    memo[(ln, start, end)] = max_sub_safety
    return memo[(ln, start, end)]


for lane in lanes:
    lane.sort()

lanes_start = []
lanes_end = []
for i in range(M):
    lanes_start.append([x[0] for x in lanes[i]])
    lanes_end.append([x[1] for x in lanes[i]])

# BRUH IM SO STUPID

print(max_safety(0, 0, 1e9))
