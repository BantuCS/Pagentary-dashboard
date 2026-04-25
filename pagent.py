# Program to get the details of a contestant in a pageantry competition

print("=== Pageantry Competition - Contestant Registration ===\n")

# Contestant personal details
firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
nationality = input("Enter nationality: ")

# Competition details
contestant_number = int(input("Enter contestant number: "))
talent = input("Enter talent: ")
height = float(input("Enter height (in cm): "))
weight = float(input("Enter weight (in kg): "))

# Display contestant details
print("\n========== Contestant Details ==========")
print(f"Contestant #   : {contestant_number}")
print(f"Name           : {firstname} {lastname}")
print(f"Age            : {age}")
print(f"Gender         : {gender}")
print(f"Nationality    : {nationality}")
print(f"Height         : {height} cm")
print(f"Weight         : {weight} kg")
print(f"Talent         : {talent}")
print("========================================")
