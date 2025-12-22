# Fundamental Programming with Python 

This repository contains a collection of Python scripts developed. The projects progress are designed to cover fundamental programming concepts ranging from basic I/O to functions and list manipulation.

## 📂 Project Structure

The exercises are divided into 9 distinct scripts, each focusing on specific programming topics:

### 1. Basic Operations (`exercise_1.py`)
* **Goal:** Introduction to variables and arithmetic operators.
* **Functionality:** Reads two integers and calculates their sum, difference, product, and quotient. Includes a check to prevent division by zero.

### 2. Advanced Conditionals (`exercise_2.py`)
* **Goal:** Working with complex `if-elif-else` logic and boolean operators.
* **Functionality:** Analyzes two input numbers based on various conditions:
    * Checks if numbers are positive, negative, or zero.
    * Performs conditional arithmetic (e.g., calculates sum only if both are positive).
    * Identifies properties like even/odd sums or "large" sums (>100).

### 3. Order Management System (`exercise_3.py`)
* **Goal:** Implementing loops (`while`, `for`) and flow control (`break`, `continue`).
* **Functionality:** A simple coffee shop console app.
    * Accepts multiple orders (Coffee, Juice, Snack) until the user types "end".
    * Applies specific business logic:
        * **Discount:** 10% off if the total exceeds 20€.
        * **Offer:** After the 3rd coffee, the price drops from 2.00€ to 1.50€.

### 4. Linear Motion Simulation (`exercise_4.py`)
* **Goal:** Physics simulation using loops and input validation.
* **Functionality:** Simulates linear motion with constant acceleration ($v = u + at$).
    * Validates non-negative inputs.
    * Prints a second-by-second table of velocity and distance.
    * Includes a safety warning if velocity exceeds 100 m/s.
    * **Feature:** Uses nested loops to "predict" velocity for the next 3 seconds when velocity is a multiple of 10.

### 5. Temperature Analysis (`exercise_5.py`)
* **Goal:** Introduction to Lists (Arrays) and statistical calculations.
* **Functionality:**
    * Stores daily temperatures for a week in a list.
    * Calculates Average, Maximum, and Minimum temperatures.
    * Identifies specific days where the temperature was above average.

### 6. Modular Programming (`exercise_6.py`)
* **Goal:** Defining and calling custom Functions.
* **Functionality:** Processes a list of space-separated integers using three custom functions:
    * `find_max(numbers)`: Returns the largest number.
    * `reverse_list(numbers)`: Returns the list in reverse order.
    * `count_even(numbers)`: Counts how many numbers are even.
      
### 7. Shopping List Manager (exercise_7.py)
* **Goal:**  List manipulation, modular functions, and user interaction.
* **Functionality:** A menu-driven program to manage a weekly shopping list.
     * Uses a list data structure to store products.
     * Includes specific functions to `add`, `remove`, `search`, and `show` items.
     * Runs an interactive loop (Menu) until the user selects "Exit".

### 8. Student Grades Dictionary (`exercise_8.py`)
* **Goal:** Working with Dictionaries (Key-Value pairs) and data retrieval.
* **Functionality:** Manages a database of student grades.
     * Stores students and their grades in a dictionary `{'Name': [grades]}`.
     * Calculates and displays the average grade for each student.
     * Identifies the top-performing student.
     * Allows searching for a student's record by name.
 
### 9. Recursive Meal Planner (`exercise_9.py`)
* **Goal:** Introduction to Recursion and Optimization problems.
* **Functionality:** Solves a resource allocation problem (similar to the Knapsack problem).
     * Accepts a list of dishes with their preparation times.
     * Accepts a total available time limit.
     * Uses a **recursive function** to determine the *maximum number of dishes* that can be prepared within the time limit.

### 10. Christmas Tree Generator (`bonus_exercise.py`)
* **Goal:** String manipulation, Loop logic, and Formatting.
* **Functionality:** Prints a symmetric Christmas tree pattern based on user-defined height.
     * Calculates dynamic width for centering text.
     * Implements specific pattern rules: Top star (`+`), Ornaments (`0`) on edges, and a Trunk (`|`) at the base.

## 🚀 How to Run

Ensure you have Python installed (version 3.x is recommended).

1.  Clone the repository.
```bash
git clone [https://github.com/AndreasAvgou/Fundamental-Programming-with-Python.git](https://github.com/AndreasAvgou/Fundamental-Programming-with-Python.git)
```
2.  Navigate to the directory.
```bash
cd Fundamental-Programming-with-Python
```
3.  Run any exercise using the command line:

```bash
python3 exercise_1.py
```
## 📝 Key Learning Outcomes
Through these exercises, the following concepts are demonstrated:

* Standard Input/Output (input(), print, f-strings).
* Control Flow (if, elif, else).
* Iterative structures (for loops, while loops).
* Data Structures (Lists, Dictionaries).
* Function definition and return values.
* Recursion and algorithmic thinking.
* Input validation and error handling.
* String formatting and alignment.

