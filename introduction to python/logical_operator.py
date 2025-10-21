"""
Logical operators are used to combine conditional statements and control flow.

Operators:
1. and     → Returns True if both statements are True
2. or      → Returns True if at least one statement is True
3. not     → Reverses the result, returns False if the result is True

Basic Usage:
"""

# Example 1: and operator
x = 10
y = 20
print("and operator:")
print(x > 5 and y > 15)  # True
print(x > 15 and y > 15) # False

# Example 2: or operator
print("\nor operator:")
print(x > 5 or y > 25)   # True
print(x > 15 or y > 25)  # False

# Example 3: not operator
print("\nnot operator:")
print(not(x > 5))        # False
print(not(x > 15))       # True

"""
Boolean Values:
Logical operators also work directly with boolean values.
"""

a = True
b = False
print("\nBoolean logic:")
print(a and b)           # False
print(a or b)            # True
print(not a)             # False

"""
Summary:
- Use 'and' when all conditions must be True
- Use 'or' when at least one condition must be True
- Use 'not' to invert a condition
- Logical operators can work with any data type, not just booleans
"""

# End of file