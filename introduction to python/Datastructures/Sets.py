''' ----------------------------   Sets   ------------------------------- '''

# Set ek unordered aur unique elements ka collection hota hai.
# Matlab, set me duplicate values automatically remove ho jati hain.
# Set ko curly braces {} ke andar likhte hain.

# Example:
numbers = {10, 20, 30, 40, 20}
print("Set:", numbers)  # Duplicate 20 sirf ek baar ayega

# Empty set banana ho to {} use mat karna (wo dictionary ban jata hai),
# uske liye set() function use karo:
empty_set = set()
print("Empty Set:", empty_set)

# Set me element add karne ke liye:
numbers.add(50)
print("After adding 50:", numbers)

# Multiple elements ek sath add karne ke liye:
numbers.update([60, 70, 80])
print("After adding multiple elements:", numbers)

# Set se element remove karne ke liye:
numbers.remove(40)  # Agar element na mila to error dega
print("After removing 40:", numbers)

# Safe tarike se remove karne ke liye:
numbers.discard(100)  # Agar element na ho to error nahi aata
print("After discard:", numbers)

# Set operations (Maths jaisa):
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A.union(B))          # {1, 2, 3, 4, 5, 6}
print("Intersection:", A.intersection(B))  # {3, 4}
print("Difference (A-B):", A.difference(B))  # {1, 2}

# Set ka fayda:
# ✅ Duplicate data automatically remove karta hai.
# ✅ Fast membership checking (like if x in set).
# ✅ Useful for mathematical operations.

# Note:
# ❌ Set me indexing ya slicing possible nahi hai (kyunki unordered hota hai)
