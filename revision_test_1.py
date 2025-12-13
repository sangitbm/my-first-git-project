#ask the user
number_of_students = int(input("How many students?"))

count = 1

while count<=number_of_students:

    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    score = int(input("Enter your score:"))

    if age < 18:
        print("Not eligible (underage)")

    
    else:
        if score >= 90:
            print("Grade A")
        
        elif score >=75:
            print("Grade B")

        elif score >= 60:
            print("Grade C")

        else:
            print("Fail")

    count = count + 1
