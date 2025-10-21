'''
User se time in hours (0 to 23) lo aur print karo greeting:

0 to 11 → “Good Morning”
12 to 15 → “Good Afternoon”
16 to 19 → “Good Evening”
20 to 23 → “Good Night”
Agar number valid nahi → “Invalid time”
'''

time = int(input("Enter time in hour: "))

if time >=0 and time <=11:
    print("Good Morning")
elif time >=12 and time <=15:
    print("Good Afternoon")
elif time >=16 and time <=19:
    print("Good Evening")
elif time >=20 and time <=23:
    print("Good night")
else:
    print("Invalid time")