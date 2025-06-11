# N, G = map(int ,input().split())
# t = list(map(int, input().split()))
 
# lower = 0
# upper = G * t[0]
 
# while lower < upper:
#     mid = (upper + lower) // 2
#     products = sum( mid // i for i in t )
#     if products >= G:
#         upper = mid
#     else:
#         lower = mid + 1
# print(lower)

data = input()
data_list = data.split()
goal = int(data_list[1])
speeds = input()
speed_list = speeds.split()
int_speed = []

for i in speed_list:
    int_speed.append(int(i))

int_speed.sort()

shortest_time = 0
longest_time = int_speed[-1] * goal
output = 0

while shortest_time <= longest_time:
    middle = (shortest_time + longest_time) // 2
    most_efficient = 0

    for i in int_speed:
        most_efficient += middle // i

    if most_efficient >= goal:
        output = middle
        longest_time = middle - 1
    else:
        shortest_time = middle + 1

print(output)