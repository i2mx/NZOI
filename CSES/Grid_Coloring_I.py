n, m = map(int, input().split())

grid = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        options = ["A", "B", "C", "D"]
        if grid[i][j] in options:
            options.remove(grid[i][j])
        if i != 0 and grid[i-1][j] in options:
            options.remove(grid[i-1][j])
        if j != 0 and grid[i][j-1] in options:
            options.remove(grid[i][j-1])

        grid[i][j] = options[0]
    
for row in grid:
    print("".join(map(str, row)))