def add(num1, num2):
    return num1 + num2  # No need for int()

def subtract(num1, num2):
    return num1 - num2  # No need for int()

def multiply(num1, num2):
    return num1 * num2  # No need for int()

def divide(num1, num2):
    return num1 / num2  # Automatically returns float if needed

# Using different variable names
addition = add(2, 3)
difference = subtract(2, 3)
product = multiply(2, 3)
quotient = divide(2, 3)  # Changed variable name

print(addition, difference, product, quotient)
