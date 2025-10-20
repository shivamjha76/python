# Ek program likho jo user se ek string le aur check kare ki wo palindrome hai ya nahi.
# (Palindrome = jo string ulta karne par bhi same rahe, jaise madam ya 121

# user se input
text = input("Enter a word: ")

reversed_text = text[::-1]

# Check palindrome
if text == reversed_text:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

# text[::-1] ka matlab hai string ko reverse karna. Isko tod ke dekhte hain:
# text[start:stop:step] ye Python ka slice syntax hai.
# start → kahan se start karna hai (agar blank chhodo, start se start hoga)
# stop → kahan tak jaayega (agar blank chhodo, string ke end tak)
# step → kitne step me move kare (agar negative ho to ulta direction)
# To text[::-1] ka matlab:
# start aur stop blank → pura string consider karo
# step = -1 → ulta direction me ek-ek character lete hue string banao

# example 
str = "hello"
print(str[::-1]) # output = olleh