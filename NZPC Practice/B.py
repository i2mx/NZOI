import bisect
import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    H = list(map(int, input().split()))
    Hi = list(zip(H, range(n,0,-1)))
    Hi.sort()


    while len(Hi) > 0:
        # print(Hi)

        h, i = Hi.pop()
        
        if len(Hi) == 0:
            print(n+1-i, end=" ")
            continue

        while (h,i) > Hi[-1]:
            h -= k
        
        if h <= 0:
            print(n+1-i, end=" ")
            continue

        bisect.insort(Hi, (h, i))

    print()