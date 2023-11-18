import copy

A, B = map(int, input().split())

c2n = {"C": 4, "N": 3, "O": 2, "H": 1, ".": 0}

grid = [ list(map( lambda x: c2n[x], input() )) for _ in range(A)]

def at(grid, x , y):
    if x < 0:
        return 0
    if x >= A:
        return 0
    if y < 0:
        return 0 
    if y >= B:
        return 0
    
    return grid[x][y]

grid_copy = copy.deepcopy(grid)

for x, row in enumerate(grid):
    for y, cell in enumerate(row):
        moves = [ (x+1, y), (x-1, y), (x, y+1), (x, y-1) ]
        neighbours = list(map(lambda x: at(grid, x[0], x[1]), moves ))

        a = sum(map(lambda x: x > 0, neighbours))

        if a == cell:
            # print(x,y)
            for i in moves:
                if at(grid, i[0], i[1]) > 0:
                    grid_copy[i[0]][i[1]] -= 1
            grid_copy[x][y] = 0

        if a < cell:
            print("Invalid")
            exit()

for x, row in enumerate(grid_copy):
    for y,cell in enumerate(row):
        if cell < 0:
            grid_copy[x][y] = 0


# # ------------------------------------------



node_list = [grid_copy]

# print(grid_copy)

def fdhahfsahdf():
    node_grid = node_list.pop()
    
    # print(node_grid)
    
    for x, row in enumerate(node_grid):
        for y, cell in enumerate(row): 
            if at(node_grid, x, y) > 0:
                if cell == 1:
                    if at(node_grid, x, y+1) == 0 and at(node_grid, x+1, y) == 0:
                        return
                    
                    if at(node_grid, x, y+1) > 0:
                        now_node = copy.deepcopy(node_grid)
                        now_node[x][y+1] -= 1
                        now_node[x][y] -= 1

                        node_list.append(now_node)

                    if at(node_grid, x+1, y) > 0:
                        now_node = copy.deepcopy(node_grid)
                        now_node[x+1][y] -= 1
                        now_node[x][y] -= 1

                        node_list.append(now_node)

                elif cell == 2:
                    if at(node_grid, x, y+1) == 0 or at(node_grid, x+1, y) == 0:
                        return
                    
                    new_node = copy.deepcopy(node_grid)
                    new_node[x+1][y] -= 1
                    new_node[x][y+1] -= 1
                    new_node[x][y] -= 2

                    node_list.append(new_node)

                return
   
    print("Valid")
    exit()

while len(node_list) > 0:
    fdhahfsahdf()
print("Invalid")