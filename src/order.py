from .menu import menu

orders = []

def take_order():
    total = 0
    while True:
        try:
            choice = int(input("Enter item number (0 to finish): "))
            if choice == 0:
                break
            if choice in menu:
                quantity = int(input("Enter quantity: "))
                item_total = menu[choice]['price'] * quantity
                orders.append((menu[choice]['name'], quantity, item_total))
                total += item_total
            else:
                print("Invalid item.")
        except ValueError:
            print("Invalid input.")
    return total, orders
