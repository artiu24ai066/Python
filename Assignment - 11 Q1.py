import pandas as pd
from datetime import datetime, date, time

dt_jan15_2012 = pd.to_datetime("2012-01-15")
print("a) Date time object for Jan 15 2012:", dt_jan15_2012)

dt_specific_time = pd.to_datetime("2012-01-15 21:20")
print("b) Specific date and time of 9:20 pm:", dt_specific_time)

local_datetime = pd.Timestamp.now()
print("c) Local date and time:", local_datetime)

date_only = pd.to_datetime("2024-04-10").date()
print("d) A date without time:", date_only)

current_date = date.today()
print("e) Current date:", current_date)

time_from_datetime = local_datetime.time()
print("f) Time from a datetime:", time_from_datetime)

current_local_time = datetime.now().time()
print("g) Current local time:", current_local_time)
