''' ----------------------------   range()   ---------------------------------- '''

# range() ek built-in function hai jo number sequence (numbers ki series) banata hai.
# Ye mostly loops me use hota hai — especially for loops me.

# Basic Syntax:
# range(start, stop, step)
# start → kaha se start karna hai (default 0)
# stop → kaha tak jana hai (but stop value include nahi hoti)
# step → kitne-kitne gap se number badhega (default 1)

# Example 1: Simple range
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Example 2: start aur stop specify karke
for i in range(2, 8):
    print(i)
# Output: 2 3 4 5 6 7

# Example 3: step value ke sath
for i in range(1, 10, 2):
    print(i)
# Output: 1 3 5 7 9

# Example 4: Reverse counting (negative step)
for i in range(10, 0, -2):
    print(i)
# Output: 10 8 6 4 2

# range() ko list me convert kar sakte ho agar sequence dekhna ho:
nums = list(range(1, 6))
print("List of numbers:", nums)
# Output: [1, 2, 3, 4, 5]

# Summary:
# ✅ range() number sequence banata hai.
# ✅ stop value include nahi hoti.
# ✅ Mostly loops me use hota hai.
# ✅ Memory efficient hota hai (numbers ko ek saath store nahi karta).
