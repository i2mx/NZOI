N, X, M = map(int, input().split())

house_cap = [int(input()) for _ in range(N)]
programmers = [tuple(map(int, input().split())) for _ in range(M)]

def valid_solution(new_house):
    for i in range(N):
        if house_cap[i] < new_house.count(i + 1):
            return False

    for i, house in enumerate(new_house):
        if X * abs( house - programmers[i][0]) > programmers[i][1]:
            return False

    return True

sequence = [1 for _ in range(M)]


def update_sequence():
    pointer = -1
    while True:
        if sequence[pointer] == N:
            sequence[pointer] = 1
            pointer -= 1
        else:
            sequence[pointer] += 1
            break

if valid_solution(sequence):
    print("SOLUTION IS TRIVIAL")
    for h in sequence:
        print(h)
    exit()

for _ in range(N**M-1):
    # print(sequence)

    update_sequence()
    # print(sequence)

    if valid_solution(sequence):
        print("SOLUTION IS TRIVIAL")
        for h in sequence:
            print(h)
        exit()

if valid_solution(sequence):
    print("SOLUTION IS TRIVIAL")
    for h in sequence:
        print(h)
    exit()

print("SOLUTION IS NON-TRIVIAL")
