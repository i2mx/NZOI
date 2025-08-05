N = int(input())
S = input()

possibilities = list(range(N))

length = 1
while len(possibilities) > 1:
    min_indices = []
    min_character = '['
    for i in possibilities:
        j = (i + length - 1) % N
        if ord(S[j]) < ord(min_character):
            min_character = S[j]
            min_indices = [i]
        elif ord(S[j]) == ord(min_character):
            if min_indices[-1] != i - length:
                min_indices.append(i)
    possibilities = min_indices
    length += 1

x = possibilities[0]
print(S[x:] + S[:x])
