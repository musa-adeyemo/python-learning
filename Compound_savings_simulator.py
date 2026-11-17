# Compound savings & Loan Amortization Simulator

mode_selection = input("Choose a mode(savings Growth(S) or Loan payoff(L)): ").strip().upper()

while "S" not in mode_selection and "L" not in mode_selection:
    print("Error: Invalid mode selection.")
    mode_selection = input("Choose a mode(savings Growth(S) or Loan payoff(L)): ").strip().upper()
if "S" in mode_selection:
    starting_amount = float(input("Enter initial savings deposit: "))
    while starting_amount <= 0:
            print("Invalid: Initial savings deposit must be greater than zero.")
            starting_amount = float(input("Enter initial savings deposit: "))
elif "L" in mode_selection:
    starting_amount = float(input("Enter total loan amount to borrow: "))
    while starting_amount <= 0:
        print("Invalid: Initial savings deposit must be greater than zero.")
        starting_amount = float(input("Enter total loan amount to borrow: "))

annual_interest_rate = float(input("Input your annual interest rate(%): "))
while annual_interest_rate <= 0:
    print("Invalid: annual_interest_rate must be greater than zero.")
    annual_interest_rate = float(input("Input your annual interest rate: "))

month_duration = int(input("Enter your duration in month(S): "))
while month_duration <= 0:
    print("Invalid: month_duration must be greater than zero.")
    month_duration = int(input("Enter your duration in month(S): "))

monthly_rate = (annual_interest_rate / 100) / 12

balance = starting_amount
if "S" in mode_selection:
    monthly_deposit = float(input("Input your fixed monthly deposit: "))
    for month in range(1, month_duration +1):
        balance = balance + monthly_deposit
        interest = balance * monthly_rate
        balance = balance + interest
        print(f"{balance:,.2f}")
elif "L" in mode_selection:
    monthly_payment = float(input("How much do you plan to pay monthly? "))
    for month in range(1, month_duration + 1):
            monthly_interest = balance * monthly_rate
            while monthly_payment <= monthly_interest:
                print("Warning!!!  you won't be able to pay off the loan with that amount.")
                monthly_payment = float(input("How much do you plan to pay monthly? "))
            balance = (balance + monthly_interest) - monthly_payment
            if balance < 0:
                 break
            print(f"{balance:,.2f}")

print(f"\n{'--------RECEIPT--------':^50}")
print(f"\n{'Month':<8} | {'Interest':<12} | {'Balance':<14} | {'Progress':<8}")
print("-" * 62)