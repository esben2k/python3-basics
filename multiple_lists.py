#multiple_lists.py

is_stock = ['blue pens', 'paper', 'staples']

shopping_cart = ['blue pens', 'paper', 'staples', 'orange post-its']

for item in shopping_cart:
    if item in is_stock:
        print("Adding " + item + " to your order")
    else:
        print("Sorry " + item + " is not in stock.")
print("Your order is complete")
