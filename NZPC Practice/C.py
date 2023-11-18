t = int(input())

for _ in range(t):
    deez = set()

    n,m = map(int, input().split())
    s = list(map(int,input())) 
    
    l_i = -1
    u_l = False
    ll = []

    for i,v in enumerate(s):
        if v == 0:
            u_l = True
        if v == 1 and u_l == True:
            u_l = False
    # print(left_zero)
    # print(right_one)

    for _ in range(m):
        l,r = map(int,input().split())
        # L = (left_zero[l-1], right_one[r-1])
        deez.add(1)
    print(len(deez))