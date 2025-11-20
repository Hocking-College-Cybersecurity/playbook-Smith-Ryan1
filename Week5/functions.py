while True:
    fun1 = float(input("Enter your height in meters:"))
    if fun1 <= 1.5:
        print("you are shorter than 5 feet!")
        if fun1 > 1.5:
            print("you are taller than 5 feet!")
        if fun1 < 0 or fun1 > 2:
            print("Invalid input, or computation cannot be calculated")
            raise ValueError

    fun2 = int(input("Please enter your weight rounded to the nearest Kilogram:"))
    if fun2 < 130 or fun2 > 50:
        print("thank you.")
    else:
        print("cannot compute value")
        raise ValueError

    result = fun2 / fun1**2

    fun3 = print("Your body mass index is", result)
    
