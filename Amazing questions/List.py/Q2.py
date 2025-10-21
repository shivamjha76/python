'''
Ek list banao jisme tumhare 3 favourite fruits aur ek aur list ho jisme 3 favourite vegetables ho (nested list).
Fir pura list print karo
'''

items = ["Guava", "Orange", "Pineapple", ["Patato", "Tomato", "Bringle"]]
# print(items) 

'''
Usi items list me se:
First fruit print karo
Second vegetable print karo
'''

print(items[0])
# print(items[3][1])

'''
items list me ek naya fruit add karo using append() method.
Fir updated list print karo
'''
items.append("Apple")
# print(items)

'''
items list me “Mango” ko second position (index 1) pe add karo using insert() method.
Fir updated list print karo.
'''

items.insert(1, "Mango")
# print(items)

'''
Ek list banao: more_fruits = ["Papaya", "Kiwi"]
items list me ye fruits add karo using extend() method
Fir updated items print karo
'''
more_fruits = ["Papaya", "Kiwi"]
items.extend(more_fruits)
# print(items)

'''
items list me se “Apple” remove karo using remove() method
Fir updated list print karo
'''

items.remove("Apple")
print(items)
