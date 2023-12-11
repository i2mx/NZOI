input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))
input()
C = list(map(int, input().split()))

if sum(A)/len(A) >= 12 and sum(B)/len(B) >= 12 and sum(C)/len(C) >= 12:
    if sum([i >= 25 for i in A]) >= len(A)/2:
        print("resow")
        exit()

    print("unhealthy")
    exit()
print("healthy")
exit()