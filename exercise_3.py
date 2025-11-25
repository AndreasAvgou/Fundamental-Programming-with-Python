# Exercise 3: Order Management System
print("\n--- Lab Exercise 3 ---")

print("Welcome to Cafe Python!")
print("Available products: coffee, juice, snack")
print("Type 'end' to finish the order.")

total_cost = 0.0
total_coffees = 0

# Price list dictionary 
prices = {"coffee": 2.00, "juice": 2.50, "snack": 3.00}

while True:
    # Read product input and normalize to lowercase
    product = input("Enter product: ").lower()
    
    # Exit condition 
    if product == "end":
        break
        
    # Validation: Check if product exists 
    if product not in prices:
        print("Invalid product. Please try again.")
        continue
    
    quantity = int(input("Quantity: "))
    item_cost = 0.0
    
    # Logic for coffee orders using 'for' loop as required 
    if product == "coffee":
        for i in range(quantity):
            total_coffees += 1
            # Offer: Price is 1.50 instead of 2.00 for every coffee after the 3rd one 
            if total_coffees > 3:
                item_cost += 1.50
            else:
                item_cost += 2.00
    else:
        # Standard calculation for other products
        item_cost = prices[product] * quantity

    print(f"Subtotal for {quantity} {product}(s): {item_cost:.2f}€")
    total_cost += item_cost

# Apply 10% discount if total cost exceeds 20€ 
if total_cost > 20:
    print(f"Original Amount: {total_cost:.2f}€")
    total_cost *= 0.90
    print("10% discount applied.")

print(f"Final payment amount: {total_cost:.2f}€")