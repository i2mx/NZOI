from queue import Queue

n = int(input())

grid = [[1e10 for _ in range(n)] for _ in range(n)]
seen = [[False for _ in range(n)] for _ in range(n)]

grid[0][0] = 0
seen[0][0] = True

queue = Queue()
queue.put((0, 0))

while not queue.empty:
    y, x = queue.get()
    moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
             (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for a, b in moves:
        if 0 > y + a or y + a >= n:
            continue
        if 0 > x + b or x + b >= n:
            continue
        if not seen[y+a][x+b]:
            seen[y+a][x+b] = True
            grid[y+a][x+b] = grid[y][x]+1
            queue.put((y+a, x+b))

for row in grid:
    print(" ".join(map(str, row)))