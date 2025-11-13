#code to determine if a person should be paying taxes
def get_binary_input(prompt):
    while True:
        try:
            responce = int(input(prompt))
            if responce in [1, 0]:
                return responce
            else:
                print("This is an invalid input, please enter only 1 or 0")
        except ValueError:
            print("This is an invalid input, please input only 1 or 0.")

while True:
    working = get_binary_input("Do you have a job? insert 1 for yes and 0 for no:")
    if working == 0:
        print("You do not have to pay taxes!")
        break
    else:
        I9 = get_binary_input("Do you have to file a I-9? Input 0 for no and 1 for yes: ")
        if I9 == 0:
            print("You do not have to pay taxes!")
            break
        else:
            exemption = get_binary_input("Do you have a tax exemption on your I-9? Input 0 for no and 1 for yes: ")
            if exemption == 0:
                print("You must pay taxes.")
                break
            else:
                print("You do not have to pay taxes!")
                break