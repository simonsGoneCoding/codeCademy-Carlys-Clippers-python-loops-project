hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]



# 1
total_price = 0

# 2
for i in prices: 
  total_price += i

# 3, 4
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# 5, 6
new_prices = [price - 5 for price in prices]
print(new_prices)


# Revenue:
# 7
total_revenue = 0 

# 8, 9, 10
for i in range(len(hairstyles)):
  total_revenue = prices[i] * last_week[i]
print("Total revenue: " + str(total_revenue))

# 11
average_daily_revenue = total_revenue / 7
print("%.2f" %average_daily_revenue)

# 12
cuts_under_30= [price for price in new_prices if price < 30 ]
print(cuts_under_30)