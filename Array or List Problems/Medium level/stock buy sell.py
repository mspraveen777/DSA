prices = [7, 2, 1, 5, 6, 4, 8, 10]

# Brute
# def buySellStock(prices):
#     n = len(prices)
#     maxProfit = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if prices[j] > prices[i]:
#                 maxProfit = max(maxProfit, prices[j] - prices[i])
#     return maxProfit


# print(buySellStock(prices))


# Optimal
def buySellStock(prices):
    n = len(prices)
    max_profit = prices[0]
    min_price = float("inf")
    for i in range(n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit


print(buySellStock(prices))
