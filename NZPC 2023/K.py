n,t,m = map(int, input().split())
car_times = [int(input()) for _ in range(m)]

def changeint(leave_time,times):
    count = 0
    for i in times:
        if count >= n:
            break
        if i <= leave_time:


def asdf(times):
    t = set([times]):
    
    min_sol = 1000000000
    for i in range(t):
        min_sol = min(min_sol, i + asdf())
        