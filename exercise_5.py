# Exercise 5: Weekly Temperatures Analysis
print("\n--- Lab Exercise 5 ---")

temperatures = []

# Read temperatures for 7 days 
for i in range(1, 8):
    temp = float(input(f"Enter temperature for day {i}: "))
    temperatures.append(temp)

# Calculate Average, Maximum, and Minimum 
avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)

print(f"Average temperature: {avg_temp:.1f}")
print(f"Maximum temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")

# Identify days where temperature was above average 
days_above_avg = []
for index, temp in enumerate(temperatures):
    if temp > avg_temp:
        # Add 1 to index because days start from 1
        days_above_avg.append(str(index + 1)) 

print(f"Days above average: {', '.join(days_above_avg)}")