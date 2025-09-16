total = 0
for i in range(1, 678 + 1):
    # if "7" in str(i):
    #     total += 1

    total += str(i).count("6")

print(total)
