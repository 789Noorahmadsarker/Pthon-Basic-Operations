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
    for lin in f:
        # strip() removes the trailing newline, split(",") separates the
        # name from the amount, e.g. "John,250" -> ["John", "250"]
        customer_name, total_amount = lin.strip().split(",")

        # The amount is read as text, so convert it to an integer
        total_amount = int(total_amount)

        # Save the customer in the dictionary
        customers_dict[customer_name] = total_amount

print("Task 1:")
print(customers_dict)

# Output:
# {'Srinivas': 120, 'John': 250, 'Maria': 150, 'Smith': 510, 'Anjali': 45}



# ---------------------------------------------------------------------------
# Task 2: Define a function to calculate the rewards level
# ---------------------------------------------------------------------------
# Question:
#   Define a function called calculate_rewards that takes the total purchase
#   amount as input and returns the rewards level:
#       Bronze: Total purchases $100-$199
#       Silver: Total purchases $200-$499
#       Gold:   Total purchases $500+

def calculate_rewards(total):
    """Return the rewards level ('Gold', 'Silver', 'Bronze' or 'None')
    for a given total purchase amount."""
    # Conditions are checked from the highest level to the lowest, so each
    # one only needs a lower limit
    if total >= 500:
        return 'Gold'
    elif total >= 200:
        return 'Silver'
    elif total >= 100:
        return 'Bronze'
    else:
        # Totals below $100 do not qualify for any rewards level
        return 'None'


print("\nTask 2:")
print(calculate_rewards(530))

# Output:
# Gold



# ---------------------------------------------------------------------------
# Task 3: Build the customer summary dictionary
# ---------------------------------------------------------------------------
# Question:
#   For each customer in customers_dict, calculate the rewards level and
#   build a customer_summary dictionary. The key is the customer's name and
#   the value is a tuple containing the total amount and the rewards level.

# Dictionary to store {customer_name: (total_amount, rewards_level)}
customer_summary = {}

# items() gives us each name and its total amount at the same time
for name, total in customers_dict.items():
    rewards_level = calculate_rewards(total)
    customer_summary[name] = (total, rewards_level)

print("\nTask 3:")
print(customer_summary)

# Output (printed on one line, wrapped here for readability):
# {'Srinivas': (120, 'Bronze'),
#  'John': (250, 'Silver'),
#  'Maria': (150, 'Bronze'),
#  'Smith': (510, 'Gold'),
#  'Anjali': (45, 'None')}


