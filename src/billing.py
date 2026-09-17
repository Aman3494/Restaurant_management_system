def generate_bill(orders, total):
    print("\n----- BILL -----")
    for name, qty, price in orders:
        print(f"{name} x{qty} = ₹{price}")
    tax = total * 0.05
    print(f"Tax: ₹{tax:.2f}")
    print(f"Grand Total: ₹{total + tax:.2f}")
