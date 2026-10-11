"""
Inventory Reorder Check
=======================
A Python practice exercise that simulates a simple inventory management
system by finding products whose stock is below a minimum level.

Concepts covered:
    - Working with parallel lists (names and stock levels)
    - for loops with range() and len()
    - if conditions and comparison operators
    - append() to build a new list
"""

# ---------------------------------------------------------------------------
# Task 8: Find products that need to be reordered
# ---------------------------------------------------------------------------
# Question:
#   Managing inventory efficiently is crucial for businesses so they do not
#   run out of key products. Using two lists (product names and their stock
#   levels):
#       1. Check each item to see if its stock level is below a minimum
#          threshold.
#       2. If the stock level is below the minimum, add the product's name
#          to a reorder list.
#       3. Print the list of products that need to be reordered.

# Lists for product names and stock levels.
# The stock at each index belongs to the product at the same index.
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

# Minimum stock threshold before a product needs to be reordered
minimum_stock = 10

# Initialize an empty list to hold the names of items that need reordering
reorder_list = []

# Loop through the indices of the lists so that we can read the name and
# the stock level of the same product using the same index
for i in range(len(product_names)):
    if stock_levels[i] < minimum_stock:             # Check if stock is below minimum
        reorder_list.append(product_names[i])       # Add the product name to the reorder list

# Print the reorder list
print("Items to Reorder:")
for product in reorder_list:
    print(f"- {product}")

# Sample Output:
# Items to Reorder:
# - Pears
# - Grapes
