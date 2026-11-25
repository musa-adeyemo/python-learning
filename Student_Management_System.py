# Project: Student Management System

print("=" * 35)
print(f"{'STUDENT MANAGEMENT SYSTEM':^35}")
print("=" * 35)
print("\n1. Register a new system")
print("2. View all students")
print("3. Search for a student")
print("4. Update studnt information")
print("5. Delete a student")
print("6. Calculate student results")
print("7. Display class Statistics")
print("8. Exit")
choice = int(input("Enter the number of your choice: "))

if choice == 1:
    full_name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    matriculation_number = input("Enter your matriculation number: ")
    department = input("Enter your department: ")
    scores = input("Enter your scores in five courses: ")