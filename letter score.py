N = int(input())
words = [input() for _ in range(N)]
a = input()

for word in words:
    total = 0
    for b in word:
        if b == a:
            total += 1
    print(total)