""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Ginger (G)                                                               │
  │ Chamomile (C)                                                            │
  │ Earl Grey (E)                                                            │
  │ Peppermint (P)                                                           │
  │ Lemon (L)                                                                │
  │ Strawberry (S)                                                           │
  └──────────────────────────────────────────────────────────────────────────┘
 """

def get_sucess_discriptor(n : int) -> str:
    if n == 0:
        return "Successful"
    if n <= 2:
        return f"Mildly Successful ({n})"
    return f"Disaster ({n})"


favteas = {"G": 0, "C": 0, "E": 0, "P": 0, "L": 0, "S": 0}
sucessfullness = {}

N, K = map(int, input().split())

for _ in range(N):
    name, tea = input().split()
    favteas[tea] += 1

for _ in range(N):
    i = input().split()
    name = i[0]
    teas = list(map(int, i[1::]))

    sucessfullness[name] = sum(list(map(lambda x: max(0, x[1]-x[0]) , zip(teas, favteas.values()))))

for _ in range(K):
    name = input()    
    print(f"{name} {get_sucess_discriptor(sucessfullness[name])}")