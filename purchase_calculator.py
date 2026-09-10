# Dynamic unit & Tax calculator

unit_price = float(input("What's the unit price of the good purchased? "))
quantity = int(input("What is the quantity of good purchased? "))
state_code = input("What's the state code(e.g CA, NY, TX.)? ").upper()

price = unit_price * quantity
discount = (10/100 * price) if quantity >= 10 else 0
discounted_price = price - discount

shipping_fee = 0 if discounted_price > 50 else 10 

# tax_rate 

if state_code == "CA":
    tax_rate = 8.5 / 100
elif state_code == "NY":
    tax_rate = 4.0 / 100
elif state_code == "TX":
    tax_rate = 6.25 / 100
else:
    tax_rate = 5.0 / 100

tax_amount = discounted_price * tax_rate

# Vip perk
vip = input("Are you a VIP? ").lower()
vip_discount = 5.0 if vip == "yes" else 0

# Total
total_before_vip = discounted_price + shipping_fee + tax_amount
final_total = total_before_vip - vip_discount
final_total = final_total if final_total > 0 else 0

print("\n--- RECEIPT---")
print(f"Subtotal:               ${price:.2f}")
print(f"Discount:              -${discount:.2f}")
print(f"shipping-fee:           ${shipping_fee:.2f}")
print(f"Tax({state_code}):                ${tax_amount:.2f}")
print(f"VIP-Discount:           ${vip_discount:.2f}")
print(f"Total-Amount:           ${final_total:.2f}")