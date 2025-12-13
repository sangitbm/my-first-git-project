students_number = int(input("How many students?"))
count = 1

while count <= students_number:
    count = count + 1

    students_name = input("Enter student name:")
    score = int(input("Enter score:"))

    if score >= 90:
        print("Grade: A")

    elif score >= 75:
        print("Grade: B")

    elif score >= 60:
        print("Grade: C")

    else:
        print("Fail")


