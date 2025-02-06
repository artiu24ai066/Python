n=int(input("Enter the number of products:"))
items={}
for i in range(n):
    items.update({input("Enter the product name:"):input("Enter the price of the product:")})

item=input("Enter any product name you want to know the price of:")

if item in items:
    print(f"Price of {item} = ",items[item])
else:
    print("Sorry! I don't know it's price")
