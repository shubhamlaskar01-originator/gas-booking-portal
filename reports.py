# reports.py
# Handles displaying customer records - all of them, or a single searched one.

from accounts import find_customer


def view_all_customers(customers):
    """Print details of every customer on record."""
    if not customers:
        print("No customer records found.")
        return

    print("\n--- ALL CUSTOMER RECORDS ---")
    for c in customers:
        _print_customer(c)


def search_customer(customers):
    """Ask for a name and print that one customer's details."""
    name = input("Enter customer name to search: ").strip()
    customer = find_customer(customers, name)
    if not customer:
        print("Customer not found.")
        return
    _print_customer(customer)


def _print_customer(c):
    """Helper to neatly print a single customer's record."""
    print("-" * 50)
    print(f"Name        : {c['name']}")
    print(f"Account No. : {c['acc_no']}")
    print(f"Date Joined : {c['date']}")
    print(f"Address     : {c['address']}")
    print(f"CNG Booked  : {c['cng_qty']} units")
    print(f"LPG Booked  : {c['lpg_qty']} units")
    print(f"Amount Due  : Rs.{c['amount_due']}")
    print(f"Credit Bal. : Rs.{c['credit']}")
