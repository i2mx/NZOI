t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    if a + b > n:
        print("NO")
        continue
    if min(a, b) == 0 and max(a, b) > 0:
        print("NO")
        continue

    print("YES")
    m = a+b
    for i in range(b):
        print(b-i, end=" ")
    for i in range(a):
        print(m-i, end=" ")

    for i in range(m+1, n+1):
        print(i, end=" ")

    print()
    for i in range(b):
        print(m-i, end=" ")

    for i in range(a):
        print(a-i, end=" ")
    for i in range(m+1, n+1):
        print(i, end=" ")

    print()
