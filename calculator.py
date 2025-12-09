# Version 1: Basic Add/Subtract Calculator (Blue theme simulation)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("\033[94mWelcome to Blue Calculator!\033[0m")  # Blue text
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\033[94mAdd:\033[0m", add(num1, num2))
print("\033[94mSubtract:\033[0m", subtract(num1, num2))