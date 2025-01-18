import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)


number_of_days = input(int("Enter number of days: "))
def calculate_future_date():
    display_current_datetime()
    future_date = current_date + timedelta(number_of_days)
    print(future_date)
    


if __name__ == "__main__":
    calculate_future_date()