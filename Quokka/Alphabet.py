from collections import Counter

alphabet = input().strip()
S = input().strip()
C = Counter(S)

for c in alphabet:
    print(c * C.get(c, 0), end="", flush=False)
