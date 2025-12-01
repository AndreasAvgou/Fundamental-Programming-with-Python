def add_item(shopping_list, item):
    """Adds an item to the shopping list."""
    shopping_list.append(item)
    print(f"[Success] '{item}' has been added to the list.")

def remove_item(shopping_list, item):
    """Removes an item from the shopping list if it exists."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"[Success] '{item}' has been removed.")
    else:
        print(f"[Error] Item '{item}' was not found in the list.")

def show_list(shopping_list):
    """Displays all items in the shopping list."""
    print("\n--- Current Shopping List ---")
    if not shopping_list:
        print("The list is empty.")
    else:
        # Enumerate gives us a counter (i) starting from 1
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    print("-----------------------------")

def search_item(shopping_list, item):
    """Searches for a specific item in the list."""
    if item in shopping_list:
        print(f"[Result] Yes, '{item}' is in your list.")
    else:
        print(f"[Result] No, '{item}' is NOT in the list.")

def main():
    shopping_list = []
    
    while True:
        print("\n=== MENU ===")
        print("1. Add product")
        print("2. Remove product")
        print("3. Show list")
        print("4. Search product")
        print("5. Exit")
        
        choice = input("Choice: ")
        
        if choice == "1":
            item = input("Enter the product you want to add: ")
            add_item(shopping_list, item)
            
        elif choice == "2":
            item = input("Enter the product you want to remove: ")
            remove_item(shopping_list, item)
            
        elif choice == "3":
            show_list(shopping_list)
            
        elif choice == "4":
            item = input("Enter the product you are looking for: ")
            search_item(shopping_list, item)
            
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Program Start
if __name__ == "__main__":
    main()