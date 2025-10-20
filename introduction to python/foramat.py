# Let's learn about format() function in python.
# 🧩 What is format()
# The format() method in Python is used to create formatted strings by embedding variables or values into placeholders defined by curly braces {}.

# Positional formatting
name = "Shivam"
age = 19
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is shivam and I am 19 years old.

# index-based fomatting
print("My name is {0} and I am {1} years old.".format("shivam", 19))
# Output: My name is Bob and I am 25 years old.

# Keyboard formatting
print("For only {price:.2f} dollars!".format(price=49))
# Output: For only 49.00 dollars!

# Thousands seperators
print("{:,}".format(10000))  # Output: 10,000

