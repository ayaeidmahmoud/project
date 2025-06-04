print("Hello World! shahd branch")

#sum function
def add(a, b):
    return a + b

a = float(input("number1: "))
b = float(input("number2: "))
result = add(a, b)
print(f"The result of the sum is: {result}")
def sum(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2
def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2
def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2
def divide(num1, num2):
    """Returns the quotient of two numbers."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def power(base, exponent):
    """Returns the base raised to the power of exponent."""
    return base ** exponent 
def modulus(num1, num2):
    """Returns the remainder of the division of two numbers."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 % num2

print("hello world")
