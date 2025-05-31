name = input("Name: ")
Age = int(input("Age: "))
GPA = float(input("Enter your GPA: "))
FOI = str(input("Enter your Field of Interest: "))
graduated = str(input("Graduated? YES or NO: "))

if Age < 25 and GPA >= 3.5 and graduated == "Yes":
    print("You are eligible for the scholarship")