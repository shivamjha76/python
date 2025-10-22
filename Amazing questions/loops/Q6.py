 # Print this pattern using nested for loop
'''
*
* *
* * *
* * * *
* * * * *
'''

for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

# Ab esi pattern ko reverse pattern print karo

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

