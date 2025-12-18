#List to store all students
all_students = []

#ask how many students
total_students = int(input("Enter number of students:"))

#loop for each studentt

for i in range(total_students):
    student = {} #create a new dictionary for each student

    #input student details
    student["name"] = input("Enter the name of student:")
    student["marks"] = int(input("Enter marks:"))
    student["attendance"] = int(input("Enter attendance:"))

    #Determine if passed or failed

    if student["marks"]>= 45:
        student["passed"] = True
    
    else:
        student["passed"] = False

    if student["attendance"] >= 70:
        student["eligible_for_exam"] = True
    
    else:
        student["eligible_for_exam"] = False

    #add student record to the list
    all_students.append(student)

print("\nStudent Records:")
print("_" * 75)

for s in all_students:
    print(f"Name: {s["name"]} | Marks: {s["marks"]} | Attendance: {s["attendance"]}% | Passed: {s["passed"]} | Eligible for Exam: {s["eligible_for_exam"]}")


