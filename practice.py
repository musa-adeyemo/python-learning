# Practice of string methods

print("""My name is Musa.
I'm a boy""")
print('''My name is Musa.
I'm a boy''')

room_type_code = input("What's the code for your room type: \"STD\" for"
"standard at & $100/night, \"SUT\" for Suite at $300/night, \"DLX\" for deluxe"
" at $180/night)? ").strip().upper()

print(room_type_code)

name = input("What's your name? ")
phone_number = input("What's your phone number? ")
print(len(name))
print(name.find("B"))
print(name.rfind("B") )
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.isalnum())
print(phone_number.count("1"))
print(phone_number.replace("-", " "))
# print(help(str))

 