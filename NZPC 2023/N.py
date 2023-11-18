L, R = map(int, input().split())
heights = list(map(int, input().split()))

dividers = {}
c = 0
for i in range(L, R+2, 2):
    dividers[i] = heights[c]
    c += 1

dividers[-0.1] = dividers[-1]
dividers[0.1] = dividers[1]

pos_max = dividers[1]
for i in range(1, R+2, 2):
    if dividers[i] > pos_max:
        pos_max = dividers[i]
        dividers[0.1] = pos_max
        for j in range(1, i, 2):
            dividers[j] = pos_max
    else:
        continue



neg_max = dividers[-1]
for i in range(-1, L-2, -2):
    if dividers[i] > neg_max:
        neg_max = dividers[i]
        dividers[-0.1] = neg_max
        for j in range(-1, i, -2):
            dividers[j] = neg_max
    else:
        continue

rightVolume = 0
leftVolume = 0

for i in range(3, R+2, 2):
    rightVolume += 2*dividers[i]

for i in range(-3, L-2, -2):
    leftVolume += 2*dividers[i]

rightVolume += dividers[1]
leftVolume += dividers[-1]


rightmax = dividers[1]
leftmax = dividers[-1]

rind = 1
for i in range(1, R+2, 2):
    if dividers[i] > rightmax:
        rightmax = dividers[i]
        rind = i

lind = -1
for i in range(-1, L-2, -2):
    if dividers[i] > leftmax:
        lind = i
        leftmax = dividers[i]


total_volume = 0
dist = rind - lind
print(dist)
if rightmax < leftmax:
    # flowing right
    total_volume += dist * rightmax
    volr = rind * rightmax
    for i in range(rind+2, R+2, 2):
        volr += 2 * dividers[i]
        total_volume += 2 * dividers[i]
elif leftmax < rightmax:
    # flowing left
    total_volume += dist * leftmax
    voll = -lind * leftmax
    for i in range(lind-2, L-2, -2):
        voll += 2 * dividers[i]
        total_volume += 2 * dividers[i]
else:
    if rightmax == dividers[R]:
        print(R * rightmax + lind * rightmax)
        exit()
    elif leftmax == dividers[L]:
        print(-L * leftmax + rind * rightmax)
        exit()
    
    if rightVolume < leftVolume:
        print(2 * rightVolume)
        exit()
    else:
        print(2 * leftVolume)
        exit()

print(total_volume)


    

