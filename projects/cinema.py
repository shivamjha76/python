films = {
    "Finding": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5],
}

while True:
    choise = input("What film whould you like to watch: ").strip().title()
    if choise in films:
        age = int(input("How old are you?: "))

        # check user age
        if age >= films[choise][0]:
            # check enough seats
            if films[choise][1] > 0:
             print("enjoy the film!")
             films[choise][1] = films[choise][1] - 1
            else:
                print("seats are full")
        else:
            print("you are too young to watch th film.")
        pass
    else:
        print("we don't have that film!")
