N = int(input())

value = 1
for i in range(N):
    x = int(input())
    if i % 3 == 0:
        value *= x
    if i % 3 == 1:
        value += x
    if i % 3 == 2:
        value -= x

print(value)