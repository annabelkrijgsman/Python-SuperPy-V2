# Report

_Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable, explain what problem they solve and why you chose to implement it in this way. Include this in your repository as a report.md file._

## Rich - table module

For a more front-end type of person like myself this was really nice to built into the program. After watching some YouTube video's I managed to show a few outputs of the program in nicely looking tables.

[Preview table view](https://i.imgur.com/7kjDrP9.png)

## The option to export data to a CSV and/or PDF file

In the `show-inventory` command you have the option to only show the inventory in the commandline, as well as the options to export the data to a CSV and/or PDF file. If this file already exists you will get a notification. If the file does not already exists a file called _export_inventory.csv_/_export_inventory.pdf_ will be created and the current inventory will be written to the file.

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
