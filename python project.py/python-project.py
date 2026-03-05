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
# write a program that show to do list and allows the user to select a task. The program should then display the details of the selected task.
To_do_list = {
    "1": {"task": "Buy groceries", "details": "Milk, Eggs, Bread, and Fruits"},
    "2": {"task": "Clean the house", "details": "Vacuum, Dust, and Mop the floors"},
    "3": {"task": "Finish homework", "details": "Complete math and science assignments"},
    "4": {"task": "Exercise", "details": "Go for a 30-minute run and do strength training"},
    "5": {"task": "Call family", "details": "Catch up with parents and siblings"},
    "6": {"task": "Pay bills", "details": "Electricity, Water, and Internet"},
    "7": {"task": "Read a book", "details": "Read at least 20 pages of a novel"},
    "8": {"task": "Cook dinner", "details": "Prepare a healthy meal with vegetables and protein"},
    "9": {"task": "Organize workspace", "details": "Declutter desk and organize files"},
    "10": {"task": "Plan weekend trip", "details": "Research destinations and make reservations"}
}
print("Welcome to your To-Do List!")
print("Please select a task from the list below:")
for key, task in To_do_list.items():
    print(f"{key}. {task['task']}") 
while True:    
    selection = input("Enter the number of the task you want to view (or 'exit' to quit): ")
    if selection.lower() == 'exit':
        print("Thank you for using the To-Do List! Goodbye!")
        break
    elif selection in To_do_list:
        selected_task = To_do_list[selection]
        print(f"You selected '{selected_task['task']}' which has the following details: {selected_task['details']}")    
    else:
        print("Invalid selection. Please try again.")
        