tables = {1: "Available", 2: "Available", 3: "Available"}

def book_table():
    print("\nAvailable Tables:")
    for t, status in tables.items():
        print(f"Table {t}: {status}")
    num = int(input("Enter table number to book: "))
    if num in tables and tables[num] == "Available":
        tables[num] = "Booked"
        print(f"Table {num} booked.")
    else:
        print("Not available or invalid.")
