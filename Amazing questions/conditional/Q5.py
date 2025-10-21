'''
Write a Python program that takes a number from the user and checks:

If it is divisible by both 3 and 5, print "FizzBuzz"
If it is only divisible by 3, print "Fizz"
If it is only divisible by 5, print "Buzz"
Otherwise, print "Not divisible by 3 or 5"
'''

num = int(input("enter a number: "))

if (num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Number is not divisible by 3 and 5")