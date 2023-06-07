n = input()
p = list(map(int, input().split()))
p.sort()

m = p[n//2]

print(sum([abs(x - m) for x in p]))
