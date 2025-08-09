# # Define the menu of the restaurant :-

# menu = {
#     'Pizza':40,
#     'Pasta':50,
#     'burger':50,
#     'salad':70,
#     'coffee':80
# }
# # Great!!
# print("WElcome to Rudra's Cafe")
# print("Menu:-\nPizza:   Rs 40\nPasta:   Rs 50\nburger:  Rs 50\nsalad:   Rs 70\ncoffee:  RS 80")

# order_total = 0

# item_1 = input("Enter the name of item you want to order = ")
# if item_1 in menu:
#     order_total += menu[item_1]
#     print("your item {item_1} has been added to your order")

# else:
#     print(f"Ordered item {item_1} is not available yet!")

# another_order = input("Do you want to add another item? (yes/no) ")
# if another_order == "yes":
#     item_2 = input("Enter the name of second item = ")
#     if item_2 in menu:
#         order_total += menu[item_2]
#         print("your item {item_2} has been added to your order")

#     else:
#         print(f"Ordered item {item_2} is not available yet!")

# print(f"The total amount of items is {order_total}")


# Hotel Menu System

# # Menu Dictionary
# menu = {
#     'Burger': 99,
#     'Pizza': 199,
#     'Pasta': 149,
#     'Fries': 29,
#     'Soda': 49
# }

# # Store order
# order = {}

# def show_menu():
#     print("\n---- HOTEL MENU ----")
#     for item, price in menu.items():
#         print(f"{item} - {price:.2f}")
#     print("--------------------")

# def take_order():
#     while True:
#         show_menu()
#         item = input("Enter item name to order (or 'done' to finish): ").title()
#         if item.lower() == 'done':
#             break
#         if item in menu:
#             quantity = int(input(f"How many {item}s? "))
#             if item in order:
#                 order[item] += quantity
#             else:
#                 order[item] = quantity
#         else:
#             print("Item not on menu. Please try again.")

# def calculate_total():
#     total = 0
#     for item, quantity in order.items():
#         total += menu[item] * quantity
#     return total

# def process_payment(total):
#     while True:
#         print(f"Your total is: ${total:.2f}")
#         amount = float(input("Enter payment amount: "))
#         if amount >= total:
#             change = amount - total
#             print(f"Payment accepted. Change: {change:.2f}")
#             break
#         else:
#             print("Insufficient amount. Please enter enough to cover the total.")

# def print_receipt():
#     print("\n----- RECEIPT -----")
#     for item, quantity in order.items():
#         price = menu[item]
#         print(f"{item} x {quantity} = ${price * quantity:.2f}")
#     total = calculate_total()
#     print(f"TOTAL = {total:.2f}")
#     print("-------------------")

# # Run the hotel menu system
# take_order()
# total = calculate_total()
# process_payment(total)
# print_receipt()


# Improved version using AI :-



# # Hotel Menu System

# Menu Dictionary
menu = {
    'Burger': 60,
    'Pizza': 199,
    'Pasta': 99,
    'Fries': 49,
    'Soda': 30
}

# Store order
order = {}

def show_menu():
    print("\n---- HOTEL MENU ----")
    for item, price in menu.items():
        print(f"{item} - {price:.2f}")
    print("--------------------")

def take_order():
    # Great!!
    print("WElcome to Rudra's Cafe\n")
    while True:
        show_menu()
        items_input = input("Enter items to order (e.g.'burger,pizza and soda' or 'done' to finish): ").lower()
        if items_input == 'done':
            break
        
        items_input = items_input.replace('and',',')
        item_list = [item.strip().title() for item in items_input.split(',') if item.strip()]

        for item in item_list:
            if item in menu:
                try:
                    quantity = int(input(f"How many {item}s? "))
                    order[item] = order.get(item, 0) + quantity
                except ValueError:
                    print("Please enter a valid number for quantity.")
            else:
                print(f"Sorry,{item} is not on the menu.")

def calculate_total():
    return sum(menu[item] * quantity for item, quantity in order.items())

def process_payment(total):
    while True:
        print(f"Your total is: {total:.2f}")
        try:
            amount = float(input("Enter payment amount: "))
            if amount >= total:
                change = amount - total
                print(f"Payment accepted. Change: {change:.2f}")
                break
            else:
                print("Insufficient amount. Please enter enough to cover the total.")
        except ValueError:
            print("Please enter a valid amount.")

def print_receipt():
    print("\n----- RECEIPT -----")
    for item, quantity in order.items():
        price = menu[item]
        print(f"{item} x {quantity} = {price * quantity:.2f}")
    total = calculate_total()
    print(f"TOTAL = {total:.2f}")
    print("-------------------")

# Run the hotel menu system
take_order()
total = calculate_total()
process_payment(total)
print_receipt()


     

