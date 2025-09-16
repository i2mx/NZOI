# wafu stupid
from queue import PriorityQueue

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    q = PriorityQueue()
    nums = list(map(int, input().split()))
    for x in nums:
        q.put(x)

    prod = 1
    for _ in range(k):
        p = q.get()
        # print(p)
        prod *= p
        prod %= 10**9 + 7
        for i in range(1, p):
            q.put(i)
    print(prod)
