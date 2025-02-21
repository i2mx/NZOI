# days,balance,min_price = map(int, input().split())
# stock_prices = list(map(int, input().split())) 

# original_balance = balance

# trades = []
# buy_price = 1e10
# currently_holding = False
# day_bought = None
# for index, value in enumerate(stock_prices):
#     if currently_holding:
#         if buy_price < value:
#             currently_holding = False
#             buy_price = 1e10
#             trades.append(('BUY', day_bought))
#             trades.append(('SELL', index))
#     else:
#         if value <= min_price:
#             if not currently_holding:
#                 currently_holding = True
#                 buy_price = value
#                 day_bought = index
# currently_holding = False
# buy_price = 0
# jindex = 0
# for index in range(days):
#     if jindex < len(trades) and  trades[jindex][1] == index:
#         if trades[jindex][0] == 'BUY':
#             currently_holding = True
#             stock_volume = balance//stock_prices[index]
#             balance -= stock_volume*stock_prices[index]
#             print('BUY', stock_volume)
#         else:
#             currently_holding = False
#             print('SELL', stock_volume)
#             balance += stock_volume*stock_prices[index]
#         jindex+=1
#     else:
#         if currently_holding:
#             print("HOLD")
#         else:
#             print("WAIT")



# print(balance-original_balance)
# # print(operations)