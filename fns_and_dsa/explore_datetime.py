from datetime import datetime
from datetime import timedelta
current_date = datetime.now()
def display_current_datetime():
    global current_date
    print(f"Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}")
display_current_datetime()
def calculate_future_date(number_of_days):
    global current_date
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.year}-{future_date.month}-{future_date.day}")
fd = int(input("enter # of days:"))
calculate_future_date(fd)

