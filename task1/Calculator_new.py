# Taking input for the first number and converting it to an integer
Number1 = int(input("Enter the first number: "))

# Taking input for the operator (+, -, *, /, %) to determine the operation
Operator = input("Enter the operator: ")

# Taking input for the second number and converting it to an integer
Number2 = int(input("Enter the second number: "))

# Checking the operator and performing the appropriate operation
if Operator == "+":
    print(Number1 + Number2)  # Addition
elif Operator == "-":
    print(Number1 - Number2)  # Subtraction
elif Operator == "*":
    print(Number1 * Number2)  # Multiplication
elif Operator == "/":
    print(Number1 / Number2)  # Division
elif Operator == "%":
    print(Number1 % Number2)  # Modulus (remainder)
else:
    # If the operator is not valid, an error message is printed
    print("Invalid operation")
