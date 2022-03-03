# Imports
import argparse
from date import advance_time, print_date, set_current_date
from purchases import purchase_product
from sales import sell_product
from inventory import display_inventory, display_sales, display_purchases
from revenue import print_total_revenue
from profit import print_total_profit
from rich.console import Console
from rich import print

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

parser = argparse.ArgumentParser(description="Supermarket 101 Iventory")

subparser = parser.add_subparsers(dest="command", required=True)

# Add parsers
show_date = subparser.add_parser("show-date", help="Show the system date")
set_today = subparser.add_parser("set-current-date", help="Set the system date to the current date")
advance_date = subparser.add_parser("advance-date", help="Advance the date by a number of days")
purchase = subparser.add_parser("register-purchase", help="Register the purchase of a product")
sale = subparser.add_parser("register-sale", help="Register the sale of a product")
total_revenue = subparser.add_parser("show-total-revenue", help="Shows the total revenue")
date_revenue = subparser.add_parser("show-date-revenue", help="Shows the total revenue, between two dates")
total_profit = subparser.add_parser("show-total-profit", help="Shows the total profit")
date_profit = subparser.add_parser("show-date-profit", help="Shows the total profit, between two dates")
inventory = subparser.add_parser("show-inventory", help="Shows the amount of currently available products")
sales = subparser.add_parser("show-sales", help="Shows all the sales made")
purchases = subparser.add_parser("show-purchases", help="Shows all the purchases made")

# Add arguments
advance_date.add_argument("--days", type= int)

purchase.add_argument("--productname", type = str)
purchase.add_argument("--quantity", type = int)
purchase.add_argument("--price", type = float)
purchase.add_argument("--expiration", type = int)

sale.add_argument("--productname", type= str)
sale.add_argument("--quantity", type= int)
sale.add_argument("--price", type= float)

date_revenue.add_argument("--firstdate", type= str)
date_revenue.add_argument("--seconddate", type= str)

# Set defaults
show_date.set_defaults(func=print_date)
set_today.set_defaults(func=set_current_date)
total_revenue.set_defaults(func=print_total_revenue)
total_profit.set_defaults(func=print_total_profit)
inventory.set_defaults(func=display_inventory)
sales.set_defaults(func=display_sales)
purchases.set_defaults(func=display_purchases)

args = parser.parse_args()

if args.command == "advance-date":
    advance_date.set_defaults(
        func=advance_time(args.days)
    )

if args.command == "register-purchase":
    purchase.set_defaults(
        func=purchase_product(
            args.productname, 
            args.quantity,
            args.price,
            args.expiration
        )
    )

if args.command == "register-sale":
    sale.set_defaults(
        func=sell_product(
            args.productname,
            args.quantity,
            args.price
        )
    )

if args.command == "show-date-revenue":
    date_revenue.set_defaults(
        func=revenue.print_revenue_between_dates(
            args.firstdate,
            args.seconddate
        )
    )

# if args.command == "show-date-profit":
#     date_profit.set_defaults()                                     # Make functionalities

# Got to fix this situation down below... :-)
if args.command != "advance-date":
    if args.command != "register-purchase":
        if args.command != "register-sale":
            if args.command != "show-date-revenue":
                # if args.command != "show-date-profit":
                    def main():
                        args.func()
                        
                    if __name__ == "__main__":
                        main()