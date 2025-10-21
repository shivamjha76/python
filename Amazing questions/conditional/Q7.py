'''
User se 3 numbers lo aur check karo:

Agar sab numbers equal hain → “All numbers are equal”
Agar sirf do numbers equal hain → “Two numbers are equal”
Agar sab alag hain → “All numbers are different”
'''

num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))
num3 = int(input("Enter c: "))

if num1 == num2 == num3:
    print("All numbers are equal")
elif (num1 == num2) or (num1 == num3) or (num2 == num3):
    print("Two number are equal")
else:
    print("All numbers are different")