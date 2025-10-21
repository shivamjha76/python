'''
User se uska age lo aur uske hisaab se print karo:

Age < 13 → "You are a child"
Age 13 to 19 → "You are a teenager"
Age 20 to 59 → "You are an adult"
Age 60 or above → "You are a senior citizen"
'''

age = int(input("Enter your age: "))

if age >= 1 and age <= 12:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 59:
    print("You are an adult")
elif age >= 60:
    print("You are a senior citizen")
else:
    print("Not a valid age")
