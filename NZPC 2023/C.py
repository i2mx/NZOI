N = int(input())

goals = dict()

for _ in range(N):
    a, b, c = input().split()

    if a == "M":
        continue

    b = int(b)
    c = int(c)

    add = 1 if a == "G" else -1

    if (b,c) in goals: 
        goals[(b,c)] += add
    else: goals[(b,c)] = add

maxgoal = -10000
maxspots = []

for i, v in goals.items():
    if v > maxgoal:
        maxgoal = v
        maxspots = [i]
    elif v == maxgoal:
        maxspots.append(i)

if len(maxspots) == 1:
    print("Best place ", end="")
else:
    print("Best places ", end="")


s = ""
for i, j in sorted(maxspots):
    s += f"{i} {j}, "

l = s.removesuffix(", ")
print(l + ".")