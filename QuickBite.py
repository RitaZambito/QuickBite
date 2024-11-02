# Initialize the menu with items and their prices
menu = {
    "Cheeseburger": 5.99,
    "Hotdog": 3.49,
    "Chicken Nuggets": 4.99,
    "Pizza": 7.99,
    "Veggie Burger": 5.49,
    "Toast": 2.49,
    "Sandwich": 3.99,
    "Chicken Wings": 6.99,
    "Fries": 2.99,
    "Chips": 2.99,
    "Salad": 4.49,
    "Ice Cream": 2.99,
    "Cheesecake": 4.49,
    "Donuts": 1.99,
    "Milkshake": 3.99,
    "Hot Drink": 1.49,
    "Soft Drink": 1.49
}

# List to store the current order
order = []


# Function to display the menu
def display_menu():
    print("\n--- QuickBite Food Menu ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print("----------------------------")


# Function to add items to the order
def add_to_order():
    item_name = input("Enter the name of the item you want to order: ").strip()
    if item_name in menu:  # Check if the item exists in the menu
        order.append(item_name)
        print(f"{item_name} has been added to your order.")
    else:
        print("Item not found. Please choose a valid menu item.")


# Function to display the current order and calculate the total price
def view_order():
    if not order:
        print("Your order is empty.")
    else:
        print("\nYour Order:")
        total_price = 0
        for item in order:
            price = menu[item]
            total_price += price
            print(f"- {item}: ${price:.2f}")
        print(f"Total Price: ${total_price:.2f}")


# Function to checkout and complete the order
def checkout():
    if not order:
        print("Your order is empty. Please add items before checking out.")
    else:
        view_order()
        confirm = input("Would you like to complete your order? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Thank you for your order! Have a great day!")
            order.clear()  # Clear the order after checkout
        else:
            print("Order cancelled.")


# Main loop to run the food ordering system
while True:
    print("\n--- QuickBite Ordering System ---")
    print("1. View Menu")
    print("2. Add to Order")
    print("3. View Order")
    print("4. Checkout")
    print("5. Exit")
    print("----------------------------")

    # Get user choice
    choice = input("Enter your choice (1-5): ")

    # Handle each choice using the defined functions
    if choice == '1':
        display_menu()
    elif choice == '2':
        add_to_order()
    elif choice == '3':
        view_order()
    elif choice == '4':
        checkout()
    elif choice == '5':
        print("Exiting the system. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
