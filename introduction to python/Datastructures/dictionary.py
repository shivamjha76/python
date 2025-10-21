''' ------------------------------  Dictionary  ------------------------------ '''

# Dictionary ek data type hai jisme data ko key-value pair ke form me store kiya jata hai.
# Har value ek unique key ke saath store hoti hai.
# Syntax: {key: value}

# Example:
student = {
    "name": "Shivam",
    "age": 18,
    "course": "B.Tech",
    "city": "Jaipur"
}
print("Student Dictionary:", student)

# Kisi value ko access karne ke liye:
print("Name:", student["name"])
print("Course:", student.get("course"))  # safer method

# Dictionary me nayi key-value pair add karna:
student["marks"] = 92
print("After adding marks:", student)

# Kisi value ko update karna:
student["city"] = "Patna"
print("After update:", student)

# Kisi key-value pair ko delete karna:
del student["age"]
print("After deleting age:", student)

# Dictionary me loop lagana:
for key in student:
    print("Key:", key, "| Value:", student[key])

# Ya direct items() se key-value dono ek sath:
for key, value in student.items():
    print(f"{key} → {value}")

# Dictionary ke useful functions:
print("All Keys:", student.keys())
print("All Values:", student.values())
print("All Items:", student.items())

# Dictionary ke andar nested dictionary bhi ho sakti hai:
students = {
    "student1": {"name": "Shivam", "marks": 90},
    "student2": {"name": "Tiya", "marks": 95}
}
print("Nested Dictionary:", students)
print("Tiya ke marks:", students["student2"]["marks"])

# Dictionary ka fayda:
# ✅ Data ko clear aur readable form me store kar sakte ho.
# ✅ Fast searching (keys ke through).
# ✅ Real-world data ko represent karne ke liye best (like name, age, city etc.)

# Empty dictionary banana:
empty_dict = {}
print("Empty Dictionary:", empty_dict)
