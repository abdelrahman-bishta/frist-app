# Restaurant Ordering System
total_bill = 0.0  # Total for the bill
orders = []  # To store orders (optional, for display at the end)
name = input("Hello! What's your name? ")

print(f"Welcome to our restaurant, {name}! We will now present you with four menus. You will choose one item from each menu.")

# First menu: Appetizers
print("\n--- First Menu: Appetizers ---")
appetizers = [
    ("Greek Salad", 15.0),
    ("Chicken Soup", 12.0),
    ("Mini Burger", 18.0)
]
for i, (item, price) in enumerate(appetizers, 1):
    print(f"{i}. {item} - {price} EGP")
choice1 = int(input("Choose the item number from this menu (1-3): ")) - 1
selected_item1 = appetizers[choice1]
total_bill += selected_item1[1]
orders.append(selected_item1[0])

# Second menu: Main Courses
print("\n--- Second Menu: Main Courses ---")
mains = [
    ("Beef Steak", 50.0),
    ("Grilled Fish", 45.0),
    ("Cheese Pasta", 35.0)
]
for i, (item, price) in enumerate(mains, 1):
    print(f"{i}. {item} - {price} EGP")
choice2 = int(input("Choose the item number from this menu (1-3): ")) - 1
selected_item2 = mains[choice2]
total_bill += selected_item2[1]
orders.append(selected_item2[0])

# Third menu: Desserts
print("\n--- Third Menu: Desserts ---")
desserts = [
    ("Ice Cream", 10.0),
    ("Chocolate Cake", 15.0),
    ("Fresh Fruits", 8.0)
]
for i, (item, price) in enumerate(desserts, 1):
    print(f"{i}. {item} - {price} EGP")
choice3 = int(input("Choose the item number from this menu (1-3): ")) - 1
selected_item3 = desserts[choice3]
total_bill += selected_item3[1]
orders.append(selected_item3[0])

# Fourth menu: Drinks
print("\n--- Fourth Menu: Drinks ---")
drinks = [
    ("Orange Juice", 12.0),
    ("Coffee", 8.0),
    ("Mineral Water", 5.0)
]
for i, (item, price) in enumerate(drinks, 1):
    print(f"{i}. {item} - {price} EGP")
choice4 = int(input("Choose the item number from this menu (1-3): ")) - 1
selected_item4 = drinks[choice4]
total_bill += selected_item4[1]
orders.append(selected_item4[0])

# Display the bill
print(f"\n--- Your Bill, {name} ---")
print("Your orders:")
for order in orders:
    print(f"- {order}")
print(f"Total: {total_bill} EGP")
print("Thank you for your visit! Welcome anytime.")
