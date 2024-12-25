#python 2.7.15

print "Hello, Dcoder!"def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input
    try:
        operation = int(input("Enter the number of the operation (1/2/3/4): "))
        if operation not in [1, 2, 3, 4]:
            print("Invalid operation. Please try again.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the operation
        if operation == 1:
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the calculator
calculator()