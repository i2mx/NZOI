_ = int(input())
word = input()
vowels = 'aeiou'
total = 0

if word == "onk":
    print(0)
    exit()

# no vowel goose latin
if word.endswith("onk"):
    start = word[:-3]
    if all(s not in vowels for s in start):
        total += 1

# vowel goose latin
# must contin a vowel
has_vowel = False
i = 0
while i < len(word):
    s = word[i]
    if s in vowels:
        if i+3 < len(word) and word[i+1] == 'l' and word[i+2] == 'f' and word[i+3] == s:
            has_vowel = True
            i += 4
            continue
        else:
            break
    i += 1
if i >= len(word) and has_vowel:
    total += 1

if word.endswith('ck'):    
    if word[0] in vowels:
        start = word[:-2]
        if all(c in vowels for c in start):
            total += 1
    if word[0] not in vowels:
        i = 0
        for c in word[-3::-1]:
            if c in vowels:
                i += 1
            else: 
                break
        total += i

if word.endswith('uack'):
    # moving the consonant
    if word[0] not in vowels:
        start = word[:-4]
        if all(c not in vowels for c in start):
            total += 1
    if word[0] in vowels:
        i = 0 
        for c in word[-5::-1]:
            if c not in vowels:
                i += 1
            else:
                break
        total += i
print(total)
