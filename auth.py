# auth.py
# Handles user login for the system.

from constants import LOGIN_USERNAME, LOGIN_PASSWORD


def login():
    """Prompt for username and password. Return True if they match, else False."""
    print("..............GAS CYLINDER BOOKING & INVENTORY SYSTEM..............")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username == LOGIN_USERNAME and password == LOGIN_PASSWORD:
        print("Login successful. Welcome!")
        return True
    else:
        print("Invalid username or password. Access denied.")
        return False
