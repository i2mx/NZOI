import collections

N = int(input())
a = [ input() for _ in range(N)] 
c = collections.Counter(a)

if len(c) == 1:
    name = c.most_common()[0][0]
    vote = c.most_common()[0][1]
    if vote == 1:
        print(f"{name} won by {vote} vote.")
    else:
        print(f"{name} won by {vote} votes.")
    exit()

M = c.most_common()

most = M[0][1]
mosts = []

for i in M:
    if i[1] == most:
        mosts.append(i[0])

if len(mosts) == 1:
    if M[0][1] - M[1][1] == 1:
        print(f"{mosts[0]} won by {M[0][1] - M[1][1]} vote.")
    else:
        print(f"{mosts[0]} won by {M[0][1] - M[1][1]} votes.")

else:
    s = "Tie between "
    mosts.sort()
    for name in mosts:
        s += name + ", "
 
    s = s[:-2]
    print(s + ".")