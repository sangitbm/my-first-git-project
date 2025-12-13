name = input("Enter your name:")
marks = int(input("Enter your obtained number:"))

if marks >= 80:
    print("Hello",name, "your result is: Distinction")

elif marks >=60:
    print("Hello",name, "your result is: Pass")

elif marks >= 40:
    print("Hello",name, "your result is: Average")

else:
    print("Hello",name, "your result is: Fail")

