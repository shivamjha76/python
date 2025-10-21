''' -----------------------   Bytes and Bytearray   ---------------------------- '''

# Bytes aur Bytearray dono binary data (0 aur 1) ke sath kaam karne ke liye use hote hain.
# Ye mainly image, audio, video, ya network data handle karne me kaam aate hain.

# ---------------------------------
# 🔹 BYTES
# Bytes ek immutable (change na hone wala) sequence hota hai.
# Matlab ek baar bytes object bana liya to uske elements badal nahi sakte.

# Example:
nums = [10, 20, 30, 40]
b = bytes(nums)
print("Bytes Object:", b)
print("First Element:", b[0])   # 10

# b[0] = 99 ❌ (Error — bytes immutable hai)

# ---------------------------------
# 🔹 BYTEARRAY
# Bytearray ek mutable version hai bytes ka.
# Matlab iske elements badle ja sakte hain.

ba = bytearray(nums)
print("\nBytearray Object:", ba)
ba[0] = 99    # allowed
print("After changing first element:", ba)
print("List form:", list(ba))

# ---------------------------------
# 🔹 Important Points

# ✅ Bytes → Immutable (change nahi kar sakte)
# ✅ Bytearray → Mutable (change kar sakte)
# ✅ Dono binary data ke liye use hote hain
# ✅ Values 0–255 ke beech hi honi chahiye

# Example of error (value > 255):
# wrong = bytes([300]) ❌ (Error aayega)

# ---------------------------------
# 🔹 Conversion Example
# Bytearray se bytes me convert karna:
new_b = bytes(ba)
print("\nConverted to bytes:", new_b)

# Bytes se bytearray me convert karna:
new_ba = bytearray(b)
print("Converted to bytearray:", new_ba)
