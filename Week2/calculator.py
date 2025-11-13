while True:
    valid_operation = "+, -, /, //, *, %, exit"
    while True:
        operation = input(("Please enter operation (+, -, /, *, //, %) or exit to quit:"))
        if operation in valid_operation:
            break
        else:
            print("please enter a valid operation.")

    if operation == "exit":
        break

    while True:
        try:    
            num1 = float(input("Enter first number:"))
        except ValueError:
            print("Please enter valid number")
        else: break
    while True:
        try:
            num2 = float(input("Enter second number:"))
        except ValueError:
            print("Please enter valid number")
        else: break

    if operation == "/":
        while num2 == 0:
            print("Invalid input, cannot divide by 0")
            num2 = float(input("Enter second number:"))
        print(num1/num2)
    if operation == "+":
        print(num1+num2)
    if operation == "-":
        print(num1-num2)
    if operation == "*":
        print(num1*num2)
    if operation == "//":
        print(num1//num2)
    if operation == "%":
        print(num1%num2)

