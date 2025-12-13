name = input("Enter your name:")
age = int(input("Enter your age:"))
has_id = input("Do you have an ID? (yes/no)") == "yes"

if age >= 21 and has_id :
    print("Hello",name,",""you are eligible.")

else:
    print("Sorry",name,",""you are not eligible.")