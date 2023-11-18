N = int(input())

total_stitches = 6
max_stitch = 1 
to_go = 6

left = 0
right = 6


for _ in range(N):
    a = input()
    ins = a[0]
    x = int(a[1:])

    if ins == "I":
        total_stitches += (x-1)
        
        left += x
        right -= 1

        if right < 0:
            right = right+left-x
            left = x
            max_stitch += 1

    if ins == "D":
        total_stitches -= (x-1)

        left += 1
        right -= x

        if right < 0:
            right = right+left-1
            left = 1
            max_stitch += 1

print(right + left)
print(max_stitch)