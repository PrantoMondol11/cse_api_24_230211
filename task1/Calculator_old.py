Number1 = int(input("Enter the first number :"))
Operator = input("Enter The Operator:")
Number2 = int(input("Enter the secoond number:"))
if Operator == "+":
    print(Number1 + Number2)
elif Operator == "-":
    print(Number1 - Number2)
elif Operator == "*":
    print(Number1 * Number2)
elif Operator == "/":
    print(Number1 / Number2)
elif Operator == "%": 
    print(Number1 % Number2)
else :
    print("Invalid operation")


