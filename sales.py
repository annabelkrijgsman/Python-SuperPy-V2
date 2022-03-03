from itertools import product
from date import get_date
from inventory import get_available_product
from purchases import get_new_id
from rich import print
import csv

def sell_product(product_name, quantity, price):
    today = get_date()
    available_products = get_available_product(product_name)
    path = "./data/sold.csv"
    with open(path, "a", newline="") as file:
        csv_writer = csv.writer(file)
        for i in range(quantity):
            bought_id = available_products[i]["id"]
            id = get_new_id(path) + i
            product = [id, bought_id, today, price]
            csv_writer.writerow(product)
    print(f"You have sold {quantity}x {product_name}, for {price} eur, on {today}")