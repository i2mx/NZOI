for _ in range(3):
    a,b = map(int, input().split())
    if a == b:
        print(f"Doubles. Move forwards {a+b} squares.")
        exit()

if input() == "y":
    print(f"Use card. Move forwards {a+b} squares.")

else:
    print(f"$50 fine. Move forwards {a+b} squares.")