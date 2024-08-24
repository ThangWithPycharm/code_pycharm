from datetime import datetime

from dateutil.relativedelta import relativedelta

# 2020-02-25
given_date = datetime(2020, 2, 25).date()

new_date = given_date + relativedelta(months = 4)
print(new_date)


