# Smart E-commerce Order & Promo Sanitizer

customer_name = input("What is your full name? ").strip().title()
item_unit_price = float(input("What's the item unit price of the goods purchased?").strip())
quantity = int(input("What is the quantity of the purchased good? ").strip())

sub_total = item_unit_price * quantity

discount = 10 / 100 * sub_total if quantity >= 10 else 0
discounted_price = sub_total - discount
total_price = discounted_price if discounted_price > 0 else 0

print("\n ---RECEIPT---")
print(f"Thank you for patronizing us: {customer_name}")
print(f"Sub_Total:      ${sub_total:.2f}")
print(f"Discount:       ${discount:.2f}")
print(f"Total:          ${total_price:.2f}")