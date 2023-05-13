import math


def repdigit(length, digit):
    return int((10**length - 1) / 9 * digit)


N = int(input())

l = []

def adiufhsd():
    global N
    x = math.floor(math.log10(N))
    
    for i in range(9,0,-1):
        if N >= repdigit(x+1,i):
            N -= repdigit(x+1,i)
            l.append(repdigit(x+1,i))
            return
    N-=repdigit(x,9)
    l.append(repdigit(x,9))
    return

while N >= 10:
    adiufhsd()

if N != 0:
    if N == 10:
        l.append(1,9)
    if N < 10:
        l.append(N)

print(len(l))
[print(i) for i in l[::-1]]
