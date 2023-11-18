names = input().split()

for _ in range(int(input())):
    a,b = map(int, input().split())

    names[b-1], names[a-1] = names[a-1], names[b-1]

for i in names:
    print(i, end=" ")