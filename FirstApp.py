# Program to take student details as input

firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
gpa = float(input("Enter GPA: "))
gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))

print("\n--- Student Details ---")
print(f"First Name : {firstname}")
print(f"Last Name  : {lastname}")
print(f"GPA        : {gpa}")
print(f"Gender     : {gender}")
print(f"Age        : {age}")
