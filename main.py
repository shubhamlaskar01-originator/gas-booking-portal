# main.py
# Entry point for the Gas Cylinder Booking & Inventory Management System.
# Run this file from the terminal with: python main.py

from auth import login
from storage import (
    ensure_data_files,
    load_customers,
    save_customers,
    load_inventory,
    save_inventory,
)
from accounts import create_account, update_address
from booking import book_gas
from reports import view_all_customers, search_customer
from inventory import view_inventory, restock


def print_menu():
    print("\n===== GAS CYLINDER BOOKING & INVENTORY SYSTEM =====")
    print("1. Create Account")
    print("2. Book Gas / Generate Bill")
    print("3. View All Customers")
    print("4. Search Customer")
    print("5. Update Customer Address")
    print("6. View Inventory Stock")
    print("7. Restock Inventory")
    print("0. Logout & Save")


def main():
    ensure_data_files()

    if not login():
        return

    customers = load_customers()
    inventory = load_inventory()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(customers)
        elif choice == "2":
            book_gas(customers, inventory)
        elif choice == "3":
            view_all_customers(customers)
        elif choice == "4":
            search_customer(customers)
        elif choice == "5":
            update_address(customers)
        elif choice == "6":
            view_inventory(inventory)
        elif choice == "7":
            restock(inventory)
        elif choice == "0":
            save_customers(customers)
            save_inventory(inventory)
            print("Data saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
