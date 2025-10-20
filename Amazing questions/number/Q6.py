# User se ek number lo aur check karo ki wo positive, negative, ya zero hai.

# user input
num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number")
elif num < 0:
    print(f"{num} is a negative number")
else:
    print("The number is zero")

