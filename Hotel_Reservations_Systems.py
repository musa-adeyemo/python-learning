# Hotel Reservation & VIP Badge System.

name = input("What is your name? ").strip().title()

nights_stayed = int(input("How many night have you stayed here? ").strip())

room_type_code = input("What's the code for your room type: `STD` for"
"standard at & $100/night, `SUT`  for Suite at $300/night, `DLX` for deluxe"
" at $180/night)? ").strip().upper()

if not room_type_code.isalpha():
    print("The Room Type Code has to be a letter.")

memebership_id = input("What's your membership Id(VIP-9942 or GUEST)? ").upper()

if room_type_code == "STD":
    room_type_amount = 100
elif room_type_code == "DLX":
    room_type_amount = 180
elif room_type_code == "SUT":
    room_type_amount = 300
else:
    room_type_amount = 100

sub_total = nights_stayed * room_type_amount

long_stay_discount = 50 if nights_stayed > 5 else 0

total_room_cost = sub_total - long_stay_discount

vip_discount = 15 / 100 * total_room_cost if memebership_id.startswith("VIP") else 0

vip_discounted_total = total_room_cost - vip_discount

tax = 7.5 / 100 * vip_discounted_total
total = vip_discounted_total + tax
total = total if total >= 0 else 0

print("\n ---RECEIPT---")
print(f"Customer_name:  {name}")
print(f"The number of night spent here is {nights_stayed} night(s)")
print(f"The room type({room_type_code}) amount:       ${room_type_amount}")
print(f"The sub_total:                   ${sub_total:.2f}")
print(f"The long stay dicount amount:    ${long_stay_discount:.2f}")
print(f"The total room cost:             ${total_room_cost:.2f}")
print(f"The VIP discount amount:         ${vip_discount:.2f}")
print(f"The vip discounted price:        ${vip_discounted_total:.2f}")
print(f"Tax_amount:                      ${tax:.2f}")
print(f"Total_amount:                    ${total:.2f}")
print(f"\nThank you {name} for your stay with us, we hope to see you again.")