# Print all numbers from 1 to 15 except 7 and 11 using a for loop

for i in  range(1,16):
    if i == 7 or i == 11:
        continue
    print(i)