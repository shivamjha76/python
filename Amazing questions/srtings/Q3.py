# User se ek string lo aur usme kitni vowels (a, e, i, o, u) hain ye count karke print karo.

text = input("Enter a string: ")
count = 0

for char in text.lower():  # lower() se capital letters bhi count ho jayenga
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)