a,b,c = map(int, input().split())
d,e,f = map(int, input().split())
g,h,i = map(int, input().split())

def no_zero(r1,c1):
    return rows[r1].count(0) + cols[c1].count(0) >= 1

def rc_solve(r,c):
    orow = [0,1,2]
    orow.remove(r)
    
    ocol = [0,1,2]
    ocol.remove(c)


    if no_zero(r, ocol[0]):
        return sum(cols[ocol[0]]) - sum(rows[r])
    if no_zero(r, ocol[1]):
        return sum(cols[ocol[1]]) - sum(rows[r])
         
    
    if no_zero(orow[0], c):
        return sum(rows[orow[0]])-sum(cols[c])

    if no_zero(orow[1], c):
        return sum(rows[orow[1]])-sum(cols[c])
         
    # return 2*rows[r][c]

rows = [[a,b,c], [d,e,f], [g,h,i]]
cols = [[a,d,g], [b,e,h], [c,f,i]]

# while any([0 in row for row in rows]):
#     for i in range(3):
#         for j in range(3):
#             if rows[i][j] == 0:
#                 rows[i][j] = rc_solve(i,j)//2
#                 cols[j][i] = rc_solve(i,j)//2

print(rc_solve(1,1))

for i in rows:
    for j in i:
        print(j, end=" ")   
    print()