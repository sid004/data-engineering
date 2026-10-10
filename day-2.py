# Exercise 1 — Discount calculator

product_price = 1200;
quantity = 3;
discount = 300;

final_amount = (product_price * quantity) - discount ;
print(final_amount);

# Type conversion

quantity = "4";
price = 250;

quantity = int(quantity);
total = quantity * price;

print(total);

# Exercise 3 — Order classification

# If an order amount is at least 5000, print Premium. Otherwise, if it is at least 2000, print High-value. Otherwise, print Regular.

order_amount = 1999;

if order_amount >= 5000:
    print("Premium")
elif order_amount >= 2000:
    print("High-value")
else:
    print("Regular")

# Problem: Given order_amount = "2500", write Python code that:
# 1. Converts the amount into a number.
# 2. Prints "Valid order" if the amount is greater than zero.
# 3. Prints "Invalid order" otherwise.
# Bonus: What happens if the input is "abc" instead of "2500"?

order_amount = "abc"

try:
    order_amount = int(order_amount)

    if order_amount > 0:
        print("Valid Order")
    else:
        print("Invalid Order")
except ValueError:
    print("Invalid data the value should be integer")