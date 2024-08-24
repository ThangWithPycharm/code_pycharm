""" Convert string into a datetime object """
from datetime import datetime
date_string = "Feb 25 2020 4:20PM"
dt_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(dt_object)