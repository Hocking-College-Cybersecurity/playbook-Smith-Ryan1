while True:
    operation = input(("Please enter operation (+, -, /, *, //, %) or exit to quit:"))

    if operation == "exit":
        break

    num1 = float(input("Enter first number:"))

    num2 = float(input("Enter second number:"))

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
