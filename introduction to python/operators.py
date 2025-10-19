# -------------------- operators in python -------------------- #

a = 10
b = 3
# Arithmetic Operators
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.3333
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponentiation:", a ** b)   # 1000
# Comparison Operators
print("Equal:", a == b)            # False
print("Not Equal:", a != b)        # True
print("Greater Than:", a > b)      # True
print("Less Than:", a < b)         # False
print("Greater Than or Equal To:", a >= b)  # True
print("Less Than or Equal To:", a <= b)     # False

# Logical Operators
x = True
y = False
print("Logical AND:", x and y)     # False
print("Logical OR:", x or y)       # True
print("Logical NOT:", not x)       # False
# Bitwise Operators
print("Bitwise AND:", a & b)       # 2
print("Bitwise OR:", a | b)        # 11
print("Bitwise XOR:", a ^ b)       # 9
print("Bitwise NOT:", ~a)          # -11
print("Left Shift:", a << 1)       # 20
print("Right Shift:", a >> 1)      # 5

# Assignment Operators
c = a
c += b
print("Assignment += :", c)        # 13
c -= b
print("Assignment -= :", c)        # 10
c *= b
print("Assignment *= :", c)        # 30
c /= b
print("Assignment /= :", c)        # 10.0
c %= b
print("Assignment %= :", c)        # 1.0
c **= b
print("Assignment **= :", c)       # 1.0
c //= b
print("Assignment //= :", c)       # 0.0

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Membership 'in':", 3 in my_list)      # True
print("Membership 'not in':", 6 not in my_list)  # True

# Identity Operators
d = a
print("Identity 'is':", a is d)              # True
e = 10
print("Identity 'is not':", a is not e)      # False

# Ternary Operator
max_value = a if a > b else b
print("Ternary Operator (max value):", max_value)  # 10

# Operator Precedence
result = a + b * 2
print("Operator Precedence (a + b * 2):", result)  # 16

# Using parentheses to change precedence
result = (a + b) * 2
print("Using Parentheses ((a + b) * 2):", result)  # 26

# Chained Comparison
is_between = 5 < a < 15
print("Chained Comparison (5 < a < 15):", is_between)  # True

# Augmented Assignment with Bitwise Operators
f = 5  # binary: 0101
f &= 3  # binary: 0011
print("Augmented Assignment Bitwise AND (f &= 3):", f)  # 1 (binary: 0001)
f |= 2  # binary: 0010
print("Augmented Assignment Bitwise OR (f |= 2):", f)   # 3 (binary: 0011)
f ^= 1  # binary: 0001
print("Augmented Assignment Bitwise XOR (f ^= 1):", f)  # 2 (binary: 0010)

# Complex Number Arithmetic
c1 = 2 + 3j
c2 = 1 + 4j
c_sum = c1 + c2
print("Complex Number Addition:", c_sum)  # (3+7j)
c_product = c1 * c2
print("Complex Number Multiplication:", c_product)  # (-10+11j)

# Floor Division with Negative Numbers
neg_a = -10
neg_b = 3
floor_div = neg_a // neg_b
print("Floor Division with Negative Numbers (-10 // 3):", floor_div)  # -4

# Modulus with Negative Numbers
mod_neg = neg_a % neg_b
print("Modulus with Negative Numbers (-10 % 3):", mod_neg)  # 2

# Exponentiation with Negative Exponent
exp_neg = a ** -b
print("Exponentiation with Negative Exponent (10 ** -3):", exp_neg)  # 0.001

# Chained Assignment
g = h = i = 5
print("Chained Assignment (g, h, i):", g, h, i)  # 5 5 5

# Using Operators with Different Data Types
str1 = "Hello"
str2 = "World"
concat_str = str1 + " " + str2
print("String Concatenation:", concat_str)  # Hello World
repeat_str = str1 * 3
print("String Repetition:", repeat_str)  # HelloHelloHello

# List Operators
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("List Concatenation:", combined_list)  # [1, 2,
# 3, 4, 5, 6]
repeated_list = list1 * 2
print("List Repetition:", repeated_list)  # [1, 2, 3, 1, 2, 3]

# Tuple Operators
tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2
print("Tuple Concatenation:", combined_tuple)  # (1, 2, 3, 4)
repeated_tuple = tuple1 * 3
print("Tuple Repetition:", repeated_tuple)  # (1, 2, 1, 2, 1, 2)

# Dictionary Membership
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary Membership 'in':", 'b' in my_dict)  # True
print("Dictionary Membership 'not in':", 'd' not in my_dict)  # True

# Set Operators
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Set Union:", union_set)  # {1, 2, 3, 4, 5}
intersection_set = set1 & set2
print("Set Intersection:", intersection_set)  # {3}
difference_set = set1 - set2
print("Set Difference:", difference_set)  # {1, 2}
symmetric_difference_set = set1 ^ set2
print("Set Symmetric Difference:", symmetric_difference_set)  # {1, 2, 4, 5}

# Frozenset Operators
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
frozenset_union = frozenset1 | frozenset2
print("Frozenset Union:", frozenset_union)  # frozenset({1, 2, 3, 4, 5})
frozenset_intersection = frozenset1 & frozenset2
print("Frozenset Intersection:", frozenset_intersection)  # frozenset({3})
frozenset_difference = frozenset1 - frozenset2
print("Frozenset Difference:", frozenset_difference)  # frozenset({1, 2})
frozenset_symmetric_difference = frozenset1 ^ frozenset2
print("Frozenset Symmetric Difference:", frozenset_symmetric_difference)  # frozenset({1, 2, 4, 5})

# Bytes and Bytearray Operators
bytes1 = bytes([65, 66, 67])
bytes2 = bytes([68, 69, 70])
combined_bytes = bytes1 + bytes2
print("Bytes Concatenation:", combined_bytes)  # b'ABCDEF'
bytearray1 = bytearray([65, 66, 67])
bytearray2 = bytearray([68, 69, 70])
combined_bytearray = bytearray1 + bytearray2
print("Bytearray Concatenation:", combined_bytearray)  # bytearray(b'ABCDEF')

# Memory View Operators
byte_array = bytearray(b'Hello')
mem_view = memoryview(byte_array)
print("Memory View Slice:", mem_view[1:4].tobytes())  # b'ell'

# Unary Operators
num = 5
print("Unary Plus:", +num)          # 5
print("Unary Minus:", -num)         # -5
print("Bitwise NOT:", ~num)         # -6
print("Logical NOT:", not num)       # False

# Identity Operators with Mutable and Immutable Types
list_a = [1, 2, 3]
list_b = list_a
print("Identity 'is' with Lists:", list_a is list_b)  # True
list_b.append(4)
print("List after modifying list_b:", list_a)  # [1, 2, 3, 4]
str_a = "hello"
str_b = "hello"
print("Identity 'is' with Strings:", str_a is str_b)  # True
str_b += "!"
print("String after modifying str_b:", str_a)  # hello

# Ternary Operator with Different Data Types
result_str = "Even" if a % 2 == 0 else "Odd"
print("Ternary Operator Result (Even/Odd):", result_str)  # Even
result_list = [1, 2, 3] if b > 2 else [4, 5, 6]
print("Ternary Operator Result (List):", result_list)  # [4, 5, 6]


# --------------------- End of operators --------------------- #