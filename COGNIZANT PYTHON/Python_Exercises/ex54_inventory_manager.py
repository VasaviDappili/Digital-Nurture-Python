inventory = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 2
}

low_stock = {item for item, qty in inventory.items() if qty < 5}

print("Inventory:", inventory)
print("Low Stock Alerts:", low_stock)