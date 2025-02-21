from math import inf
from pprint import pprint

n = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
k = int(input())

# total distance + whatever
table = [[(inf, 0) for _ in range(k + 1)] for _ in range(n + 1)]
table[0][0] = (0, 1)

for i, br in enumerate(b[::-1]):
    # going through the rows
    cr = c[n - 1 - i]

    for current in range(k + 1):
        # now going through each cell in the row
        if table[i][current][1] == 0:
            continue

        distance, _ = table[i][current]

        for add in range(cr + 1):
            if current + add * br > k:
                break

            if table[i + 1][current + add * br][0] > distance + add:
                table[i + 1][current + add * br] = (distance + add, add + 1)

print(table[n][k][0])

row = n
col = k


while row != 0:
    add = table[row][col][1] - 1
    bi = b[n - row]

    print(add, end=" ")

    col -= add * bi
    row -= 1
