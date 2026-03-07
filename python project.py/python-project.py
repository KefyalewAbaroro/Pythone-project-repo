# # Write a program that shows Snack menu and allows the user to select an item. The program should then display the price of the selected item.
# # Display the snack menu to the user
# # Define the snack menu with items and their prices
# # Prompt the user to select an item from the menu
# # Check if the user's selection is valid and display the price
# # keep the program running until the user decides to exit
# from asyncio import tasks
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
        calculate_total = input("Would you like to calculate the total cost of your selected items? (y/n): ")
        if calculate_total.lower() == 'y':
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
# # Write a program that shows predefined grocery items and allows the user to select an item. The program should then display the price of the selected item.
Grocery_menu ={
     "Apple": {"name": "Apple", "price": 3.50},
     "Banana": {"name": "Banana", "price": 0.52},
     "Bread": {"name": "Bread", "price": 2.00},
     "Milk": {"name": "Milk", "price": 3.50},
     "Eggs": {"name": "Eggs", "price": 2.50},
     "Cheese": {"name": "Cheese", "price": 3.00},
     "Chicken": {"name": "Chicken", "price": 5.00},
     "Rice": {"name": "Rice", "price": 4.00},
     "Pasta": {"name": "Pasta", "price": 2.25},
     "Tomatoes": {"name": "Tomatoes", "price": 0.85}
}
print("Welcome to the Grocery Menu!")
print("Please select an item from the menu below:")
for key, item in Grocery_menu.items():
    print(f"{key}. {item['name']} - ${item['price']:.2f}")
while True:
    selection = input("Enter the name of the item you want to select (or 'exit' to quit): ")
    if selection.lower() == 'exit':
        calculate_total = input("Would you like to calculate the total cost of your selected items? (y/n): ")
        if calculate_total.lower() == 'y':
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
# display to do list to the user
# define the to do list with tasks and their details
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
To_do_list = []
priorities = ["high", "medium", "low"]
while True:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == "done":
        break
    priority = input("Enter the priority (high, medium, low): ")
    if priority.lower() in priorities:
        To_do_list.append((task, priority.lower()))
        To_do_list.sort(key=lambda x: priorities.index(x[1]))
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
To_do_list.sort(key=lambda x: priorities.index(x[1]))
print("\nTo-Do List:")
for task, priority in To_do_list:
    print(f"{task} - {priority}")
    print("\nEnter the task you have completed (or type 'done' to finish): ")
while True:    
    completed_task = input()
    if completed_task.lower() == "done":
        break
    for task in To_do_list:
        if task[0].lower() == completed_task.lower():
            To_do_list.remove(task)
            print(f"Task '{completed_task}' marked as completed and removed from the list.")
            break
print("\nUpdated To-Do List:")
for task, priority in To_do_list:
    print(f"{task} - {priority}")
# # 4)	 Movie Ticket Booking Simulation
# -	Simulate a movie theater booking system that:
# •	Shows a list of available movie titles, showtimes, and seat prices.
# •	Asks the user to choose a movie and number of tickets.
# •	Confirms total price and asks if they want to book another movie.
# •	Ends when they say "no" and displays total bookings and cost.
#	write a program for Movie Ticket Booking Simulation
# •	Shows a list of available movie titles,
# •	Calculates the total price based on the selected movie and number of tickets,
# •	Provides a confirmation message with the total price.
movie_titles =     showtimes = {
        "Avator": "2:00 PM, 5:00 PM, 8:00 PM",
        "Zootopia": "1:00 PM, 4:00 PM, 7:00 PM",
        "Blockbusters & supperheroes": "3:00 PM, 6:00 PM, 9:00 PM",
        "king of king": "2:30 PM, 5:30 PM, 8:30 PM",
        "Dreams": "1:30 PM, 4:30 PM, 7:30 PM",
        "David": "2:15 PM, 5:15 PM, 8:15 PM",
        "Sarahs' oil": "3:15 PM, 6:15 PM, 9:15 PM",
        "Dogman": "2:45 PM, 5:45 PM, 8:45 PM",
        "Pets on a train": "1:45 PM, 4:45 PM, 7:45 PM",
        "Shelter": "2:00 PM, 5:00 PM, 8:00 PM",
        "Scream 7": "3:00 PM, 6:00 PM, 9:00 PM",
        "The last of us": "1:30 PM, 4:30 PM, 7:30 PM",
        "One Battle After Another": "2:15 PM, 5:15 PM, 8:15 PM",
    }
seat_prices = {
        "Avator": 12,
        "Zootopia": 8,
        "Blockbusters & supperheroes": 12,
        "king of king": 10,
        "Dreams": 8,
        "David": 12,
        "Sarahs' oil": 12,
        "Dogman": 6,
        "Pets on a train": 8,
        "Shelter": 10,
        "Scream 7": 7,
        "The last of us": 10,
        "One Battle After Another": 8,
    }
total_price = 0
tax_amount = total_price * 0.08
subtotal_price = total_price
while True:
    print("Available movies_titles:")
    print("showtimes, and seat prices:")
    for movie in movie_titles:
        print(f"- {movie} (${seat_prices[movie]}) - Showtimes: {showtimes[movie]} ")
    movie = input("Enter the movie title (or type 'done' to finish): ")
    if movie.lower() == "done":
        break
    if movie in movie_titles:
        quantity = int(input(f"Enter the number of tickets for {movie}: "))
        total_price += seat_prices[movie] * quantity
    else:
        print("Movie not found in the list. Please try again.")
print(f"The total price for your movie tickets is: ${total_price:.2f}.")
movie = input("do you want to book another movie (or type 'done' to finish): ")
print(" your booking has been confirmed. Enjoy your movie!")
print(f"The total price for your movie tickets is: ${total_price:.2f}.")
print(f"The subtotal price for your movie tickets is: ${subtotal_price:.2f}.")
print(f"The tax amount for your movie tickets is: ${tax_amount:.2f}.")
# # 5)	Create a basic quiz game that:
# # •	Asks the user a series of multiple-choice questions.
# # •	Tracks the user's score based on correct answers.
# # •	Provides feedback after each question and a final score at the end of the quiz.
my_quiz = [{

        "question": "The battle of Adwa is a battle between which two countries?",
        "options": ["Ethiopia and Italy", "Ethiopia and France", "Ethiopia and Britain"],
        "correct_answer": "Ethiopia and Italy",
        "explanation": "The Battle of Adwa was a significant battle fought on March 1, 1896, between the Ethiopian Empire and the Kingdom of Italy. The battle took place near the town of Adwa in northern Ethiopia. The Ethiopian forces. led by Emperor Menelik II, successfully defeated the Italian forces, marking a significant victory for Ethiopia and a major setback for Italian colonial ambitions in Africa. The Battle of Adwa is often regarded as a symbol of African resistance against European colonization and is celebrated as a national holiday in Ethiopia."
        
    },
    {   "question": "Who was mahatam gandhi?",
        "options": ["An Indian independence leader", "A South African civil rights activist", "A British politician"],
        "correct_answer": "An Indian independence leader",
        "explanation": "Mahatma Gandhi was an Indian independence leader who led the country's struggle for independence from British rule. He is known for his philosophy of non-violent resistance and his efforts to promote social justice and equality."
    },
    {
        "question": "What was the outcome Lichemeda agreement in 1878?",
        "options": ["Accepttance of Yohaness II as king of king", "Menelik II becomes king of Ethiopia", "Italy gains control of Eritrea"],
        "correct_answer": "Accepttance of Yohaness II as king of king",
        "explanation": "The Lichemeda agreement in 1878 resulted in the acceptance of Yohaness II as the king of Ethiopia. This agreement was a significant event in Ethiopian history as it solidified Yohaness II's position as the ruler of Ethiopia and helped to maintain the country's independence during a time of increasing European colonization in Africa."
    },
    {   "question": "Who wrote the novel 'Sememen'?",
        "options": ["Fikremarkos desta", "Sisay Negusu", "Abe Gubegnaw"],
        "correct_answer": "Sisay Negusu",
        "explanation": "Sisay Negusu is the author of the novel 'Sememen'. The novel is a significant work in Ethiopian literature and explores themes of love, identity, and social issues. Sisay Negusu is known for his unique storytelling style and has contributed greatly to the literary scene in Ethiopia."
    },
    {   "question": "Nelson Mandela was imprisoned for how many years?",
        "options": ["27 years", "30 years", "25 years"],
        "correct_answer": "27 years",
        "explanation": "Nelson Mandela was imprisoned for 27 years. He was arrested in 1962 and released in 1990. During his imprisonment, he became a symbol of the anti-apartheid movement. Mandela's release marked a significant turning point in South Africa's history, leading to the end of apartheid and the establishment of a democratic government. He later became the first black president of South Africa in 1994."
    },
    {
        "question": "who is Kuwame Nkrumah?",
        "options": ["first president of Ghana", "first president of Nigeria", "first president of Kenya"],
        "correct_answer": "first president of Ghana",
        "explanation": "Kwame Nkrumah was the first president of Ghana. He played a crucial role in Ghana's independence movement and is considered one of the founding fathers of modern Africa. Nkrumah was a strong advocate for Pan-Africanism and worked towards the unity and development of African nations. He served as Ghana's president from 1957 until 1966, when he was overthrown in a coup d'état."
    },
    {
        "question": "What is the historical background of Goree Island?",
        "options": ["A former slave trading post", "A former colonial administrative center", "A former military fort"],
        "correct_answer": "A former slave trading post",
        "explanation": "Goree Island, located off the coast of Dakar, Senegal, has a significant historical background as a former slave trading post. During the transatlantic slave trade, Goree Island served as a major hub for the capture and export of enslaved Africans to the Americas. The island's history is marked by the suffering and resilience of those who were forcibly taken from their homeland. Today, Goree Island stands as a symbol of remembrance and education about the atrocities of the slave trade."
    },
    {
        "question": "What is the solomonic dynasty?",
        "options": ["A dynasty that ruled Ethiopia from the 13th to the 20th century", "A dynasty that ruled Egypt from the 10th to the 15th century", "A dynasty that ruled Greece from the 5th to the 1st century BC"],
        "correct_answer": "A dynasty that ruled Ethiopia from the 13th to the 20th century",
        "explanation": "The Solomonic dynasty was a ruling dynasty in Ethiopia that claimed descent from King Solomon and Queen of Sheba. This dynasty ruled Ethiopia from the 13th to the 20th century and played a significant role in the country's history."
    }]
score = 0
for q in my_quiz:
    print(q["question"])
    for i, option in enumerate(q["options"]):
        print(f"{i + 1}. {option}")
    user_answer = input("Enter your answer (1, 2, or 3): ")
    if user_answer == str(q["options"].index(q["correct_answer"]) + 1):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
print(f"Your final score is: {score}/{len(my_quiz)}")
print("you are a great historian!")
  