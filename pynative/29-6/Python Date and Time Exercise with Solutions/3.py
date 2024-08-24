""" Subtract a week (7 days)  from a given date in Python """
from datetime import datetime, timedelta
given_date = datetime(2020, 2, 25)
future_date = given_date - timedelta(days=7)
print(future_date)