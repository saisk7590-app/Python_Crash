first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
age = int(input("Enter your age: "))

print("Hello", full_name)
print("Next year you will be", age + 1)

# Length without spaces
print("Total characters (no spaces):", len(full_name.replace(" ", "")))

print(full_name.upper())
print(full_name.lower())
print(full_name[0])
print("Your initials are:", first_name[0] + last_name[0])