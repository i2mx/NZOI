import bisect

_ = int(input())
a = list(map(int, input().split()))
k = int(input())

a.sort()

for _ in range(k):
    l,r = map(int, input().split())

    left = bisect.bisect_left(a, l)
    right = bisect.bisect_right(a, r)

    print(right-left, end=" ")