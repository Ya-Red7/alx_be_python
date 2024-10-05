from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    form = '%Y-%m-%d %H:%M:%S'
    print(f"Current date and time: {current_date.strftime(form)}")
display_current_datetime()

def calculate_future_date(number_of_days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    form = '%Y-%m-%d'
    print(f"Future date: {future_date.strftime(form)}")
fd = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(fd)

