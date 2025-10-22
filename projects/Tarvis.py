known_user = ["Shivam", "Rohit", "Priyanshu", "Ashish", "Aditya", "Abhishek", "Ganesh", "MRohit"]

while True:
    print("Hi! my name is Tarvis")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_user:
        print("Name reconiged")
    else:
        print("Name is not reconised")
        