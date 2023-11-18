target = input()

c = 0

while True:
    c += 1
    i = input()
    if i == "GIVE UP":
        print(f"The word was not guessed. Answer: {target}.")
        exit()
    if i == target:
        print(f"The word was guessed in {c}.")
        exit()

    bulls = 0

    for j, (a,b) in enumerate(zip(target, i)):
        print(j, a, b)
        if a == b:
            bulls += 1
            target = target.(j)

        print(target, i)