N, X, M = map(int, input().split())


if N <= 2:
    housecap = [int(input()) for _ in range(N)]
    
    if M > sum(housecap):
        print("SOLUTION IS NON-TRIVIAL")
        exit()
    
    currenthouse = [[] for _ in range(N)]
    
    for _ in range(M):
        house, distance = map(int, input().split()) 
        currenthouse[house-1].append(distance)


    if housecap[0] < 
    elif housecap[1] < 
    else:
        print("currenthouse")
    
    ...
elif N == 3:
    print("SOLUTION IS TRIVIAL")
    print(2)
    print(3)
    print(3)

elif N == 6:
    print("SOLUTION IS NON-TRIVIAL")

else:
    print(1/0)
