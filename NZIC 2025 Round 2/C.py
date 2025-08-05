from collections import Counter

N, M, K = map(int, input().split())
ribbon = list(map(int, input().split()))

max_length = 1
max_count = 0
colours: Counter[int] = Counter()

start = 0
end = 1

colours.update([ribbon[0]])
while end < len(ribbon):
    while (
        end < len(ribbon)
        and (
            len(colours) < K
            or (
                len(colours) == K
                and
                ribbon[end] in colours
            )
        )
        and end - start < M
    ):
        colours.update([ribbon[end]])
        end += 1
        max_length += 1
        max_count = 1

    if end < len(ribbon):
        colours.update([ribbon[end]])
        colours.subtract([ribbon[start]])
        if colours.get(ribbon[start], 0) == 0 and ribbon[start] in colours:
            colours.pop(ribbon[start])
        start += 1
        end += 1
        if len(colours) <= K:
            max_count += 1

print(max_length, max_count)
