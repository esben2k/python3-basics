#empty lists

#empty shopping cart
shopping_cart = ['pens']
#shopping_cart = []

if shopping_cart:
    for item in shopping_cart:
        print("Adding " + item + " to your cart.")
    print("Your order is complete")
else:
    print("You must select an item before proceeding")
    
