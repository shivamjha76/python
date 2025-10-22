# Print this triangle pattern using nested loops
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

for i in range(1,6):
    print(" " * (5 -i), end="")
    print("* " * i)


# now print it in reverse order

for i in range(5,0,-1):
    print(" "* (5 - i), end="")
    print("* " * i)