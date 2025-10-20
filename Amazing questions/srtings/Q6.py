# User se string lo aur check karo ki wo uppercase, lowercase ya mixed hai.

# user input
text = input("enter a string: ")

if text == text.upper():
    print("sritng is in uppercase")
elif text == text.lower():
    print("string is in lowercase")
else:
    print("string is mixed")