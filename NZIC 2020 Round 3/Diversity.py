# WOW why does this work?


def digits(n):
    return list(map(int, str(n)))


def to(arr):
    result = 0
    d = 1
    for i in arr[::-1]:
        result += i * d
        d *= 10
    return result


x = int(input())


def fix(n):
    N = digits(n)
    for i in range(len(N) - 1):
        if N[i] == N[i + 1]:
            N[i + 1] += 1
            if N[i + 1] == 10:
                return fix(to(N))
            for j in range(i + 2, len(N)):
                if j % 2 == i % 2:
                    N[j] = 0
                else:
                    N[j] = 1
            break
    return to(N)


print(fix(x))
