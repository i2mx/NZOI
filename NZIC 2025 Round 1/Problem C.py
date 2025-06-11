N = int(input())
hs = list(map(int, input().split()))
hs.sort()

curr = 0
for h in hs:
    if h > curr:
        curr += 1
print(curr)

