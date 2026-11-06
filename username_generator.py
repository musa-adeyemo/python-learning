name = input("Enter your name: ").strip().title()
gmail = input("Enter your gmail: ").strip()
working = gmail.find("@")
first_name = gmail[:working]

username = f"{name} {first_name}"
print(username)
print(name + " " + first_name)