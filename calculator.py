# Version 2: Added Multiply + Red theme
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

print("\033[91mWelcome to Red Calculator!\033[0m")  # Red text
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\033[91mAdd:\033[0m", add(num1, num2))
print("\033[91mSubtract:\033[0m", subtract(num1, num2))
print("\033[91mMultiply:\033[0m", multiply(num1, num2))