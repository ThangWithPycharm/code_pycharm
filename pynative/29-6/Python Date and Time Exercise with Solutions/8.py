""" Convert the following datetime into a string """
""" Expected output:

"2020-02-25 00:00:00" """
from datetime import datetime

given_date = datetime(2020, 2, 25)
string_date = datetime.strftime(given_date, "%Y-%m-%d %H:%M:%S")
print(string_date)
print(type(string_date))
