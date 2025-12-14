#options
running = True

while running:
    print("1. Check eligibility and grade")
    print("2. Exit")

    choose = int(input("Choose 1 or 2:"))
    
    if choose==1:

        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        score = int(input("Enter your score:"))
        grade = "N/A"
        eligibility = ""
             
        
        if age < 18:
            eligibility = "Not Eligible"

        else:
            eligibility = "Eligible"

        if score >= 90:
            grade = "A"

        elif score >= 75:
            grade = "B"

        elif score >= 60:
            grade = "C"

        else:
            grade = "Fail"

        #print("Your name is:",Name)
        #print("Your age is:", Age)
        #print("Your score is:", Score)
        print(f"{name} |Age:{age} | Eligible: {eligibility} | Score: {score} | Grade: {grade}")

        

    elif choose == 2:
        print("Program Exited")

        running = False

    else:
        print("Invalid Choice")







