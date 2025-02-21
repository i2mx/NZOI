_ = int(input())
R, P, D, G = map(int, input().split())
TOTAL = R + P + D + G
T = R+P+D

i = 0

for c in input():
    if c == 'R':
        R -= 1
        T -= 1
    if c == 'P':
        P -= 1
        T -= 1
    if c == 'D':
        D -= 1
        T -= 1
    if c == 'G':
        G -= 1
    if c == '.':
        T -= 1

    if R < 0 or P < 0 or D < 0 or G < 0 or T < 0:
        break

    i += 1

print(i)
print(TOTAL - i)