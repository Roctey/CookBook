prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)  # (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)  # (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)  # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

