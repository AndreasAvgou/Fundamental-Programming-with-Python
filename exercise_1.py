# Exercise 1: Basic Operations
print("--- Lab Exercise 1 ---")

# 1. Read two integers from the keyboard
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# 2. Calculate and display results 
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

# 3. Check for division by zero before dividing 
if num2 != 0:
    print(f"Quotient: {num1 / num2:.2f}")
else:
    print("Division by zero is not allowed.")