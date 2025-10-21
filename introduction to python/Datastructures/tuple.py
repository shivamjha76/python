''' ----------------------------    Tuple  --------------------------- '''

# Tuple ek ordered aur immutable (change na hone wala) data type hai.
# Matlab, tuple me elements ka order fix hota hai aur ek baar create hone ke baad usme kuch change nahi kar sakte.
# Tuple ko parentheses () ke andar likha jata hai.

# Example:
my_tuple = (10, 20, 30, 40)
print("My Tuple:", my_tuple)

# Tuple ke elements ko index ke through access karte hain:
print("First Element:", my_tuple[0])

# Tuple me elements ko change nahi kar sakte:
# my_tuple[1] = 50   ❌ (Ye error dega)

# Agar ek hi element ka tuple banana ho to uske baad comma lagana zaroori hai:
single_tuple = (5,)
print("Single Element Tuple:", single_tuple)

# Tuple ke andar alag-alag data types rakh sakte ho:
mixed_tuple = (10, "Hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# Tuple ke andar dusra tuple bhi ho sakta hai (Nested Tuple):
nested_tuple = (1, 2, (3, 4))
print("Nested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[2][1])  # 4

# Tuple ke kuch common functions:
print("Length of tuple:", len(my_tuple))
print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))

# Tuple se loop lagakar elements print karna:
for item in my_tuple:
    print("Item:", item)

# Tuple ko list me convert karna (agar modify karna ho to):
temp_list = list(my_tuple)
temp_list.append(50)
my_tuple = tuple(temp_list)
print("Modified Tuple:", my_tuple)

# Tuple ka fayda:
# ✅ Fast execution (list se faster)
# ✅ Memory efficient
# ✅ Fixed data ke liye perfect (jisme change nahi chahiye)
