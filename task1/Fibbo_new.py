# Number of Fibonacci terms to generate
n = 4

# Initializing the first two numbers in the sequence
a = 0
b = 1

# Printing the first two numbers
print(a)  # 0
print(b)  # 1

# Loop to calculate and print the remaining numbers in the sequence
for i in range(2, n):
    c = a + b  # Calculate the next number in the sequence
    a = b      # Move the second number to the first
    b = c      # Update the second number to the new calculated value
    print(c)   # Print the next number in the sequence
