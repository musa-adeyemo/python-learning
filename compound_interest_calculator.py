# Compound interest calculator
# import math

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the priniple amount: "))
    if principle <=0:
        print("Principle must be greater than zero(0).")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <=0:
        print("Interest rate must be greater than zero(0).")

while time <= 0:
    time = float(input("Enter the time in year(s): "))
    if time <=0:
        print("Time must be greater than zero(0).")

amount = round(principle * pow((1 + rate / 100), time))
compound_interest = amount - principle
# print(f"{compound_interest:.2f}")
# print(math.ceil(compound_interest))

print(f"Compound interest: ${compound_interest}")
print(f"Amount: ${amount}")
