N = int(input())

total_max = -1
running_max = 0

for _ in range(N) :
    a = int(input())

    if a <= 0:
        running_max = 0
        continue

    running_max += a
    total_max = max(running_max, total_max)

print(total_max)