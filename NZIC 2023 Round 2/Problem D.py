a,b,c = map(int, input().split())
d,e,f = map(int, input().split())
g,h,i = map(int, input().split())

M = [[a,b,c], [d,e,f], [g,h,i]]
N = [a,b,c,d,e,f,g,h,i].count(0)

if N <= 2:
    for possible_sum in [[a,b,c], [d,e,f], [g,h,i], [a,d,g], [b,e,h], [c,f,i]] :
        if not 0 in possible_sum:
            true_sum = sum(possible_sum)
            for i in range(3):
                for j in range(3):
                    if M[i][j] == 0:
                        other_i = [0,1,2]
                        other_i.remove(i)

                        other_j = [0,1,2]
                        other_j.remove(j)

                        if not 0 in [M[i][other_j[0]], M[i][other_j[1]]]:
                            M[i][j] = true_sum - M[i][other_j[0]] - M[i][other_j[1]]

                        if not 0 in [M[other_i[0]][j], M[other_i[1]][j]]:
                            M[i][j] = true_sum - M[other_i[0]][j] - M[other_i[1]][j]


else:
    for possible_sum in [[a,b,c], [d,e,f], [g,h,i], [a,d,g], [b,e,h], [c,f,i]] :
        if not 0 in possible_sum:
            true_sum = sum(possible_sum)
            for i in range(3):
                for j in range(3):
                    if M[i][j] == 0:
                        other_i = [0,1,2]
                        other_i.remove(i)

                        other_j = [0,1,2]
                        other_j.remove(j)

                        if not 0 in [M[i][other_j[0]], M[i][other_j[1]]]:
                            M[i][j] = true_sum - M[i][other_j[0]] - M[i][other_j[1]]

                        if not 0 in [M[other_i[0]][j], M[other_i[1]][j]]:
                            M[i][j] = true_sum - M[other_i[0]][j] - M[other_i[1]][j]

for i in M:
    for j in i:
        print(j, end=" ")
    print()
