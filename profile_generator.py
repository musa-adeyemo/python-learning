# Personal Profile Generator

first_name = input("What's your first name? ").strip().capitalize()
last_name = input("What's your last name? ").strip().capitalize()
age = int(input("What's your age? "))
country_name = input("What's the name of your country? ").strip().capitalize()
favourite_programming_language = input("What's your favourite programming language? ").strip().capitalize()
programming_language_writeup = input("Provide a short writeup as why you want to learn programming? ").strip()
username = first_name[:3].lower().strip()
initials = f"{first_name[0]}{last_name[0]}"

print("\n PERSONAL PROFILE")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Country: {country_name}")
print(f"Favourite Language: {favourite_programming_language}")
print(f"Username: {username}")
print(f"Initials: {initials}")
print(f"About: \n{programming_language_writeup}")