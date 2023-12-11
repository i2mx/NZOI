colors = [input() for _ in range(5)]

if any([colors[0].count(letter) > 1 for letter in colors[0]]):
    if all([len(color) % 2 == 1 for color in colors[1::]]):
        print("best")
        exit()
elif all([len(colors[i]) > len(colors[i+1]) for i in range(1,4)]):
    print("ok")
    exit()
print("bad")