count = 0
word = "hello"

for i in input():
    if i == word[count]:
        count+=1
    if count == 5:
        break

print("YES" if count == 5 else "NO")
    


