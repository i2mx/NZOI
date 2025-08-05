grid = [list(input()) for _ in range(8)]


def solve(n=0):
    if n == 8:
        # for line in grid:
        #     print("".join(line))
        # print()
        return 1

    total = 0

    for i in range(8):
        # check that this is a free square
        if grid[n][i] == "*":
            continue

        # check that this space is not attacked by a queen
        valid = True
        for m in range(n):
            if grid[m][i] == "Q":
                valid = False
                break

            d1 = i + m - n
            if 0 <= d1 and d1 < 8 and grid[m][d1] == "Q":
                valid = False
                break

            d2 = i + n - m
            if 0 <= d2 and d2 < 8 and grid[m][d2] == "Q":
                valid = False
                break

        if valid:
            grid[n][i] = "Q"
            total += solve(n+1)
            grid[n][i] = "."

    return total

# print(grid)


print(solve())
