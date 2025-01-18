import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)


number_of_days = input(int("Enter the number of days to add to the current date: "))
def calculate_future_date():
    display_current_datetime()
    future_date = current_date + timedelta(number_of_days)
    future_date = future_date.strftime("%Y-%m-%d")
    print(future_date)
    


if __name__ == "__main__":
    calculate_future_date()