# Exercise 31 - Create List

def display_cart(cart):

    if not cart:
        print("Cart is empty")
        return

    print("Cart Items:", cart)


cart = [100, 250, 75]

display_cart(cart)