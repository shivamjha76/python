'''
User se marks lo (0 to 100) aur grade print karo:

Marks ≥ 90 → “A+”
Marks 80 to 89 → “A”
Marks 70 to 79 → “B”
Marks 60 to 69 → “C”
Marks 50 to 59 → “D”
Marks < 50 → “Fail
'''
marks = int(input("Enter marks: "))

if marks >= 90 and marks <=100:
    print("A+")
elif marks >= 80 and marks <= 89:
    print("A")
elif marks >=70 and marks <=79:
    print("B")
elif marks >=60 and marks <=69:
    print("C")
elif marks >=50 and marks <=59:
    print("D")
elif marks < 50 and marks >= 0:
    print("Fail")
else:
    print("Invalid marks number")