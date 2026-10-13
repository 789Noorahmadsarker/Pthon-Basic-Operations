"""
Loyalty Rewards Program
=======================
A Python practice exercise that reads customer purchase data from a file,
assigns each customer a rewards level, and packages everything into a
reusable function.

Scenario:
    You run a loyalty program where customers earn rewards based on the
    total amount they have spent.

Concepts covered:
    - File handling (reading a file line by line)
    - Dictionaries and tuples
    - Functions with parameters and return values
    - if / elif / else conditions
"""

# ---------------------------------------------------------------------------
# Task 1: Read the customer file into a dictionary
# ---------------------------------------------------------------------------
# Question:
#   You are given a file called customers.txt that contains the name of each
#   customer and the total amount they spent. Read this file line by line and
#   save the customer name and total amount in a dictionary.
#
#   Example of customers.txt:
#       Srinivas,120
#       John,250
#       Maria,150
#       Smith,510
#       Anjali,45

# Dictionary to store {customer_name: total_amount}
customers_dict = {}

# "with" closes the file automatically once the block ends
with open("customers.txt", "r") as f:
    for line in f:
        # strip() removes the trailing newline, split(",") separates the
        # name from the amount, e.g. "John,250" -> ["John", "250"]
        customer_name, total_amount = line.strip().split(",")

        # The amount is read as text, so convert it to an integer
        total_amount = int(total_amount)

        # Save the customer in the dictionary
        customers_dict[customer_name] = total_amount

print("Task 1:")
print(customers_dict)

# Output:
# {'Srinivas': 120, 'John': 250, 'Maria': 150, 'Smith': 510, 'Anjali': 45}
