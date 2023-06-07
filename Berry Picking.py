N,K = map(int, input().split())
B = list(map(int, input().split()))

B.sort()

max_number = 0
for i in range(1000):
    