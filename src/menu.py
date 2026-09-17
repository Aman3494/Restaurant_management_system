menu = {
    1: {"name": "Pizza", "price": 150},
    2: {"name": "Burger", "price": 80},
    3: {"name": "Pasta", "price": 120}
}

def show_menu():
    print("\n----- MENU -----")
    for id, item in menu.items():
        print(f"{id}. {item['name']} - ₹{item['price']}")
