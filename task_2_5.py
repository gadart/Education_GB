prices = [57.8, 46.51, 97, 35.12, 56.76, 12.1, 39.98, 95.54, 39.54, 34.2]
prices_formated = []

for price in prices:
    price = int(round(price * 100))
    rub = price // 100
    penny = price % 100
    prices_formated.append(f'{rub:02d} руб {penny:02d} коп',)

print(prices)
print(prices_formated)
print(id(prices_formated))
prices_formated.sort()
print(prices_formated)
print(id(prices_formated))
down_prices = sorted(prices_formated, reverse=True)
print(down_prices)
sorted_prices = sorted(down_prices[:5], reverse=True)
print(sorted_prices)