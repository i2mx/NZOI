N = int(input())
time = sum([int(input()) for _ in range(N)])

string = "It took "

hour = time // 60
if hour == 1:
    string += f"{hour} hour "
elif hour > 1:
    string += f"{hour} hours "

minute = time % 60

if hour and minute:
    string += "and "

if minute == 1:
    string += f"{minute} minute"
elif minute > 1:
    string += f"{minute} minutes"

print(string)