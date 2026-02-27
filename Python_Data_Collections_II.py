# Initial shopping list
shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]

# ------------------ Task 1 ------------------

# Add new item
shopping_list.append({"item": "Butter", "price": 80})

# Remove first item
shopping_list.pop(0)

# Print number of items
print("Number of items:", len(shopping_list))

# ------------------ Task 2 ------------------

# Calculate total cost (basic loop)
total_cost = 0
for item in shopping_list:
    total_cost += item["price"]

# Find most expensive item (basic loop)
most_expensive = shopping_list[0]

for item in shopping_list:
    if item["price"] > most_expensive["price"]:
        most_expensive = item


print("Most Expensive Item:", most_expensive["item"], "-", most_expensive["price"])
print("Total Cost:", total_cost)

# ------------------ Task 3 ------------------

# Calculate average price manually (2 decimal places)
average_price = total_cost / len(shopping_list)

# Convert to 2 decimal places without using round()
average_price = int(average_price * 100) / 100

summary = {
    "total_items": len(shopping_list),
    "total_cost": total_cost,
    "average_price": average_price
}

print("Summary:", summary)
