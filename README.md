# Welcome to SuperPy

SuperPy is a supermarket inventory system using command line arguments

_Assignment by Winc Academy_

## Modules

- [Argparse](https://docs.python.org/3/library/argparse.html)
- [CSV](https://docs.python.org/3/library/csv.html)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [Rich](https://rich.readthedocs.io/en/stable/introduction.html)

## Command line options

Positional arguments:

| Commands           | Description of commands                                                                 |
| ------------------ | --------------------------------------------------------------------------------------- |
| -h                 | Shows the help message and exits the program                                            |
| show-date          | Shows the system date                                                                   |
| set-current-date   | Set the system date to the current date                                                 |
| advance-date       | Advance the date by a number of days                                                    |
| register-purchase  | Register the purchase of a product                                                      |
| register-sale      | Register the sale of a product                                                          |
| show-total-revenue | Shows the total revenue                                                                 |
| show-date-revenue  | Shows the total revenue, between two dates                                              |
| show-total-profit  | Shows the total profit                                                                  |
| show-date-profit   | Shows the total profit, between two dates                                               |
| show-inventory     | Shows the amount of currently available products, and gives the option to export to CSV |
| show-sales         | Shows all the sales made                                                                |
| show-purchases     | Shows all the purchases made                                                            |

- ### `show-date`

Shows the date currently maintained by the system, saved in date.txt (note: system date is not necessarily today's date)

`python main.py show-date`

- ### `set-current-date`

Uses datetime to get today's date and writes this date to date.txt

`python main.py set-current-date`

- ### `advance-date`

Asks for an integer and advances the system date by this many days by writing the new date to date.txt

`python main.py advance-date --days 3`

- ### `register-purchase`

Starts the buy registration process, asks for a product name (str), quantity (int), the price (float, accepts int), number of days from now the product will expire (int) and writes the bought item(s) to the bought.csv file

`python main.py register-purchase --productname Olives --quantity 5 --price 1.55 --expiration 10`

- ### `register-sale`

Starts the sales registration process, asks for a product name (str) and number of products sold (int), asks for sell price (float) and writes the sold products to sales.csv

`python main.py register-sale --productname Olives --quantity 2 --price 2.15`

- ### `show-total-revenue`

Reads all the sales prices from sales.csv and shows the total

`python main.py show-total-revenue`

- ### `show-date-revenue`

Same as total revenue, but asks for two dates, earliest first and latest second, in 'YYYY-MM-DD' format and returns the total revnue between the given dates

`python main.py show-date-revenue --firstdate 2022-01-01 --seconddate 2022-03-03`

- ### `show-total-profit`

Calculates and shows the total profit from the data in bought.csv and sales.csv

`python main.py show-total-profit`

- ### `show-date-profit`

Same as total profit, but asks for two dates, earliest first and latest second, in 'YYYY-MM-DD' format and returns the total profit between the given dates

`python main.py show-date-profit --firstdate 2022-01-01 --seconddate 2022-03-03`

- ### `show-inventory`

Checks which items are currently available and uses Rich to report the numbers. Also gives you the option to export the data.

To see the inventory _without_ an export, use the following command:
`python main.py show-inventory`

To see the inventory _and_ receive an export, use the following command:
`python main.py show-inventory --export Yes`

- ### `show-sales`

Reads sales.csv and reports all the relevant information using a Rich Table

`python main.py show-sales`

- ### `show-purchases`

Reads bought.csv and reports all the relevant information using a Rich Table

`python main.py show-purchases`
