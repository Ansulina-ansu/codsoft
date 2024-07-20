def calculator():
    print("Welcome to the simple calculator!")

    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        operation_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        operation_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        operation_symbol = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_symbol = '/'
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    print(f"{num1} {operation_symbol} {num2} = {result}")

# Run the calculator function
calculator()