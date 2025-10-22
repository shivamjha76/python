''' -------------------------------  Loops  ----------------------------------------- '''

# Loops ka use tab hota hai jab hume ek hi code baar-baar chalana ho.
# Python me mainly 2 types ke loops hote hain:
# 1️⃣ for loop
# 2️⃣ while loop

# ---------------------------------
# 🔹 FOR LOOP
# Jab hume ek sequence (list, tuple, string, range, etc.) ke elements par iterate karna ho.

# Example 1: List ke sath
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

# Example 2: range() ke sath
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Example 3: start, stop, step ke sath
for i in range(2, 10, 2):
    print(i)
# Output: 2 4 6 8

# ---------------------------------
# 🔹 WHILE LOOP
# Jab tak condition True hai tab tak loop chalta rahega.

# Example:
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # har bar +1

# ---------------------------------
# 🔹 LOOP CONTROL STATEMENTS

# 1️⃣ break → loop ko turant rok deta hai
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# Output: 1 2 3 4

# 2️⃣ continue → current iteration skip karke next par chala jata hai
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5

# 3️⃣ else with loop → jab loop normally complete ho jata hai (break se nahi), tab else part chalta hai
for i in range(1, 4):
    print(i)
else:
    print("Loop completed successfully!")

# ---------------------------------
# 🔹 NESTED LOOP
# Ek loop ke andar dusra loop

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# ---------------------------------
# 🔹 Summary
# ✅ for loop → sequence ke sath use hota hai
# ✅ while loop → condition-based loop
# ✅ break → loop rokta hai
# ✅ continue → skip karta hai
# ✅ else → tab chalta hai jab loop normally finish hota hai
# ✅ nested loop → loop ke andar loop
