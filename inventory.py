# inventory.py
# Handles viewing and restocking gas cylinder inventory.

from constants import LOW_STOCK_THRESHOLD


def view_inventory(inventory):
    """Print current stock levels, flagging any that are running low."""
    if not inventory:
        print("No inventory data found.")
        return

    print("\n--- CURRENT STOCK LEVELS ---")
    for gas_type, qty in inventory.items():
        status = "LOW STOCK!" if qty < LOW_STOCK_THRESHOLD else "OK"
        print(f"{gas_type}: {qty} units  [{status}]")


def restock(inventory):
    """Add more units to a gas type's stock."""
    gas_type = input("Enter gas type to restock (CNG/LPG): ").strip().upper()
    if gas_type not in inventory:
        print("Invalid gas type. Must be CNG or LPG.")
        return

    try:
        qty = int(input(f"Enter quantity to add to {gas_type} stock: "))
    except ValueError:
        print("Invalid quantity.")
        return

    if qty <= 0:
        print("Quantity must be a positive number.")
        return

    inventory[gas_type] += qty
    print(f"{gas_type} stock updated. New stock level: {inventory[gas_type]} units.")
