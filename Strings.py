# ------------------------ Strings in python ------------------------ #

# What are strings?
# strings are sequence of characters enclosed within single quotes(' ') or double quotes(" ").

# creating strings
str1 = 'Hello, shivam'
str2 = "Welcome to Python programming"
print(str1)
print(str2)

# checking the type of strings
print(type(str1))
print(type(str2))

# ----------------------------- String operations ----------------------------- #

# Concatenation
greeting = str1 + " - " + str2
print(greeting)

# Repetition
repeat_str = str1 * 3
print(repeat_str)

# Accessing characters in a string
first_char = str1[0]
last_char = str1[-1]
print("First character:", first_char)
print("Last character:", last_char)

# Slicing strings
substring = str2[11:17]
print("Substring:", substring)

# String methods
upper_str = str1.upper()
print("Uppercase:", upper_str)
lower_str = str2.lower()
print("Lowercase:", lower_str)
find_index = str1.find("shivam")
print("Index of 'shivam':", find_index)
replace_str = str2.replace("Python", "Java")
print("Replaced String:", replace_str)
split_str = str2.split(" ")
print("Split String:", split_str)

# String formatting
name = "Shivam"
age = 25
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)
f_string = f"My name is {name} and I am {age} years old."
print(f_string)

# Escape sequences
escape_str = "Hello,\nWelcome to\tPython programming!"
print(escape_str)

# That's a brief overview of strings in Python! They are versatile and widely used for handling text data.