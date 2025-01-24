def calculator():
    print("Welcome to the Simple Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        # Take user input for operation
        operation = int(input("Enter the number corresponding to the operation (1/2/3/4): "))

        # Validate operation
        if operation not in [1, 2, 3, 4]:
            print("Invalid selection. Please choose a valid operation.")
            return

        # Take user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
       


        # Perform the selected operation
        if operation == 1:
            result = num1 + num2 
            print(f"The result of addition is: {result}")
        elif operation == 2:
            result = num1 - num2 
            print(f"The result of subtraction is: {result}")
        elif operation == 3:
            result = num1 * num2 
            print(f"The result of multiplication is: {result}")
        elif operation == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()