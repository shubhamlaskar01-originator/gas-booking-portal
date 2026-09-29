# constants.py
# Central place for all configuration values used across the project.

CNG_PRICE = 75          # Rs. per unit
LPG_PRICE = 80          # Rs. per unit
LOW_STOCK_THRESHOLD = 50  # Below this, a low-stock warning is shown

CUSTOMERS_FILE = "data/customers.csv"
INVENTORY_FILE = "data/inventory.csv"

LOGIN_USERNAME = "learnpython4cbse"
LOGIN_PASSWORD = "learnpython4cbse"

CUSTOMER_FIELDS = [
    "name", "acc_no", "date", "address",
    "cng_qty", "lpg_qty", "amount_due", "credit"
]
