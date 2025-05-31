# name = input("Name: ")
Age = int(input("Age: "))
GPA = float(int(input("Enter your GPA (0 to 5): ")))
# FOI = str((input("Enter your Field of Interest: ")))
graduated = str(input("Graduated? YES or NO: ")).strip().lower()

if Age < 25 and GPA >= 3.5 and graduated == "yes":
    print("You are eligible for the scholarship")
elif Age < 30 and GPA >= 2.5:
    print("You are eligible for the Internship")
else:
    print("You are not eligible for any of the programs")