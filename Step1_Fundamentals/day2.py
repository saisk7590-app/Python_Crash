name = input("Enter your name: ")
age = int(input("Enter your age: "))
Dress_code = input("Enter your dress code (formal/casual): ").lower()
has_id = input("Do you have an ID? (yes/no): ").lower()

print("\n Checking entry for", name)

if age < 18:
    decision ="Not allowed(underage)"
elif age >=18 and has_id == "yes" and Dress_code == "formal":
    decision = "Allowed"
elif age >=18 and has_id ==  "no":
    decision = "Not allowed(no ID)"
else:
    decision = "Not allowed(dress code)"

print("Welcome", name + "!", "Entry decision:", decision)