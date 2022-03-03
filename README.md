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

| Commands           | Description of commands                          |
| ------------------ | ------------------------------------------------ |
| -h                 | Shows the help message and exits the program     |
| show-date          | Shows the system date                            |
| set-current-date   | Set the system date to the current date          |
| advance-date       | Advance the date by a number of days             |
| register-purchase  | Register the purchase of a product               |
| register-sale      | Register the sale of a product                   |
| show-total-revenue | Shows the total revenue                          |
| show-date-revenue  | Shows the total revenue, between two dates       |
| show-inventory     | Shows the amount of currently available products |
| show-sales         | Shows all the sales made                         |
| show-purchases     | Shows all the purchases made                     |

- ### `show-date`

Shows the date currently maintained by the system, saved in date.txt (note: system date is not necessarily today's date)

`python main.py show-date`

- ### `set-current-date`

Uses datetime to get today's date and writes this date to date.txt

`python main.py set-current-date`

- ### `advance-date`

Asks for an integer and advances the system date by this many days by writing the new date to date.txt

`python main.py advance-date`

- ### `register-purchase`

Starts the buy registration process, asks for a product name, amount (int), the price (float, accepts int), number of days from now the product will expire (int) and writes the bought item(s) to the bought.csv file

`python main.py register-purchase`

- ### `register-sale`

Starts the sales registration process, asks for a product name and number of items and checks if these are available, asks for sell price and writes the sold products to sales.csv

`python main.py register-sale`

- ### `show-total-revenue`

Reads all the sales prices from sales.csv and shows the total

`python main.py show-total-revenue`

- ### `show-date-revenue`

Same as total revenue, but asks for two dates, earliest first and latest second, in 'YYYY-MM-DD' format and returns the total revnue between the given dates

`python main.py show-date-revenue`

- ### `show-inventory`

Checks which items are currently available and uses Rich to report the numbers

`python main.py show-inventory`

- ### `show-sales`

Reads sales.csv and reports all the relevant information using a Rich Table

`python main.py show-sales`

- ### `show-purchases`

Reads bought.csv and reports all the relevant information using a Rich Table

`python main.py show-purchases`
