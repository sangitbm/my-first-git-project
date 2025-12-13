name = input("Enter your name:")
marks = int(input("Enter your marks (0-100):"))
extra_credit = input("Did you receive extra credit? (yes/no)")=="yes"

if marks >= 80 :
    print("Hello",name,",","your final grade is: Distinction")

elif marks >= 60:
    print("Hello",name,",","your final grade is: Pass")

elif marks >= 40:
    print("Hello",name,",","your final grade is: Average")

elif extra_credit and marks >= 35:
    print("Hello",name,",","your final grade is: Average")

else:
    print("Hello",name,",","your final grade is: Fail")


