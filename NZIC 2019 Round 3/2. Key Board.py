alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",'t',"u","v","w","x","y","z"]

for i,letter in enumerate(alphabet):
    alphabet[i] = letter.upper()


initial = 0
count = 0

word = input()

for letter in word:
    position = alphabet.index(letter)
    count += min(26-abs(initial - position),abs(initial - position))
    initial = position

print(count+len(word))