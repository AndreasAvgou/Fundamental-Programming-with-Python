# Fundamental Programming with Python 

This repository contains a collection of Python scripts developed. The exercises are designed to cover fundamental programming concepts ranging from basic I/O to functions and list manipulation.

## 📂 Project Structure

The exercises are divided into 6 distinct scripts, each focusing on specific programming topics:

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

## 🚀 How to Run

Ensure you have Python installed (version 3.x is recommended).

1.  Clone the repository.
2.  Navigate to the directory.
3.  Run any exercise using the command line:

```bash
python exercise_1.py
