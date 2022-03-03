from revenue import get_total_revenue
from inventory import get_bought_items
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