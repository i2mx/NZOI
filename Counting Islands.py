# yeah I should have realised that just storing all of the grid is going to MLE
# I know that this can be done with a DSU, but do I really wanna do that?

count = 0
i = 0

width, height, threshold = map(int, input().split())
grid = [input() for _ in range(height)]

row0 = input()

for _ in range(1, height):
    row1 = input()
    ...
    row0 = row1

print("hello world")