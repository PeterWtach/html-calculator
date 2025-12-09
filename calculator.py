# Version 3: Added Divide + Bold Green theme
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Divide by zero!"
    return a / b

print("\033[1;92mWelcome to Bold Green Calculator!\033[0m")  # Bold green
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\033[1;92mAdd:\033[0m", add(num1, num2))
print("\033[1;92mSubtract:\033[0m", subtract(num1, num2))
print("\033[1;92mMultiply:\033[0m", multiply(num1, num2))
print("\033[1;92mDivide:\033[0m", divide(num1, num2))