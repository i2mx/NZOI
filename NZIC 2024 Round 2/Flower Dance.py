from pprint import pprint
import bisect
# 1≤N≤700
# 0≤A≤500
N, A = map(int,input().split())

# we are going to use a similar compression idea to modern art

xValues = set()
yValues = set()

# squares = [lowerX, lowerY, upperX, upperY]
squares = []

for i in range(N):
    x,y = map(int, input().split())
    lowerX = max(x-A,0)
    lowerY = max(y-A,0)
    # using python style indexing
    upperX = x+A+1
    upperY = y+A+1

    xValues.add(lowerX)
    xValues.add(upperX)
    yValues.add(lowerY)
    yValues.add(upperY)

    squares.append((lowerX, lowerY, upperX, upperY))

xValues = sorted(xValues)
yValues = sorted(yValues)
compressedGrid = [[0 for _ in range(len(yValues)-1)] for _ in range(len(xValues)-1)]
# print(xValues)
# print(yValues)

for lowerX, lowerY, upperX, upperY in squares:
    lowerX = bisect.bisect_left(xValues, lowerX)
    lowerY = bisect.bisect_left(yValues, lowerY)
    upperX = bisect.bisect_left(xValues, upperX)
    upperY = bisect.bisect_left(yValues, upperY)
    # find corresponding indices in compressed grid
    for i in range(lowerX, upperX):
        for j in range(lowerY, upperY):
            compressedGrid[i][j] = 1

# print()

for row in compressedGrid:
    # print(row)
    ...

# print()
total = 0

for i in range(len(xValues)-1):
    for j in range(len(yValues)-1):
        w = xValues[i+1] - xValues[i]
        h = yValues[j+1] - yValues[j]

        # print((w*h, compressedGrid[i][j]), end = " ")
        total += w*h * compressedGrid[i][j]
    # print()

# print()
print(total)