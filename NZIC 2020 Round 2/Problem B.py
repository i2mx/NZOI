N = int(input())
count = 0
for _ in range(N):
    count -= int(input())

if count == 0:
    print("She's got them all")
else:
    print(count)