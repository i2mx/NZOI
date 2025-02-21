N = int(input())
for _ in range(N):
    x,y = map(int, input().split())
    print ("BLACK" if (x+y)%2==0 else "WHITE")