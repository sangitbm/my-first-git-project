number_of_people = int(input("Enter the number of students:"))
count = 1

while count <= number_of_people:
    name = input(f"Enter name of student {count}:")
    age = int(input(f"Enter age of {name}:"))
    subject1 = float(input(f"Enter score of subject 1:"))
    subject2 = float(input(f"Enter score of subject 2:"))
    subject3 = float(input(f"Enter score of subject 3:"))
    average_score = (subject1+subject2+subject3)/3

    if average_score >=90:
        grade = "A"

    elif average_score >= 75:
        grade = "B"

    elif average_score >= 60:
        grade = "C"

    else:
        grade = "Fail"

    print(f"{name} | Age:{age} | Average Score:{average_score:.2f} | Grade:{grade}")

    count += 1


        

    

