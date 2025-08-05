from itertools import permutations
seen = set()
total = 0
ls = []
for chars in permutations(sorted(input())):
    s = "".join(chars) 
    if s not in seen:
        seen.add(s)
        ls.append(s)
        total += 1
print(len(ls))
for s in ls:
    print(s) 