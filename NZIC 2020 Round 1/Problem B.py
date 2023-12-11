
A, B, C = map(int, input().split())
D = int(input())

distances = [
    min(D % A, (-D) % A),
    min(D % B, (-D) % B),
    min(D % C, (-D) % C),
]

min_dist = (min(map(abs,distances)))
print(min_dist)
if (distances.count(min_dist) > 1):
    print("can't make up my mind")