# Data Types in Python 

# What are Data Types?
# Data types are categories that define what kind of value a variable holds. They determine how the data can be used and what operations can be performed on it.

# Common Data Types in Python:
# 1. Integers: Whole numbers (e.g., 1, 2, 3)
# 2. Floats: Decimal numbers (e.g., 1.5, 2.75)
# 3. Strings: Text (e.g., "Hello", "Python")
# 4. Booleans: True or False values

# How to Check Data Types?
# You can use the type() function to check the data type of a variable or value.
# Example:
num = 10
print(type(num))  # Output: <class 'int'>
pi = 3.14
print(type(pi))   # Output: <class 'float'>
name = "Shivam"
print(type(name)) # Output: <class 'str'>
is_student = True
print(type(is_student)) # Output: <class 'bool'>

# Converting Data Types:
# You can convert between data types using built-in functions:
# int(): Converts to integer
# float(): Converts to float
# str(): Converts to string

# Example:
num_str = "100"
num_int = int(num_str)      # Converts string to integer
print(type(num_int))        # Output: <class 'int'>
num_float = float(num_int)  # Converts integer to float
print(type(num_float))      # Output: <class 'float'>
name_str = str(num_int)     # Converts integer to string
print(type(name_str))       # Output: <class 'str'>

# That's a brief overview of data types in Python! They help you manage and manipulate data effectively in your programs.

