t = int(input())

for _ in range(t):
    b,c,h = map(int, input().split())
    b -= 1
    print(2 * min(b,c+h) + 1)
