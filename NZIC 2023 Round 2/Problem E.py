import itertools

N = int(input())

pairs = set()
first = []


for i in range(N):
    a,b = map(int, input().split())
    pairs.add((a,b))
    first.append(a)

possible_persm = []

for perm in itertools.permutations(first):
    friends = dict()
    friend_pairs = set()
    
    for i in perm:
        x = 2
        while True:
            if not x*i in friends.keys():
                friends[x * i] = True
                friends[i] = True

                friend_pairs.add((i, x*i))
                break
            x += 1

        # print(friend_pairs.difference(pairs))


    if pairs.issubset(friend_pairs):
        possible_persm.append(perm)

p = min(possible_persm)

for i in p:
    print(i, end=" ")