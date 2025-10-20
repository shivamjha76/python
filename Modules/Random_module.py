# --------------------- Random module in python --------------------- #
# The random module is a built-in Python library that introduces randomness into your programs. It’s widely used in simulations, games, testing, data sampling, and machine learning tasks.

import random

# Key functions in random module.
random.random()  # Returns a float between 0.0 and 1.0
random.randint(10,30) # Returns a random integer between a and b (inclusive [yani a aur b dono ko le karke])
random.randrange(10,20) # Returns a random integer from range a to b (exclusive of b [yani b ko chorna hai])
print(random.uniform(10,25)) # Returns a random float between a and b.


# ----------- chosing form any sequences [ we use randam.choice() function] ------------------- #
# example
# Let's make a set to understand it.
number = (10, 20, 30, 40,50)
random.choice(number)

# ---------------------------------------------------------------------------------------------- #
# random.choices(seq, k) function
# This function is used to pick multiple random elements from a sequence.
# here seq = list, tuple, or string
# k = number of items you want to pick.
# ------------ Example 1: List ------------- #
colors = ["red", "yellow", "blue", "green"]
random.choices(colors, k=2)
# ---------- Example 2:string ------------- #
letters = "Hello"
random.choices(letters, k=3)
# -------------------------------------------------------------------------------------------------------- #

# random.sample(seq, k) function
# ye bhi random item choose karta hai lekin bina kisi repetition ke 
# Examples
color = ["red", "pink", "green", "yellow"]
random.sample(color, k=2)
# --------------------------------------------------- #

# ----------------------- random.suffle(seq) function ----------------------------
# eska use kisi sequence ke elements ko random order me reaggrage karne ke liye kiya jata hai.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
random.shuffle(num)
# print(num)
# --------------------------------------------------------------------------------------------------------- #