# -------------------------- Modules in python ---------------------------------------- #

# Module
     # Modules Python me toolboxes ki tarah hote hain.
     # Ye aise files hote hain jisme extra tools (functions, classes, variables) hote hain
     # jo tum apne programs me use kar sakte ho.
     # Basically, modules pre-made instructions ka set hote hain jo kaam ko easy bana dete hain.

# Example:
# Agar tumhe dates aur times ke sath kaam karna hai, to tum 'datetime' module use kar sakte ho.
# Ye module functions aur classes provide karta hai jaise:
import datetime

# Current date aur time nikalne ke liye:
current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)


# Why Use Modules?
      # 1. Code reuse karne ke liye: Ek baar code likho aur baar-baar use karo.
      # 2. Code organize karne ke liye:
      # Related code ek file me rakhne se organize rahta hai.
      # 3. Dusre logon ka code use karne ke liye:
      # Python me built-in aur third-party modules hote hain jo kaafi useful hote hain.


# Types of Modules
# Python me modules 3 types ke hote hain:

# 1. Built-in Modules:
    # Ye Python ke sath pre-installed hote hain.
    # Examples: math, datetime, random

import math
print("Square root of 16:", math.sqrt(16))

# 2. Third-Party Modules:
     # Ye modules Python ke bahar ke developers ne banaye hote hain.
     # Inhe use karne ke liye install karna padta hai pip se.
     # Examples: requests (HTTP requests), NumPy (numerical computations)

# Example install command:
# pip install requests

# 3. Custom Modules:
      # Ye modules tum khud create kar sakte ho.
      # Functions, classes, aur variables define karke ek reusable module bana sakte ho.
# Example:
  # Tum ek file banao: mymodule.py
  # Aur usme function define karo:
'''
def greet(name):
    return f"Hello {name}"
#   Fir use kar sakte ho:

from mymodule import greet
print(greet("Shivam"))

'''
