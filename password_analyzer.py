# Terminal Security & password analyzer.

#  Build a custom-line security tools that register a user, validates a strong password,masks their credentials, and runs a simulated 
# brute-force/countdown lock if they fail login attempts.


while True:
    username = (input("Enter your username: ")).strip()

    if len(username) <  4 or len(username) > 15:
        print("Invalid Username: must be a 4-15 characters long.")
    elif " " in username:
        print("Username must not contain space(s), try a new one!")
    else:
        username = username.capitalize()
        break

special_chars = "!@#$%&*"
while True:
    password = input("Input your password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if len(password) < 8:
        print("Error: password must be at least 8 characters long.")
    elif not has_upper:
        print("Error: password must contain at least one uppercase letter.")
    elif not has_lower:
        print("Error: password must contain at least one lowercase letter.")
    elif not has_digit:
        print("Error: password must contain at least one digit.")
    elif not has_special:
        print("Error: password must at least one special character.(!@#$%&*)")
    else:
        print("Password accepted!")
        break
password_length = len(password) - 2
masked_password = (f"{password[0]}{"*" * password_length}{password[-1]}")
password_strenght_score = min(100, len(password) * 8)
print("\n --------RECEIPT--------")
print(f"{'Username':<16}: {username:>20}")
print(f"{'Masked-Password':<16}: {masked_password:>20}")
print(f"{'Password-Score':<16}: {password_strenght_score:>20}")

import time
attempts = 3
while attempts > 0:
    login_pass = input("Enter your password to login: ")
    if login_pass == password:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        print(f"Wrong password: {attempts} attempt(s) left.")

        if attempts == 0:
            for seconds in range(10, 0, -1):
                print(f"Locked out! Try again in {seconds}s...")
                time.sleep(1)
            attempts = 3