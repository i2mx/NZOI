from pprint import pprint

N = int(input())


def construct(a: list[int], x: int):
    # digit added, previous mod, length
    dp = [[(-1, -1, 0) for _ in range(x)] for _ in range(len(a)+1)]

    for i, d in enumerate(a):
        if dp[i][d % x] == (-1, -1, 0):
            # if we haven't ever made this before then we make it
            dp[i+1][d % x] = (d, 0, 1)

        for j in range(x):
            _, _, le = dp[i][j]
            # if reusing the previous one without adding any digits
            # is more optimal we will just do that
            if dp[i+1][j][2] < le:
                dp[i+1][j] = (-1, j, le)

            # if j hasn't been made before we continue
            if dp[i][j] == (-1, -1, 0):
                continue

            # j has been made, which means k = 10*[]+d can then be made
            k = (10*j+d) % x
            if dp[i+1][k][2] < le + 1:
                dp[i+1][k] = (d, j, le+1)

    if dp[len(a)][0][2] == 0:
        return -1

    # do a quick traversal up the dp to find the number
    digits = []
    j = 0
    i = 0
    while True:
        cell = dp[len(a)-i][j]
        if (d := cell[0]) != -1:
            digits.append(d)
        if cell[2] == 0:
            break
        j = cell[1]
        i += 1

    return "".join(map(str, digits[::-1]))


for _ in range(N):
    a = list(map(int, input()))
    x = int(input())

    print(construct(a, x))
