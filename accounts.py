# accounts.py
# Handles creating new customer accounts and updating existing ones.

import datetime


def find_customer(customers, name):
    """Search the customer list by name (case-insensitive). Return the dict or None."""
    for c in customers:
        if c["name"].strip().lower() == name.strip().lower():
            return c
    return None


def create_account(customers):
    """Ask the user for details and add a new customer record."""
    name = input("Enter customer name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if find_customer(customers, name):
        print("A customer with this name already exists.")
        return

    while True:
        try:
            acc_no = int(input("Enter account number: "))
            break
        except ValueError:
            print("Please enter a valid whole number for account number.")

    address = input("Enter address: ").strip()

    while True:
        try:
            credit = float(input("Enter opening credit amount (0 if none): "))
            break
        except ValueError:
            print("Please enter a valid amount (numbers only).")

    new_customer = {
        "name": name,
        "acc_no": acc_no,
        "date": datetime.date.today().isoformat(),
        "address": address,
        "cng_qty": 0,
        "lpg_qty": 0,
        "amount_due": 0,
        "credit": credit,
    }
    customers.append(new_customer)
    print(f"Account created successfully for '{name}'.")


def update_address(customers):
    """Update the address of an existing customer."""
    name = input("Enter customer name to update: ").strip()
    customer = find_customer(customers, name)
    if not customer:
        print("Customer not found.")
        return

    new_address = input("Enter new address: ").strip()
    if not new_address:
        print("Address cannot be empty. No changes made.")
        return

    customer["address"] = new_address
    print("Address updated successfully.")
