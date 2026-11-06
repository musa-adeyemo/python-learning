name = input("Enter your name: ")

while name == "":
    print("Name is compulsory.")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("What's your age? "))

while age < 0:
    print("Invalid age")
    age = int(input("What's your age? "))
print(f"Your age({age}) has been confirmed.")

favourite = input("Enter your favourite person name(q to quit): ").lower()

while not favourite == "q":
    print(f"Your favourite person is {favourite}")
    favourite = input("Enter your next favourite person name(q to quit): ").lower()

print("My regards to them all.")