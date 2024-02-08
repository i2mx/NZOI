# Shocking Calculation
# https://train.nzoi.org.nz/problems/1204

N = int(input())
hurts = dict(zip(map(str, range(10)), map(int, input().split())))
hurts["+"], hurts["*"], hurts["="] = map(int, input().split())

def hurt(s):
    if isinstance(s, int):
        return hurt(s)
    if len(s) == 1:
        return hurts[s]
    return sum(map(hurt, s))


min_cost = 10000000000000000000000000000000000000000000000000000000000000000000

for a in range(1, int(N**0.5) + 1):
    for b in range(1, N // a + 1):
        cost = 0

        if a * b > N:
            continue
        if a == 1 or b == 1:
            cost += hurt(f"{max(a,b)}")
        else:
            cost += hurt(f"{a}*{b}")

        if a * b < N:
            cost += hurt(f"+{N-a*b}")

        min_cost = min(min_cost, cost)

print(min_cost + hurts["="])