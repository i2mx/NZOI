N, K = map(int,input().split())

prev = None
prevprev = None


count = 0
for _ in range(N):
    i = int(input())
    if i < K:
        count += 1
    else:
        count = 0    
    if count == 3:
        print("Fault Detected")
        print(f"{prevprev} {prev} {i}")
        exit()
    prevprev = prev
    prev = i
print("No Fault")