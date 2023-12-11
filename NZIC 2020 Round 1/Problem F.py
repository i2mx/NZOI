from math import inf
from queue import PriorityQueue

R, N, T = map(int, input().split())


class Rocket:
    def __init__(self, cost, fuel) -> None:
        self.cost = cost
        self.fuel = fuel


rockets = list(map(lambda x: Rocket(x[0], x[1]),  [list(map(int, input().split())) for _ in range(R)]))
rockets.sort(key=lambda x:x.cost)

tiles = [int(input()) for _ in range(N)]

cost_to_ith_tile = [inf for _ in range(T)]

path_queue = PriorityQueue()
path_queue.put((0,0))

while not path_queue.empty():
    current_cost, current_destination = path_queue.get()
    if cost_to_ith_tile[current_destination] != inf:
        continue

    cost_to_ith_tile[current_destination] = current_cost

    for rocket in rockets:
        if rocket.fuel + current_destination < T:
            path_queue.put((rocket.cost + current_cost, rocket.fuel + current_destination))
        if rocket.fuel - current_destination >= 0:
            path_queue.put((rocket.cost + current_cost, rocket.fuel - current_destination)) 

for tile in tiles:
    print(cost_to_ith_tile[tile])