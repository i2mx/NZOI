n, mean, median, mode = map(int, input().split())

if mean == median == mode:
    print("Possible")
    print(f"{mean} " * n)

elif n == 1:
    print("Impossible")

elif n == 3:
    x = 3*mean - 2*mode
    if median != mode or x < 1 or x > 1000000:
        print("Impossible")
    else:
        print("Possible")
        print(mode, mode, x)