# Automated Freelance Invoice & Security Token Generator

freelancer_name = input("What is your name? ").title().strip()
client_company_name = input("What is the client company name? ").upper().strip().replace(" ", "").replace("-", "")
hourly_rate = float(input("What is your hourly rate? "))
total_hours_worked = int(input("How many hour(s) did the work take you? "))
project_urgency_level = input("What is the project urgency level(`HIGH`, `MEDIUM` or `LOW`)? ").upper()

client_company_code = client_company_name[:3]
code_no = str(total_hours_worked)
invoice_id = client_company_code + "-" + code_no

base_pay = hourly_rate * total_hours_worked
if total_hours_worked > 40:
    overtime = total_hours_worked - 40
    overtime_pay = overtime * 1.5
    overtime_total = base_pay + overtime_pay
    urgency_charge = 20 / 100 * overtime_total if project_urgency_level == "HIGH" else 0
    total = base_pay + urgency_charge
else:
    urgency_charge = 20 / 100 * base_pay if project_urgency_level == "HIGH" else 0
    total = base_pay + urgency_charge

print("\n ---Receipt---")
print(f"Your invoice Id: {invoice_id}")
print(f"Base_Pay:                      ${base_pay:.2f}")
print(f"Project_Urgency_Payment:       ${urgency_charge}")
print(f"Total_Amount:                  ${total:.2f}")

print(f"\n Thank you {client_company_name}")