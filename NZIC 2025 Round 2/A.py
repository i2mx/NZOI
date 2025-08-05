N = int(input())
teacups = [int(input()) for _ in range(N)]

teacups.sort(reverse=True)

shelf1 = []
shelf2 = []

while len(teacups) > 0:
    if len(teacups) == 1:
        shelf2.append(teacups.pop())
        continue
    teacup = teacups.pop()
    if teacups[-1] == teacups:
        teacups.pop()
        shelf1.append(teacup)
        shelf1.append(teacup)
    else:
        shelf2.append(teacup)


print("Shelf 1:", " ".join(map(str, shelf1)))
print("Shelf 2:", " ".join(map(str, shelf2)))
