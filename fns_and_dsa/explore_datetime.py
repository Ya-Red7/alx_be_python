from datetime import datetime
from datetime import timedelta
current_date = datetime.now()
Y,m,d,H,M,S = current_date.year,current_date.month,current_date.day,current_date.hour,current_date.minute,current_date.second
def display_current_datetime():

    print(f"Current date and time: {Y}-{m}-{d} {H}:{M}:{S}")
display_current_datetime()
def calculate_future_date(number_of_days):
    global current_date
    future_date = current_date + timedelta(days=number_of_days)
    Y,m,d = future_date.year,future_date.month,future_date.day
    print(f"Future date: {Y}-{m}-{d}")
fd = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(fd)

