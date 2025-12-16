# Exercise 9: Meal Planner (Recursion)
print("--- Lab Exercise 9: Recursive Meal Planner ---")

def solve_meal_plan(times, available_time, n):
    """
    Recursive function to find the maximum number of dishes 
    that can be prepared within the available time.
    
    Args:
        times (list): List of preparation times for the dishes.
        available_time (int): Remaining time.
        n (int): Index of the current dish being considered (working backwards).
        
    Returns:
        int: Maximum number of dishes.
    """
    # Base Case: No dishes left or no time left
    if n == 0 or available_time == 0:
        return 0

    # Get time of the current dish (n-1 because lists are 0-indexed)
    current_dish_time = times[n-1]

    # If current dish takes more time than available, we cannot include it.
    # We move to the next dish (n-1).
    if current_dish_time > available_time:
        return solve_meal_plan(times, available_time, n-1)
    
    else:
        # Two options:
        # 1. Include the dish: Add 1 to count, subtract its time, check remaining dishes.
        include = 1 + solve_meal_plan(times, available_time - current_dish_time, n-1)
        
        # 2. Exclude the dish: Count doesn't change, time doesn't change, check remaining dishes.
        exclude = solve_meal_plan(times, available_time, n-1)
        
        # Return the maximum of the two options
        return max(include, exclude)

def main():
    try:
        # 1. Read number of dishes
        num_dishes = int(input("Enter number of dishes: "))
        
        dish_names = []
        dish_times = []
        
        # 2. Read details for each dish
        for i in range(num_dishes):
            name = input(f"Name of dish {i+1}: ")
            time = int(input(f"Preparation time (min): "))
            dish_names.append(name)
            dish_times.append(time)
            
        # 3. Read total available time
        total_time = int(input("Enter total available time (min): "))
        
        # 4. Call recursive function
        max_dishes = solve_meal_plan(dish_times, total_time, num_dishes)
        
        # 5. Output result
        print(f"\nMaximum number of dishes you can prepare: {max_dishes}")

    except ValueError:
        print("[Error] Please enter valid integers for quantities and time.")

if __name__ == "__main__":
    main()