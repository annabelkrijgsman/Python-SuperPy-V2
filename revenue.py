from inventory import get_sold_between_dates, get_sold_items
from rich import print

def get_total_revenue():
    sold_items = get_sold_items()
    total = 0
    for item in sold_items:
        total += float(item["sell_price"])
    return total

# Write functions down below for calculating profit
# def get_total_purchase():
#     return 10

# def get_total_profit():
#     return get_total_revenue - get_total_purchase

def print_total_revenue():
    total_revenue = get_total_revenue()
    print(f"The total revenue is: {total_revenue} eur")

def get_revenue_between_dates(first_date, second_date):
    total = 0
    items = get_sold_between_dates(first_date, second_date)
    for item in items:
        total += float(item["sell_price"])
    return total

def print_revenue_between_dates(first_date, second_date):
    revenue = get_revenue_between_dates(first_date, second_date)
    print(f"The total revenue in the chosen period was {revenue} eur")