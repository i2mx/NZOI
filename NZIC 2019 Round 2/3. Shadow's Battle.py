import bisect

N = int(input())

players = []
shadow_health = 60

players_attack = 0

for _ in range(N):
    p, a = map(int, input().split())
    players.append([p, 10, a])
    players_attack += a

players.sort()
p_shadow, a_shadow = map(int, input().split())

while True:
    shadow_slot = bisect.bisect(players, [p_shadow, 0, 0])

    if shadow_slot >= 1:
        victim = players[shadow_slot - 1]
        victim[1] -= a_shadow
        if victim[1] <= 0:
            players_attack -= victim[2]
            players.remove(victim)
            shadow_slot -= 1
            if len(players) == 0:
                print("Shadow wins!")
                exit()

    if shadow_slot < len(players):
        victim = players[shadow_slot]
        victim[1] -= a_shadow
        if victim[1] <= 0:
            players_attack -= victim[2]
            players.remove(victim)
            if len(players) == 0:
                print("Shadow wins!")
                exit()

    shadow_health -= players_attack
    if shadow_health <= 0:
        print(f"We win! Players alive: {str(list(map(lambda x:x[0], players))).replace('[', '').replace(']','').replace(',','')} ")
        exit()