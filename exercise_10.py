# Christmas Tree Generator
def print_christmas_tree():
    """
    Reads an integer height N from the user and prints a Christmas tree pattern.
    - Top: '+'
    - Body: Starts/Ends with '0', filled with '*'
    - Bottom: Trunk '|'
    """
    try:
        # Get user input
        height = int(input("Enter tree height (N): "))
        
        if height < 2:
            print("Height must be at least 2 to form a proper tree.")
            return

        # Calculate the maximum width of the tree at the bottom row (N-1)
        # The formula for the width of the row is: 2 * row_index + 1
        # For the last row (index = height - 1), width = 2 * (height - 1) + 1
        # However, since we add '0' borders, the logic for stars inside is (2*i - 1).
        # Total width of the widest part = 1 ('0') + stars + 1 ('0').
        # Widest stars count at row i = N-1 is: 2*(N-1) - 1.
        # Total max width = 2 + (2 * height - 3) = 2 * height - 1.
        max_width = (2 * height) - 1

        # 1. Print the Top Star
        print("+".center(max_width))

        # 2. Print the Body (from row 1 to N-1)
        for i in range(1, height):
            # Calculate number of stars between the '0's
            # Pattern goes: 1, 3, 5... which is (2 * i) - 1
            num_stars = (2 * i) - 1
            
            # Construct the row string
            row_str = f"0{'*' * num_stars}0"
            
            # Print centered
            print(row_str.center(max_width))

        # 3. Print the Trunk
        print("|".center(max_width))

    except ValueError:
        print("[Error] Please enter a valid integer.")

if __name__ == "__main__":
    print_christmas_tree()