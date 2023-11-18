G, R = map(int, input().split())

N, T = map(int, input().split())

total_elapsed_time = T
queue = [0 for _ in range(N)]

max_queue_length = len(queue)
max_wait_time = 0

K = int(input())
for _ in range(K):
    color, cars = input().split()
    cars = int(cars)

    if color == "R":
        for _ in range(cars):
            queue.append(total_elapsed_time)
        max_queue_length = max(max_queue_length, len(queue))
        total_elapsed_time += R
    else:
        for _ in range(cars):
            car = queue.pop(0)
            max_wait_time = max(max_wait_time, total_elapsed_time - car)
        total_elapsed_time += G

max_queue_length = max(max_queue_length, len(queue))

if max_queue_length == 1:
    print("Longest queue was 1 vehicle.")
else:
    print(f"Longest queue was {max_queue_length} vehicles.")

minutes = max_wait_time // 60
seconds = max_wait_time % 60

s = f'Longest through time was {minutes} {"minute" if minutes == 1 else "minutes"} and {seconds} {"second" if seconds == 1 else "seconds"}.'
print(s)
