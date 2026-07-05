while True:
    print("\n===================================")
    print("      MATHEMATICAL CALCULATOR")
    print("===================================")
    print("+   : Addition")
    print("-   : Subtraction")
    print("*   : Multiplication")
    print("/   : Division")
    print("^   : Power")
    print("%   : Modulus")
    print("C   : Clear")
    print("OFF : Exit")
    print("===================================")

    choice = input("Enter an operation (+, -, *, /, ^, %, C, OFF): ").upper()

    if choice == "+":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer =", num1 + num2)

    elif choice == "-":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer =", num1 - num2)

    elif choice == "*":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer =", num1 * num2)

    elif choice == "/":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 == 0:
            print("Error! Cannot divide by zero.")
        else:
            print("Answer =", num1 / num2)

    elif choice == "^":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer =", num1 ** num2)

    elif choice == "%":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer =", num1 % num2)

    elif choice == "C":
        print("\n" * 30)
        print("Calculator Cleared!")

    elif choice == "OFF":
        print("Calculator is OFF. Goodbye!")
        break

    else:
        print("Invalid operation! Please try again.")