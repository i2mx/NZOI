from collections import Counter
# lol based on a true story

N, Q = map(int, input().split())
H = list(map(int, input().split()))

C = Counter()
C.update(H)

throws = list(C.items())
throws.insert(0, (0,0))
throws.sort()

for _ in range(Q):
    T = int(input())

    total_height = 0
    added = 0

    i = len(throws) - 1
    while T > 0 and i > 0:
        height, number = throws[i]
        next_height, _ = throws[i-1]
        avaliable = number + added

        if avaliable * (height - next_height) <= T:
            total_height += avaliable * (height + next_height+1) * (height - next_height) // 2
            total_height %= 1_000_000_007
        else:
            size = T // avaliable
            total_height += avaliable * size * (height + height - size + 1) // 2
            total_height %= 1_000_000_007

            total_height += (T % avaliable) * (height - size)
            total_height %= 1_000_000_007

        T -= (number + added) * (height - next_height)
        added += number
        i -= 1

    print(total_height)