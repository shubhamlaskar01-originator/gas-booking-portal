# booking.py
# Handles gas booking, bill calculation, stock deduction and credit settlement.

from constants import CNG_PRICE, LPG_PRICE, LOW_STOCK_THRESHOLD
from accounts import find_customer


def book_gas(customers, inventory):
    """Main entry point for booking gas for an existing customer."""
    name = input("Enter customer name: ").strip()
    customer = find_customer(customers, name)
    if not customer:
        print("Customer not found. Please create an account first.")
        return

    print("1. CNG only  (Rs.", CNG_PRICE, "/unit)")
    print("2. LPG only  (Rs.", LPG_PRICE, "/unit)")
    print("3. Both CNG and LPG")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter 1, 2 or 3.")
        return

    total_amount = 0

    if choice == 1:
        total_amount += _book_single(inventory, "CNG", CNG_PRICE, customer, "cng_qty")
    elif choice == 2:
        total_amount += _book_single(inventory, "LPG", LPG_PRICE, customer, "lpg_qty")
    elif choice == 3:
        total_amount += _book_single(inventory, "CNG", CNG_PRICE, customer, "cng_qty")
        total_amount += _book_single(inventory, "LPG", LPG_PRICE, customer, "lpg_qty")
    else:
        print("Invalid choice.")
        return

    if total_amount > 0:
        customer["amount_due"] = float(customer.get("amount_due", 0)) + total_amount
        print(f"\nTotal amount to be paid: Rs.{total_amount}")

        pay_choice = input("Settle this amount using credit balance now? (y/n): ").strip().lower()
        if pay_choice == "y":
            _settle_via_credit(customer, total_amount)


def _book_single(inventory, gas_type, price, customer, field_name):
    """Book one gas type: validate quantity, check stock, update records."""
    try:
        qty = int(input(f"Enter quantity of {gas_type} to book: "))
    except ValueError:
        print("Invalid quantity entered. Skipping this item.")
        return 0

    if qty <= 0:
        print("Quantity must be a positive number. Skipping this item.")
        return 0

    available = inventory.get(gas_type, 0)
    if qty > available:
        print(f"Insufficient {gas_type} stock. Only {available} units available.")
        return 0

    inventory[gas_type] = available - qty
    customer[field_name] = int(customer.get(field_name, 0)) + qty
    amount = qty * price
    print(f"{qty} unit(s) of {gas_type} booked. Amount for this item: Rs.{amount}")

    if inventory[gas_type] < LOW_STOCK_THRESHOLD:
        print(f"WARNING: {gas_type} stock is now low ({inventory[gas_type]} units remaining).")

    return amount


def _settle_via_credit(customer, amount):
    """Deduct the billed amount from the customer's credit balance, if sufficient."""
    credit = float(customer.get("credit", 0))
    if credit >= amount:
        customer["credit"] = credit - amount
        customer["amount_due"] = float(customer.get("amount_due", 0)) - amount
        print("Payment successful. Amount deducted from credit balance.")
    else:
        print(f"Insufficient credit balance (Rs.{credit}). Payment not completed; amount remains due.")
