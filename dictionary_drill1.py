student = {
    "name" : "aman",
    "marks" : 72,
    "attendance" : 68,
    "passed" : True,
    "eligible_for_exam" : True
}

if student["marks"] < 40:
    student["passed"] = False

else:
    student["passed"] = True

if student["attendance"] < 75:
    student["eligible_for_exam"] = False

else:
    student["eligible_for_exam"] = True

print(student)