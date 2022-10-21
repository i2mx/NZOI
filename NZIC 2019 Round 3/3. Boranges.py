from math import ceil


N, c = map(int, input().split())

# the number of boranges needed to make a profit, anything more will make a profit
B = c // 5

orang = {}
max_height = 0

orang[0] =  N

for _ in range(N):
    h = int(input())
    max_height = max(h, max_height)

    if h < B:
        if h in orang.keys():
            orang[h] -= 1
        else:
            orang[h] = -1

count = 0
trees_sum = 0
for i in range(B):
    x = orang[i] if i in orang.keys() else 0 
    trees_sum += x
    oranges = trees_sum * (i+1)
    if oranges > B:
        count += 1

        
print(max(0, max_height - B) + count)