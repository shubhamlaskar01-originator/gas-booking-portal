# storage.py
# Handles all reading/writing of data to CSV files.
# This replaces a database with plain Python file handling.

import csv
import os
from constants import CUSTOMERS_FILE, INVENTORY_FILE, CUSTOMER_FIELDS


def ensure_data_files():
    """Create the data folder and starter CSV files if they don't exist yet."""
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(CUSTOMERS_FILE):
        with open(CUSTOMERS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CUSTOMER_FIELDS)
            writer.writeheader()

    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["gas_type", "stock_qty"])
            writer.writerow(["CNG", 500])
            writer.writerow(["LPG", 500])


def load_customers():
    """Read all customer records from the CSV file into a list of dictionaries."""
    customers = []
    try:
        with open(CUSTOMERS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                customers.append(row)
    except FileNotFoundError:
        print("Customer data file not found. Starting with an empty list.")
    except IOError as e:
        print("Error reading customer data:", e)
    return customers


def save_customers(customers):
    """Write the full list of customer dictionaries back to the CSV file."""
    try:
        with open(CUSTOMERS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CUSTOMER_FIELDS)
            writer.writeheader()
            writer.writerows(customers)
    except IOError as e:
        print("Error saving customer data:", e)


def load_inventory():
    """Read gas stock levels from the CSV file into a dictionary."""
    inventory = {}
    try:
        with open(INVENTORY_FILE, newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header row
            for row in reader:
                if len(row) == 2:
                    inventory[row[0]] = int(row[1])
    except FileNotFoundError:
        print("Inventory file not found. Starting with default stock.")
    except IOError as e:
        print("Error reading inventory data:", e)
    return inventory


def save_inventory(inventory):
    """Write current stock levels back to the CSV file."""
    try:
        with open(INVENTORY_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["gas_type", "stock_qty"])
            for gas_type, qty in inventory.items():
                writer.writerow([gas_type, qty])
    except IOError as e:
        print("Error saving inventory data:", e)
