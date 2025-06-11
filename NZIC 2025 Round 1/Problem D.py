from collections import Counter

N, M = map(int, input().split())
s = input()
# it is the string of length N repeated M times
# this problem is equivalent to finding the mode

t = 0
ns = ""
for i in range(N):
    c = Counter()
    for j in range(M):
        c.update(s[j * N + i])
    letter, freq = c.most_common(1)[0]
    t += M - freq
    ns += letter

print(t)
print(ns * M)