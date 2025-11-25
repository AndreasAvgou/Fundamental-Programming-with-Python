# Exercise 4: Physics Simulation (Linear Motion)
print("\n--- Lab Exercise 4 ---")

# 1. Input loop to ensure non-negative values for time 
while True:
    u = float(input("Enter initial velocity u (m/s): "))
    a = float(input("Enter acceleration a (m/s^2): "))
    t_total = int(input("Enter total time t (s): "))
    
    # Check if time is positive (Velocity u can be anything, time must be > 0)
    if t_total > 0:
        break
    print("Please enter a positive value for time.")

print(f"{'Time (s)':<10} {'Velocity (m/s)':<15} {'Distance (m)':<15}")

# 2. Loop for each second from 1 to t 
for t in range(1, t_total + 1):
    # Calculate velocity and distance
    v = u + a * t
    s = u * t + 0.5 * a * (t ** 2)
    
    print(f"{t:<10} {v:<15.2f} {s:<15.2f}")
    
    # 3. Warning if velocity exceeds 100 m/s 
    if v > 100:
        print("! The body is moving very fast!")
    
    # 5. Optional: Nested loop for prediction if velocity is a multiple of 10 
    if v % 10 == 0:
        print(f"Prediction for next 3s:")
        for next_t in range(1, 4):
            pred_time = t + next_t
            pred_v = u + a * pred_time
            print(f"  At {pred_time}s -> velocity: {pred_v:.2f} m/s")

    # 4. Stop simulation if body stops (v <= 0) while decelerating 
    if a < 0 and v <= 0:
        print("The body has stopped.")
        break