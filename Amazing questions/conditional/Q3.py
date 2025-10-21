# User se 3 numbers lo aur check karo ki unme se sabse bada kaun hai.

num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))
num3 = int(input("Enter c: "))

if (num1 > num2) and (num1 > num3):
    print(f"{num1} is the largest number")
elif (num2 > num1) and (num2 > num3):
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")
