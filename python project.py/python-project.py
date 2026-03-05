# Write a program that shows Snack menu and allows the user to select an item. The program should then display the price of the selected item.
# Display the snack menu to the user
# Define the snack menu with items and their prices
# Prompt the user to select an item from the menu
# Check if the user's selection is valid and display the price
# keep the program running until the user decides to exit
snack_menu = {
    "1": {"name": "Chips", "price": 1.50},
    "2": {"name": "Chocolate", "price": 2.00},
    "3": {"name": "Cookies", "price": 1.75},
    "4": {"name": "Soda", "price": 1.25},
    "5": {"name": "milkshake", "price": 1.75},
    "6": {"name": "Sandwich", "price": 2.50},
    "7": {"name": "Fruit Salad", "price": 3.00},
    "8": {"name": "Yogurt", "price": 1.00},
    "9": {"name": "Granola Bar", "price": 1.25},
    "10": {"name": "Ice Cream", "price": 2.50},
    "11": {"name": "cappuccino", "price": 1.50},
    "12": {"name": "Popcorn", "price": 1.75},
}
print("Welcome to the Snack Menu!")
print("Please select an item from the menu below:")
for key, item in snack_menu.items():
    print(f"{key}. {item['name']} - ${item['price']:.2f}")
while True:
    selection = input("Enter the number of the item you want to select (or 'exit' to quit): ")
    if selection.lower() == 'exit':
        calculate_total = input("Would you like to calculate the total cost of your selected items? (yes/no): ")
        if calculate_total.lower() == 'yes':
            total = sum(item['price'] for item in snack_menu.values())
            print(f"The subtotal cost of your selected items is: ${total:.2f}")
            tax = total * 0.07  # Assuming a tax rate of 7%
            total_with_tax = total + tax
            print(f"Total with tax: ${total_with_tax:.2f}")
        print("Thank you for visiting! Goodbye!")
        break
    elif selection in snack_menu:
        selected_item = snack_menu[selection]
        print(f"You selected {selected_item['name']} which costs ${selected_item['price']:.2f}.")
    else:
        print("Invalid selection. Please try again.")       
# Write a program that shows predefined grocery items and allows the user to select an item. The program should then display the price of the selected item.
Grocery_menu ={
     "Apple": {"name": "Apple", "price": 0.50},
     "Banana": {"name": "Banana", "price": 0.30},
     "Bread": {"name": "Bread", "price": 2.00},
     "Milk": {"name": "Milk", "price": 1.50},
     "Eggs": {"name": "Eggs", "price": 2.50},
     "Cheese": {"name": "Cheese", "price": 3.00},
     "Chicken": {"name": "Chicken", "price": 5.00},
     "Rice": {"name": "Rice", "price": 1.00},
     "Pasta": {"name": "Pasta", "price": 1.50},
     "Tomatoes": {"name": "Tomatoes", "price": 0.80}
}
print("Welcome to the Grocery Menu!")
print("Please select an item from the menu below:")
for key, item in Grocery_menu.items():
    print(f"{key}. {item['name']} - ${item['price']:.2f}")
while True:
    selection = input("Enter the number of the item you want to select (or 'exit' to quit): ")
    if selection.lower() == 'exit':
        calculate_total = input("Would you like to calculate the total cost of your selected items? (yes/no): ")
        if calculate_total.lower() == 'yes':
            total = sum(item['price'] for item in Grocery_menu.values())
            print(f"The subtotal cost of your selected items is: ${total:.2f}")
            tax = total * 0.07  # Assuming a tax rate of 7%
            total_with_tax = total + tax
            print(f"Total with tax: ${total_with_tax:.2f}")
        print("Thank you for visiting! Goodbye!")
        break
    elif selection in Grocery_menu:
        selected_item = Grocery_menu[selection]
        print(f"You selected {selected_item['name']} which costs ${selected_item['price']:.2f}.")
    else:
        print("Invalid selection. Please try again.")