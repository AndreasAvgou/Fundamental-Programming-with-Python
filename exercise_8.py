# Exercise 8: Student Grades Dictionary
print("--- Lab Exercise 8: Student Grades ---")

def calculate_average(grades):
    """Helper function to calculate the average of a list of grades."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

# 1. Create a dictionary with student names and their grades
# Key: Student Name (String), Value: List of grades (List of floats)
students = {
    "Alice": [8.5, 9.0, 7.5],
    "Bob": [6.0, 5.5, 6.5],
    "Charlie": [9.5, 10.0, 9.0],
    "Diana": [7.0, 7.5, 8.0],
    "Eve": [4.0, 5.0, 3.5]
}

print(f"\n1. Initial Dictionary created with {len(students)} students.")

# 2. Add a new student dynamically
print("\n--- Adding a New Student ---")
new_name = input("Enter student name: ")
grades_input = input("Enter grades separated by space (e.g., 8 9 10): ")

try:
    # Convert string input "8 9 10" to list of floats [8.0, 9.0, 10.0]
    new_grades = [float(g) for g in grades_input.split()]
    students[new_name] = new_grades
    print(f"[Success] {new_name} added to the dictionary.")
except ValueError:
    print("[Error] Invalid input. Please enter numeric grades.")

# 3. Calculate and Print Average for each student
print("\n--- Student Averages ---")
highest_avg = -1
top_student = ""

for name, grades in students.items():
    avg = calculate_average(grades)
    print(f"{name}: {avg:.2f}")
    
    # Check for top student
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

# 4. Find and print the student with the highest average
if top_student:
    print(f"\n--- Top Student ---")
    print(f"Name: {top_student}")
    print(f"Average: {highest_avg:.2f}")

# 5. Search for a student
print("\n--- Search Student ---")
search_name = input("Enter name to search: ")

if search_name in students:
    grades = students[search_name]
    avg = calculate_average(grades)
    print(f"Found {search_name}. Grades: {grades}, Average: {avg:.2f}")
else:
    print(f"Student '{search_name}' not found.")