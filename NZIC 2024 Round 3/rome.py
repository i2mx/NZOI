# 2 watch towers are safe if they are the same height and nothing biggest between them
N = int(input())
unsafe = 0
safe = [False] * N
heights = list(map(int, input().split()))
for i in range(N):
    unsafe += 1
    for j in range(i-1, -1, -1):
        if heights[j] > heights[i]:
            break
        if heights[j] == heights[i]:
            unsafe -= 1
            safe[i] = True
            if not safe[j]:
                safe[j] = True
                unsafe -= 1
            break
    print(unsafe)