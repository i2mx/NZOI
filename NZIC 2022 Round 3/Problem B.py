N, M, Va, Vb = map(int, input().split())

A_names = input().split()
A_ver = [list(map(int, input().split())) for _ in range(Va)]
B_names = input().split()
B_ver = [list(map(int, input().split())) for _ in range(Vb)]

for i in range(N):
    if A_names[i] in B_names:
