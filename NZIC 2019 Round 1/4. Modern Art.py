import bisect

H, W, N = map(int, input().split())

throws = []

y_list = []
x_list = []

for _ in range(N):
    x, y, s, c = input().split()
    x, y, s = int(x), int(y), int(s)

    top_y = max(0, y - s)
    bottom_y = min(H, y + s + 1)
    left_x = max(0, x - s)
    right_x = min(W, x + s + 1)

    throws.append((top_y, bottom_y, left_x, right_x, c))
    y_list.append(top_y)
    y_list.append(bottom_y)
    x_list.append(right_x)
    x_list.append(left_x)

x_list.sort()
y_list.sort()

prev_i = -1
for i in x_list:
    if prev_i == i:
        x_list.remove(i)
    prev_i = i

prev_j = -1
for j in y_list:
    if prev_j == j:
        y_list.remove(j)
    prev_j = j


compressed_board = []
for _ in range(len(x_list)):
    compressed_board.append([])
    for _ in range(len(y_list)):
        compressed_board[-1].append("")

for throw in throws:
    top_y, bottom_y, left_x, right_x, c = throw
    compressed_top_y = bisect.bisect_left(y_list, top_y)
    compressed_bottom_y = bisect.bisect_left(y_list, bottom_y)
    compressed_left_x = bisect.bisect_left(x_list, left_x)
    compressed_right_x = bisect.bisect_left(x_list, right_x)

    for x in range(compressed_left_x, compressed_right_x):
        for y in range(compressed_top_y, compressed_bottom_y):
            compressed_board[x][y] = c

color = input().strip()

total = 0

x_list.append(0)
y_list.append(0)

for comp_x, i in enumerate(compressed_board):
    for comp_y, c in enumerate(i):
        if c == color:
            total += (x_list[comp_x + 1] - x_list[comp_x]) * (
                y_list[comp_y + 1] - y_list[comp_y]
            )

print(total)
