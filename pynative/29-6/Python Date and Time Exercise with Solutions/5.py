""" Find the day of the week of a given date """
from datetime import datetime
import calendar
from datetime import datetime

given_date = datetime(2020, 7, 26)
day_of_week = datetime.strftime(given_date, "%A")
print(day_of_week)

# or


given_date = datetime(2020, 7, 26)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)
