'''
User se year input lo aur check karo:

Agar year leap year hai → print "Leap Year"
Agar year normal year hai → print "Not a Leap Year"

Leap year rules:
Agar year 400 se divisible → Leap year
Agar year 100 se divisible → Not a leap year
Agar year 4 se divisible → Leap year
Baaki → Not a leap year
'''

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
