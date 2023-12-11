N = int(input())
toddy_skills = list(map(int, input().split()))
rival_skills = list(map(int, input().split()))

toddy_skills.sort()
rival_skills.sort()

toddy_pointer = 0
count = 0

# print(toddy_skills, rival_skills)

for index, skill in enumerate(rival_skills):
    while toddy_skills[toddy_pointer] < skill:
        toddy_pointer += 1
        if toddy_pointer >= N:
            print(count)
            exit()
    count += 1
    toddy_pointer += 1
    if toddy_pointer >= N:
        print(count)
        exit()

print(count)