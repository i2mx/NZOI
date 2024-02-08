L, R = map(int, input().split())
N = int(input())

L2R = []
R2L = []

h = 0 

for _ in range(N):
    c, hl, hr = map(int, input().split())

    if hr == -1:
        L -= c
        h += hl
        continue

    if hl == -1:
        R -= c
        h += hr
        continue

    if hl > hr:
        L -= c
        h += hl
        L2R.append((hl-hr, c))

    else:
        R -= c
        h += hr
        R2L.append((hr-hl, c))

if L >= 0 and R >= 0:
    print(h)
    exit()

if L + R < 0:
    print("Camp is cancelled")
    exit()

bigger = max(L,R)
smaller = abs(min(L,R))

actions = L2R if L < R else R2L

if len(actions) == 0:
    print("Camp is cancelled")


inf = 123456789000000000000000000000000000000000000000000000000
loss4move = [inf] * (bigger + 1)
loss4move[0] = 0

for dh, c in actions:
    for i in range(bigger + 1):
        if loss4move[i] == inf:
            continue
        if i+c > bigger:
            continue
        loss4move[i+c] = min(loss4move[i+c], loss4move[i] + dh)

if all(loss == inf for loss in  loss4move[smaller:]):
    print("Camp is cancelled")
else:
    print(h - min(loss4move[smaller:]))