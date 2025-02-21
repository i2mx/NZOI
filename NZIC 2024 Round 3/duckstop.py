D, C, A = map(int, input().split())
prices = list(map(int, input().split()))

capital = C
rubber_ducks = 0
buy_price = 0
actions = []

suffix_max = [0] * D
suffix_max[-1] = prices[-1]
for i in range(D - 2, -1, -1):
    suffix_max[i] = max(suffix_max[i + 1], prices[i])

for i in range(D):
    price = prices[i]
    
    if i == D - 1:
        if rubber_ducks > 0:
            actions.append(f"SELL {rubber_ducks}")
            capital += rubber_ducks * price
            rubber_ducks = 0
        else:
            actions.append("WAIT")
        break
    
    if rubber_ducks > 0:
        if price > buy_price:
            actions.append(f"SELL {rubber_ducks}")
            capital += rubber_ducks * price
            rubber_ducks = 0
            buy_price = 0
        else:
            actions.append("HOLD")
    else:
        if price <= A and price <= capital:
            if suffix_max[i+1] > price:
            # if any(prices[j] > price for j in range(i + 1, D)):
                num_ducks = capital // price
                capital -= num_ducks * price
                rubber_ducks += num_ducks
                buy_price = price
                actions.append(f"BUY {num_ducks}")
            else:
                actions.append("WAIT")
        else:
            actions.append("WAIT")

profit = capital - C

for action in actions:
    print(action)
print(profit)
