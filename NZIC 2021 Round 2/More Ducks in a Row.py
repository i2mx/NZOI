import statistics
# 1 <= N <= 60,000
N = int(input())
C = [None] * N
R = [None] * N
for i in range(N):
    C[i], R[i] = map(int, input().split())
    
cm = statistics.median(C)
rm = statistics.median(R)

cd = sum(abs(c - cm) for c in C)
rd = sum(abs(r - rm) for r in R)

print(int(min(cd, rd)))