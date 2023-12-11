import bisect

N, T = map(int, input().split())
keyboards = list(map(int, input().split()))
keyboards.sort()

best_prefix_target = 0
best_prefix_index = 0
for i in range(1, N):
    a = best_prefix_target + i * (keyboards[i] - keyboards[i - 1])

    if a > T:
        break

    best_prefix_target = a
    best_prefix_index = i


best_suffix_target = 0
best_suffix_index = 0
for i in range(1, N):
    a = best_suffix_target - i * (keyboards[N - 1 - i] - keyboards[N - 1 - (i - 1)])

    if a > T:
        break

    best_suffix_target = a
    best_suffix_index = i


smollest = keyboards[best_prefix_index] + (T - best_prefix_target) // (
    best_prefix_index + 1
)
biggest = keyboards[N - 1 - best_suffix_index] - (T - best_suffix_target) // (
    best_suffix_index + 1
)

if biggest - smollest <= 0:
    if sum(keyboards) % N == 0:
        print(0)
    else:
        print(1)
else: 
    print(biggest - smollest)