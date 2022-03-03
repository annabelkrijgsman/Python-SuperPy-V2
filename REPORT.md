# Report

_Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable, explain what problem they solve and why you chose to implement it in this way. Include this in your repository as a report.md file._

## Rich - table module

For a more front-end type of person like myself this was really nice to built into the program. After watching some YouTube video's I managed to show a few outputs of the program in nicely looking tables.

[Preview table view](https://i.imgur.com/7kjDrP9.png)

## Buy and Sell

Both the buy and sell functions take multiple arguments of a specific format in order to write data to a csv.

In the code example below you can see how I decided to solve this problem. By wrapping the try except in a while True loop, the program will keep asking for input until a valid input has been given.

```
while True:
    try:
        amount = int(input("Enter the quantity of the purchased product (example input: 4): "))
        break
    except:
        print("Please try again with a whole number (example input: 4): ")
```

## Inventory functions

In the inventory.py file I decided to write all the functions in small seperate steps, so parts can be easily reused.

For example:

```
def get_bought_items():
    # Reads the bought.csv file and returns a list of dictionaries containing all bought items.
```

is used later in:

```
def get_available_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    today = get_date()
    for item in bought_items:
        if item["id"] not in sold_ids and item["expiration_date"] >= today:
            available_products.append(item)
    return available_products
```

and also:

```
def get_expired_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    expired_products = []
    today = get_date()
    for item in bought_items:
        if item["id"] not in sold_ids and item["expiration_date"] < today:
            expired_products.append(item)
    return expired_products
```
