import bisect

N, D = map(int, input().split())

mods = [ dict() for _ in range(51)]

for _ in range(D):
    k, p = map(int, input().split())


    if mods[p].get(k%p) == None:
        mods[p][k%p] = []

    bisect.insort(mods[p][k%p], k)

for light in range(1,N+1):
    totalparity = 0
    for mod in range(1,51):
        residue = light % mod
        
        residuelist = mods[mod].get(residue)
        if residuelist == None:
            residuelist = []
        
        flips = bisect.bisect_right(residuelist,light)

        totalparity += flips
        totalparity %= 2

    print("ON" if totalparity % 2 == 1 else "OFF")