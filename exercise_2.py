# Exercise 2: Advanced Conditionals
print("\n--- Lab Exercise 2 ---")

# Read two integers
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

# Case: Both numbers are positive
if a > 0 and b > 0:
    print("Both numbers are positive.")
    total = a + b
    
    # Check if sum is greater than 100 
    if total > 100:
        print(f"Large sum: {total}")
    
    # Check if the sum is even or odd 
    if total % 2 == 0:
        print(f"The sum {total} is even.")
    else:
        print(f"The sum {total} is odd.")

# Case: Both numbers are zero 
elif a == 0 and b == 0:
    print("Both numbers are zero.")

# Case: One is zero and the other is positive 
elif (a == 0 and b > 0) or (b == 0 and a > 0):
    print("One is zero and the other is positive.")

# Case: At least one number is negative
else:
    if a < 0 and b < 0:
        # If both are negative, display their difference 
        print(f"Difference: {a - b}")
    else:
        # If only one is negative, display their product 
        print(f"Product: {a * b}")