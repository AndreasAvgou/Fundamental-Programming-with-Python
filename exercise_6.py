# Exercise 6: Functions and List Manipulation
print("\n--- Lab Exercise 6 ---")

# Function 1: Find the maximum value in a list 
def find_max(numbers):
    """Returns the largest number in the list."""
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Function 2: Reverse the list 
def reverse_list(numbers):
    """Returns a new list with elements in reverse order."""
    reversed_lst = []
    # Loop backwards from the last index to 0
    for i in range(len(numbers) - 1, -1, -1):
        reversed_lst.append(numbers[i])
    return reversed_lst

# Function 3: Count even numbers 
def count_even(numbers):
    """Returns the count of even numbers in the list."""
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# Main Program 
# 1. Read a list of space-separated integers
input_str = input("Enter numbers separated by space: ")

if input_str.strip():
    # Convert string input to a list of integers
    numbers_list = [int(x) for x in input_str.split()]

    # 2. Call functions and display results
    print(f"Max number: {find_max(numbers_list)}")
    print(f"Reversed list: {reverse_list(numbers_list)}")
    print(f"Count of even numbers: {count_even(numbers_list)}")
else:
    print("No numbers were entered.")