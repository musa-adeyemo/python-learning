# Project Overview

# You are hired by an international logistics hub to build a single-pass terminall auditing program. The system
# takes raw, unformatted payload data from incoming transport ships, cleans and parses securityt codes, perform complex
# tariff/math calculations, evaluates risk levels, and prints a formatted security clearance invoice.

import math

raw_manifest_code = input("What's your raw payload string? (e.g., 'cargo-7890-CONTAINER-XYZ-2026'). ").strip().upper()
gross_weight_lbs = float(input("Input your cargo weight as a floating point number: "))
travel_distance_nm = float(input("Distance in nautical miles as a floating point number? "))
security_passcode = input("Enter your 8-digit passcode: ")
while len(security_passcode) != 8: 
    print("The password input isn't exactly 8, please check it again.")
    security_passcode = (input("Enter your 8-digit passcode: ")).strip()
security_passcode = int(security_passcode)

base_tax_rate, hazard_surcharge = 0.12, 0.05
base_tax_rate, hazard_surcharge = (hazard_surcharge, base_tax_rate) if gross_weight_lbs > 5000 else (base_tax_rate, hazard_surcharge)
base_tax_amount = gross_weight_lbs * base_tax_rate
calculated_surcharge = gross_weight_lbs * hazard_surcharge

hyphen_count = raw_manifest_code.count("-")
container_find = raw_manifest_code.find("CONTAINER")
vessel_tag_start = raw_manifest_code.find("-", container_find)
hyphen_index = raw_manifest_code.rfind("-")
manifest_code_formatted = raw_manifest_code.replace("-", "/")

numerical_id = raw_manifest_code[6:10]
vessel_tag = raw_manifest_code[vessel_tag_start + 1 : -5]
scrambled_security_key = numerical_id[::-2]

containers_unit = math.ceil(gross_weight_lbs / 4500)
fuel_reserve_buffer = math.floor(travel_distance_nm / 12.5)
risk_perimeter_radius = math.sqrt(gross_weight_lbs)
perimeter_boundary_area = math.pi * math.pow(risk_perimeter_radius, 2)

if gross_weight_lbs < 20000.0 and travel_distance_nm < 1000.0 and not (security_passcode < 10000000):
    tier = "Tier1(PRIORITY CLEARANCE)"
elif gross_weight_lbs >= 8000.0 and gross_weight_lbs <= 20000.0 or travel_distance_nm > 1000.0 and\
    travel_distance_nm< 5000.0 and security_passcode >= 10000000:
    tier = "TIER2(STANDARD CLEARANCE)"
else:
    tier = "TIER3(HIGH RISK / DETAINED)"

inspection_fee = 500.00 if hazard_surcharge > 0.10 else 150.00
approval_status = "APPROVED" if tier == "Tier1(PRIORITY CLEARANCE)" or tier == "TIER2(STANDARD CLEARANCE)" else "REJECTED"
total_clearance_fee = base_tax_amount + calculated_surcharge + inspection_fee

print(f"Vessel({vessel_tag}) carrying Cargo ID({scrambled_security_key}) arrived after travelling ({travel_distance_nm}) miles. With ({containers_unit})\
 containers loaded, the automated terminal issued an audit status of ({approval_status}) under ({tier}) protocols.")

# RECEIPT GENERATOR
print("=" * 50)
print(f"{'ORBITAL FREIGHT CLEARANCE RECEIPT':^50}")
print("=" * 50)
print(f"{'Passcode Reference':<25} : {security_passcode:08}")
print(f"{'Vessel Designation':<25} : {vessel_tag}")
print(f"{'Manifest Code':<25} : {manifest_code_formatted}")
print("-" * 50)
print(f"{'Gross Cargo Weight':<25} : {gross_weight_lbs:>15.2f} lbs")
print(f"{'Base Tax Rate':<25} : {base_tax_rate:>15.2%}")
print(f"{'Hazard Surcharge':<25} : {hazard_surcharge:>15.2%}")
print(f"{'Calculated Surcharge':<25} : {f'+${calculated_surcharge:.2f}':>15}")
print(f"{'Inspection Fee':<25} : {f'+${inspection_fee:.2f}':>15}")
print("-" * 50)
print(f"{'TOTAL CLEARANCE FEE':<25} : {f'${total_clearance_fee:.2f}':>15}")
print(f"{'Approval Status':<25} : {approval_status:>15}")