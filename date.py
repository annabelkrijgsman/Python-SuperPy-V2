import datetime

path = "./data/date.txt"

def get_date():
    with open(path, "r") as file:
        for line in file:
            return line

def print_date():
    date = ""
    with open(path, "r") as file:
        for line in file:
            date = line
    print(f"The current system date is: {date}")

def set_current_date():
    today = str(datetime.date.today())
    with open(path, "w") as file:
        file.write(today)
    print(f"The system date has changed to: {today}")

def advance_time(days):
    today = datetime.datetime.strptime(get_date(), "%Y-%m-%d").date()
    new_date = today + datetime.timedelta(days)
    with open(path, "w") as file:
        file.write(str(new_date))
        print(f"The new system date is: {new_date}")