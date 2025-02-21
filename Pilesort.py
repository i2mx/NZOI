N = int(input())
p = list(map(int, input().split()))
v = [False for _ in range(N)]

count = 0

for i in range(N):
    if v[i]:
        continue
    # print("hi")
    big = i
    for j in range(i, N):
        if p[j] <= p[big]:
            big = j
            # print(j)
            v[j] = True
    count += 1

print(count)