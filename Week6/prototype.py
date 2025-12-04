import random
def get_name():
    while True:
        name = input("Please enter your name:")
        if name.strip() and name.isalpha():
            return name
        else:
            print("Error, invalid input, please enter your name:")
def get_random_number():
    print(random.randint(100000,999999))
    return random.randint
while True:

    user_number_list = {}

    user_number_list[get_random_number] = get_name

    print("\nMenu")
    print("1. enter a new name")
    print("2. view list")
    print("3. Exit")

    choice = int(input("please choose a option:"))

    if choice == 1:
        get_name()
        get_random_number()
    elif choice == 2:
        print(user_number_list)
    elif choice == 3:
        break
    else:
        print("invlaid option please try again.")