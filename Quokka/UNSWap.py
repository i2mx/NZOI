from collections import Counter

M = 1_000_000_007

n = int(input())
A = list(map(int, input().split()))


C = Counter()
for a in A:
    C.update(map(int, str(a)))

same_digit_swaps = 0
for i in range(10):
    n = C.get(i, 0)
    same_digit_swaps += (n * (n - 1)) // 2
    same_digit_swaps %= M

same_position_swaps = 0
for p in range(12):
    C.clear()
    n = 0
    for a in A:
        if len(str(a)) > p:
            C.update([int(str(a)[::-1][p])])
            n += 1
    same_position_swaps += (n * (n - 1)) // 2
    for c in C:
        same_position_swaps -= C[c] * C[c]

print((same_digit_swaps + same_position_swaps) % M)
