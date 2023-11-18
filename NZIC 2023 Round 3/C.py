import copy

n_pin, n_bamboo, n_character = map(int, input().split())

pins = list(map(int, input().split()))
bamboos = list(map(int, input().split()))
characters = list(map(int, input().split()))

if not 1 in pins and not 9 in pins and not 1 in bamboos and not 9 in bamboos and not 1 in characters and not 9 in characters:
    simple = True
else: 
    simple = False

def is_complete(p, b, c):
    
    # base case
    if sorted([len(p), len(b), len(c)]) == [0, 0, 2]:
        if len(p) == 2:
            if p[0] == p[1]: return True
            else: return False
        if len(b) == 2:
            if b[0] == b[1]: return True
            else: return False
        if len(c) == 2:
            if c[0] == c[1]: return True
            else: return False

    # recusive
    for i in range(1,10):
        # P
        if i in p and i+1 in p and i+2 in p:
            np = copy.deepcopy(p)
            
            np.remove(i)
            np.remove(i+1)
            np.remove(i+2)

            if is_complete(np, b, c):
                return True

        if p.count(i) >= 3:
            np = copy.deepcopy(p)
            
            np.remove(i)
            np.remove(i)
            np.remove(i)

            if is_complete(np, b, c):
                return True
            
        # B
        if i in b and i+1 in b and i+2 in b:
            nb = copy.deepcopy(b)
            
            nb.remove(i)
            nb.remove(i+1)
            nb.remove(i+2)

            if is_complete(p, nb, c):
                return True

        if b.count(i) >= 3:
            nb = copy.deepcopy(b)
        
            nb.remove(i)
            nb.remove(i)
            nb.remove(i)

            if is_complete(p, nb, c):
                return True

        # C
        if i in c and i+1 in c and i+2 in c:
            nc = copy.deepcopy(c)
            
            nc.remove(i)
            nc.remove(i+1)
            nc.remove(i+2)

            if is_complete(p, b, nc):
                return True

        if c.count(i) >= 3:
            nc = copy.deepcopy(c)
            
            nc.remove(i)
            nc.remove(i)
            nc.remove(i)

            if is_complete(p, b, nc):
                return True
    return False




complete = is_complete(pins, bamboos, characters)

if simple and complete:
    print("WIN")
elif simple:
    print("SIMPLE")
elif complete:
    print("COMPLETE")
else:
    print("SAD")