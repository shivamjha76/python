# -------------------------- math module in python --------------------------------- #

# This math module is part of python's standard libarary and offers funcitons for performing mathematical operations.

import math

# -------------------------------basic arithmetic  ----------------------- #
math.sqrt(9)            # use for square root of x
math.pow(2,3)           # 2 raised to the power of 3
math.fabs(-4)           # (use of convert into +ve)
math.ceil(2.4)          # round up to  the nearest integer
math.floor(2.8)         # Round down to the nearest intergermath.trunc(46.99) # Truncates decimal parts

# ------------------ Trigonometry ---------------------------- #
math.sin(1)
math.cos(3) 
math.tan(0) 

# --------------------- inverse trigonometry ----------------- #
math.asin(1) 
math.acos(1) 
math.atan(1) 

math.degrees(180)         # converts radians to  degrees
math.radians(45)          # Converts degrees to radian

# ------------------- Logarithmic & Exponential -------------- #
math.exp(2)               # Returns e^2
math.log(10)              # Natural logarithm
math.log10(1000)          # Base 10 logarithm

# ------------------------ combinatories --------  ----------- #
math.factorial(5)         # Factorial of x 
# Note factorial  means like 5! then it will be 5 x 4 x 3 x 2 x 1 = 120

math.comb(5,2)            # Combinations
# Note first number should be greater than second

math.perm(5,2) # perutations

# ------------------------- Constants ---------------------- #
math.pi                 # π (3.14159....)
math.e                  # Euler's number (2.711828...)
math.tau                # τ (2π)
math.inf                # infinity
math.nan                # Not a number

# Limitations 
    # Only works with real  numbers. for complex numbers, use the cmath module.
    # Doesn't support symbolic math (use sympy for that)

# Where it is used
    # physics simulations
    # statistical analysis
    # Engineering calculations
    # Financial modeling
    # Geometry and graphics