import math
import bisect

I, T = map(int, input().split())
sunIntensity = list(map(int, input().split()))
prefixSumOfSunIntensity = [0]
for i in sunIntensity:
    prefixSumOfSunIntensity.append(prefixSumOfSunIntensity[-1] + i)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]


for i in range(M):
    a, b, d, s = input().split()
    a = int(a)
    b = int(b)
    d = int(d)

    graph[a].append((s, d, b))

minimalSun = [math.inf for _ in range(N)]
minimalSun[0] = 0

# Sun Intensity, Time, Current Node
q = [(0, 0, 0)]

while len(q) > 0:
    sunIntensity, time, currentNode = q.pop(0)
    minimalSun[currentNode] = min(minimalSun[currentNode], sunIntensity)
    print(sunIntensity, time, currentNode)

    for path in graph[currentNode]:
        shaded, pathTime, newNode = path
        if shaded == 'S':
            shaded = 0
        else:
            shaded = 1
        
        bisect.insort(q, ( sunIntensity + shaded * (I*(max(time+pathTime, T-1)-(T-1)) + prefixSumOfSunIntensity[min(time+pathTime,T-1)] - prefixSumOfSunIntensity[min(time,T-1)]), time+pathTime, newNode))
