# Create a formatted receipt generator for 2 Item purchase.
item1 = input("What's the name of the first item? ")
item1_price = float(input("What's the price of ITEM1? "))

item2 = input("What's the name of the second item? ")
item2_price = float(input("What's the price of ITEM2? "))

item1_price = f"{item1_price:,.2f}"
item2_price = f"{item2_price:,.2f}"

item1_price = str(item1_price)
item2_price = str(item2_price)

print(f"\n{'------RECEIPT------':^40}")
print(f"{'ITEM':<20}{'PRICE':>20}")
print("-" * 40)
print(f"1.{item1:<19}{'$'+ item1_price:>19}")
print(f"2.{item2:<19}{'$'+ item2_price:>19}")