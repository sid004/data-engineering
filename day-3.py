# Exercise 1 — List total

# Given `amounts = [1200, 2500, 800, 1500]`, calculate the total using a loop.

amounts = [1200, 2500, 800, 1500]
total_amount = 0

for amount in amounts:
    total_amount = total_amount + amount

print(total_amount)

# Exercise 2 — Find large orders
# Use a loop to print only amounts greater than or equal to 2000 from `[1200, 2500, 800, 3200]`.

amounts = [1200, 2500, 800, 3200]

for amount in amounts:
    if amount >= 2000:
        print(amount)

# Exercise 3 — Clean customer names

# Clean `[' rahul ', 'ANU', ' priya ']` by removing extra spaces and converting names to title case. Store the results in a new list.

customers = [' rahul ', 'ANU', ' priya ']

clean_customers = []

for customer in customers:
    clean_name = customer.strip().title()
    clean_customers.append(clean_name)

print(clean_customers)

#Given the list below, create a new list containing only cleaned customer names that start with the letter A.

# Requirements:
# 1. Remove extra spaces.
# 2. Convert each name to title case.
# 3. Keep only names beginning with A.
# 4. Print the new list.

customers = [" anu ", "Rahul", " AMIT ", "priya", " anjali "]

new_customer = []

for customer in customers:
    clean_name = customer.strip().title()
    if clean_name[0] == "A":
        new_customer.append(clean_name)

print(new_customer)