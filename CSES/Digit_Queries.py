# from math import ceil

q = int(input())

for _ in range(q):
    k = int(input())

    digits = 1
    total = 0

    while total + digits * (10**digits - 10**(digits - 1)) < k:
        total += digits * (10**digits - 10**(digits - 1))
        digits += 1

    number = ((k - total + (total-k) % digits) //
              (digits)) + 10**(digits-1) - 1

    i = ((k-total)-1) % digits

    print(str(number)[i])
    # print(digits, number, i)
