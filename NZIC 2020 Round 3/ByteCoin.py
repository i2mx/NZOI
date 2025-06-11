inf = 10**10

_, money = map(int, input().split())
buy_prices = list(map(int, input().split()))
sell_prices = list(map(int, input().split()))

min_buy_price = inf

for buy, sell in zip(buy_prices, sell_prices):
    min_buy_price = min(min_buy_price, buy)
    if sell > min_buy_price:
        money = sell * (money // min_buy_price) + (money % min_buy_price)
        min_buy_price = buy

print(money)
