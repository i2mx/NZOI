M, R = map(int, input().split())
minces = list(map(int, input().split()))

def pair_up(arr):
    return [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]

recipes = [pair_up(list(map(int, input().split()))[1:]) for _ in range(R)]


def how_many(mice_type):
    """returns the number of initial mice needed to produce one of a single
    type of mince
    """
    minces_needed = [
        0,
    ] * M
    if mice_type <= M:
        minces_needed[mice_type - 1] = 1
    else:  # figure out how to produce the mince from the recipe provided
        for mince, amount in recipes[mice_type - M - 1]:
            new_mince_needed = how_many(mince)
            for i in range(M):
                minces_needed[i] += new_mince_needed[i] * amount

    return minces_needed


initial_mince_required = how_many(M + R)
max_final_mince_producible = 1000000000

for i in range(M):
    if initial_mince_required[i] == 0:
        continue
    max_final_mince_producible = min(
        max_final_mince_producible, minces[i] // initial_mince_required[i]
    )

print(max_final_mince_producible)
# THIS PROBLEM SUCKS BTW