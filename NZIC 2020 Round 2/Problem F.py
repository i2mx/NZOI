
N, K = map(int, input().split())
packing = [0]
for _ in range(N):
    box_width = int(input())
    lowest_avaliable_row = -1
    
    for i in range(0, len(packing)):
        if K - packing[i] >= box_width:
            lowest_avaliable_row = i
        else: 
            break

    if lowest_avaliable_row == -1:
        packing.insert(0, box_width)
    else:
        packing[lowest_avaliable_row] += box_width

print(len(packing))