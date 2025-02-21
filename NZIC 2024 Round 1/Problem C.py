# just had to use pypy

from collections import Counter
from itertools import product
# N is rlly rlly small

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = Counter()

for a,b in product(A,B):
    C.update([b-a])

val = C.most_common(1)[0][1]
print(N*2 - val)