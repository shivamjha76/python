"""
Conditional statements allow decision-making in code based on certain conditions.

Syntax:
if condition:
    # code block if condition is True
elif another_condition:
    # code block if another_condition is True
else:
    # code block if none of the above conditions are True
"""

# Example 1: Basic if condition
age = 20
print("Basic if condition:")
if age >= 18:
    print("You are eligible to vote.")

# Example 2: if-else condition
print("\nif-else condition:")
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Example 3: if-elif-else ladder
marks = 85
print("\nif-elif-else ladder:")
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

"""
Nested if:
You can place one if inside another if block.
"""

print("\nNested if:")
num = 15
if num > 0:
    print("Number is positive")
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is not positive")

"""
Using logical operators with if-else:
"""

print("\nLogical operators with if-else:")
temperature = 30
humidity = 70

if temperature > 25 and humidity > 60:
    print("It's hot and humid.")
elif temperature > 25 or humidity > 60:
    print("It's either hot or humid.")
else:
    print("Weather is pleasant.")

"""
Edge Cases:
- Conditions can be based on any expression that returns True or False
- You can use input() to take user input and apply conditions
"""

print("\nEdge case with user input:")
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Invalid input")

"""
Summary:
- Use if to check a condition
- Use elif for multiple conditions
- Use else for fallback/default case
- Conditions can be combined using logical operators
- Nesting is allowed but should be used carefully for readability
"""

# End of file