import pandas as pd
asking_input = input("Enter asking prices separated by commas: ")
asking_prices = pd.Series([int(price) for price in asking_input.split(',')])

fair_input = input("Enter fair prices separated by commas: ")
fair_prices = pd.Series([int(price) for price in fair_input.split(',')])

good_deal_indices = asking_prices[asking_prices < fair_prices].index.tolist()

print("\nAsking Prices:\n", asking_prices)
print("\nFair Prices:\n", fair_prices)
print("\nGood Deal Indices:", good_deal_indices)
