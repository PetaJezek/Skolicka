import sys
'''
prices = [10, 30, 20, 50]
prices = list(map(int, prices))
'''
inputData = sys.stdin.read()
prices = list(map(int, inputData.split()))



prices.sort()
n = len(prices)

loc_price = prices[0]
loc_revenue = loc_price * (n)
revenue = loc_revenue
idx = 0
price = prices[0]
for i in range(len(prices)):
    if prices[i] != loc_price:
        loc_price = prices[i]
        loc_revenue = loc_price * (n - i)
        if revenue < loc_revenue:
            revenue = loc_revenue     
            price = prices[i]


print(price)


