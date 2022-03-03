from revenue import get_total_revenue, get_revenue_between_dates
from inventory import get_bought_items, get_bought_between_dates
from rich import print

def get_total_profit():
    bought_items = get_bought_items()
    total_revenue = get_total_revenue()
    total = 0
    for item in bought_items:
        total += float(item["buy_price"])

    sum = total_revenue - total
    return sum

def print_total_profit():
    total_profit = get_total_profit()
    print(f"The total revenue is: {total_profit} eur")

def get_profit_between_dates(first_date, second_date):
    total = 0
    items = get_bought_between_dates(first_date, second_date)
    for item in items:
        total += float(item["buy_price"])
    return total

def print_profit_between_dates(first_date, second_date):
    profit = get_profit_between_dates(first_date, second_date)
    revenue = get_revenue_between_dates(first_date, second_date)
    sum = revenue - profit
    print(f"The total profit in the chosen period was {sum} eur")