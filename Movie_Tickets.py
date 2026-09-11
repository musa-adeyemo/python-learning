# Smart Movie Tickets & Concession kiosk

age = int(input("How old are you? "))

if age < 12:
    price = 8
elif age >= 12 and age < 65:
    price = 14
else:
    price = 10

matinee = input("Are you attending a matinee before 5pm(Y/N)? ").upper()

matinee_discount = 3 if matinee == "Y" else 0
discounted_price = price - matinee_discount

is_student = input("Are you a student(Y/N)? ").upper()
student_discount = 2 if age > 12 and age < 25 and is_student == "Y" else 0
student_discounted_price = discounted_price - student_discount

is_snack = input("Do you want a combo snack - popcorn + drink(Y/N)? ").upper()
combo_cost = 7 if is_snack == "Y" else 0

grand_total = student_discounted_price + combo_cost

print("\n ---RECEIPT---")

print(f"Sub_Total:                 ${price}")
print(f"Discounted_Price:          ${student_discounted_price}")
print(f"Snack_Cost:                ${combo_cost}")
print(f"Grand_Total:               ${grand_total}")

print(f"\n Thanks for shopping with us, your total price is ${grand_total}")