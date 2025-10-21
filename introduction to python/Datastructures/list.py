"""
Lists are used to store multiple items in a single variable.

Syntax:
my_list = [item1, item2, item3, ...]

Lists are:
- Ordered
- Mutable (can be changed)
- Allow duplicate values
"""

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry", "apple"]
print("Original list:", fruits)

# Example 2: Accessing elements
print("\nAccessing elements:")
print(fruits[0])      # First element
print(fruits[-1])     # Last element

# Example 3: Modifying elements
print("\nModifying elements:")
fruits[1] = "blueberry"
print(fruits)

# Example 4: List methods
print("\nList methods:")
fruits.append("orange")         # Add item at end
fruits.insert(1, "kiwi")        # Insert at index
fruits.remove("apple")          # Remove first occurrence
fruits.pop()                    # Remove last item
print(fruits)

# Example 5: Length and membership
print("\nLength and membership:")
print("Length:", len(fruits))
print("cherry" in fruits)       # Check if item exists

# Example 6: Looping through a list
print("\nLooping through list:")
for fruit in fruits:
    print(fruit)

# Example 7: List slicing
print("\nList slicing:")
print(fruits[1:3])              # Elements from index 1 to 2
print(fruits[:2])               # First two elements
print(fruits[-2:])              # Last two elements

# Example 8: Nested lists
print("\nNested lists:")
nested = [["a", "b"], [1, 2]]
print(nested[0][1])             # Access 'b'

# Example 9: List comprehension
print("\nList comprehension:")
squares = [x**2 for x in range(5)]
print(squares)

# Example 10: Sorting and reversing
numbers = [4, 2, 9, 1]
print("\nSorting and reversing:")
numbers.sort()                  # Sort ascending
print("Sorted:", numbers)
numbers.reverse()               # Reverse list
print("Reversed:", numbers)

"""
Summary:
- Lists are versatile and widely used
- Common methods: append, insert, remove, pop, sort, reverse
- Use slicing and loops to access and manipulate data
- List comprehension is a powerful way to create lists
"""

# End of file