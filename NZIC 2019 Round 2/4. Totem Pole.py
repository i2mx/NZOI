N, T = map(int, input().split())

people = list(map(int, input().split()))
people.sort(reverse=True)

for i, H in enumerate(people):
    T = min(T-1, H-1)
    if(T <= 0):
        print(i + 1)
        exit()

print(N)
