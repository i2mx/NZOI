# https://ltu.diva-portal.org/smash/get/diva2:995901/FULLTEXT01.pdf
# what?

N, M, K = map(int, input().split())

trees = [tuple(map(int, input().split())) for _ in range(M)]
trees.sort()

segments = []
if trees[0][0] != 1:
    segments.append(trees[0][0] - 1)

for i in range(M-1):
    segments.append(1 - trees[i][1])
    segments.append(trees[i+1][0] - trees[i][0] - 1)

segments.append(1 - trees[-1][1])
if (trees[-1][0] != N):
    segments.append(N - trees[-1][0])

# maximum k non overlapping sub arrays


def max_k_subarrays(arr, k):
    max_sum_up_to = [0] * (k + 1)
    max_sum_ending_here = [-1e9] * (k + 1)

    for num in arr:
        prev_max_sum_up_to = max_sum_up_to[:]  # copy trick
        for j in range(k, 0, -1):
            max_sum_ending_here[j] = max(
                max_sum_ending_here[j] + num, prev_max_sum_up_to[j-1] + num)
            max_sum_up_to[j] = max(max_sum_up_to[j], max_sum_ending_here[j])

    return max_sum_up_to[k]


total = sum(map(lambda x: x[1], trees))
gain = max_k_subarrays(segments, K)

print(total + gain)
