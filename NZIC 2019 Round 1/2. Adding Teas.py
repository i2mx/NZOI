teas = {"G": 0, "C": 0, "E": 0, "P": 0, "L": 0, "S": 0}

while (i := input()) != "D":
    tea, n = i.split()
    teas[tea] += int(n)

for value in teas.values():
    print(value, end=" ")