def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

def perform_operation(n1, n2, operation):
    if operation == '1':
        return add(n1, n2)
    elif operation == '2':
        return subtract(n1, n2)
    elif operation == '3':
        return multiply(n1, n2)
    elif operation == '4':
        return divide(n1, n2)
    else:
        return "Invalid operation choice."

# Loop to allow multiple operations
while True:
    # Get user input
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    # Display operation choices
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Perform the calculation using functions
    result = perform_operation(n1, n2, choice)

    # Display the result
    print(f"\nResult: {result}")

    # Ask user if they want to continue
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() != 'yes':
        break  # Exit the loop if user doesn't want to continue
