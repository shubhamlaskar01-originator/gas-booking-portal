# Gas Cylinder Booking & Inventory Management System MADE BY SHUBHAM LASKAR 26BCE11245

## Overview
A command-line application to manage gas cylinder customer accounts, bookings, 
billing, and inventory stock levels. Built in Python using file handling (CSV) 
for data persistence.

## Features
- Customer account creation and address updates
- Book CNG and/or LPG cylinders with automatic bill calculation
- Real-time inventory stock deduction with low-stock warnings
- Credit balance settlement for bills
- View all customers or search a specific customer's record
- Restock inventory
- Data saved to CSV files, persists between sessions

## Technologies/Tools Used
- Python 3
- Built-in `csv`, `os`, and `datetime` modules (no external libraries)

## Project Structure
- `main.py` – entry point, menu loop
- `constants.py` – configuration (prices, thresholds, file paths)
- `storage.py` – reads/writes customer and inventory CSV files
- `auth.py` – login handling
- `accounts.py` – create/update customer accounts
- `booking.py` – booking and billing logic
- `reports.py` – view/search customer records
- `inventory.py` – stock viewing and restocking
- `data/` – auto-generated folder holding customers.csv and inventory.csv

## Steps to Install & Run
1. Clone or download this repository.
2. Ensure Python 3 is installed (`python --version`).
3. Open a terminal in the project folder.
4. Run: `python main.py`
5. Login with username: `learnpython4cbse`, password: `learnpython4cbse`
6. Follow the on-screen numbered menu.

## Instructions for Testing
- Create a new account (option 1), then book gas for that same customer name (option 2) to verify billing and stock deduction.
- View inventory (option 6) before and after a booking to confirm stock updates.
- Try booking more units than available stock to see the insufficient-stock error handling.
- Logout (option 0) and re-run the program to confirm data persisted in the `data/` folder.

# Problem Statement

Gas distribution agencies currently rely on manual registers to track customer 
accounts, cylinder bookings, and stock levels. This is slow, error-prone, and 
makes it difficult to track dues or low inventory in time.

## Scope
This project automates account management, booking/billing, and inventory 
tracking for a small gas distribution agency, using a command-line Python 
application with file-based data storage.

## Target Users
Gas agency staff who manage customer accounts and process daily bookings.

## High-Level Features
- Customer account management
- Gas booking with automatic bill generation
- Inventory stock tracking with low-stock alerts
- Customer record reporting and search
