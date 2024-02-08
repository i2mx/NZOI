import queue

N = int(input())

for o in range(N):
    x, y = map(int, input().split())

    rows = [input() for _ in range(y)]
    start = None
    end = None

    parents = dict()

    for i in range(y):
        for j in range(x):
            if rows[i][j] == "S":
                start = (j, i)
            if rows[i][j] == "E":
                end = (j, i)

    search = queue.Queue()
    search.put(start)

    dead = False

    while search.not_empty and not dead:
        c_x, c_y = search.get()
        
        for n_x, n_y in [(c_x + 1, c_y), (c_x, c_y + 1), (c_x - 1, c_y), (c_x, c_y - 1)]:

            if n_x < 0 or n_y < 0 or n_x >= x or n_y >= y:
                continue

            if rows[n_y][n_x] == "#":
                continue
            if (n_x,n_y) not in parents:
                parents[(n_x, n_y)] = (c_x, c_y)
                search.put((n_x, n_y))

                if (n_x,n_y) == end:
                    dead = True
                    break

    current = end
    path = [current]

    while current != start:
        path.append(parents[current])
        current = parents[current]

    for i, (x,y) in enumerate(path[1:-1][::-1]): 
        i = (i + 1) % 10
        rows[y] = rows[y][:x] + str(i) + rows[y][x+1:]

    for row in rows:
        print(row)

    if o != N-1:
        print()