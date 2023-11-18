import collections
import itertools

N = int(input())
boxes = list(map(int, input().split()))
boxes.sort()

c = collections.Counter(boxes)
# one_hot_boxes = list(c.elements())


most = c.most_common()[0][1]

nestings = [[] for _ in range(most)]

for i in itertools.cycle(range(most)):
    b = boxes.pop()
    nestings[i].append(b)
    if len(boxes) == 0:
        break
print(most)
for i in nestings:
    for j in i:
        print(j, end=" ")
    print()