def maxProfit(prices):
    cheapest_stock_price = min(prices)
    cheapest_price_index = prices.index(cheapest_stock_price)

    arr = prices[cheapest_price_index:]

    if len(arr) <= 1:
        return 0

    return max(arr) - cheapest_stock_price


arr = [2, 4, 1]

print(maxProfit(arr))
