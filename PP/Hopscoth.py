N = int(input())

prev = None
for _ in range(N):
    current = input()
    if prev == "S":
        if current == "N":
            print("impossible")
            exit()
    if prev == "E":
        if current != "N":
            print("impossible")
            exit()
    if prev == "N":
        if current == "N":
            print("impossible")
            exit()
    prev = current

print('plausible')