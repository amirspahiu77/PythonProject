import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)

print("Year: ", current_datetime.year)
print("Month: ", current_datetime.month)
print("Day: ", current_datetime.day)
print("Hour: ", current_datetime.hour)
print("Minute: ", current_datetime.minute)
print("Second: ", current_datetime.second)
print("Microsecond: ", current_datetime.microsecond)

#date class
current_date = datetime.datetime.now().date()
print(current_date)
print("Year: ", current_date.year)
print("Month: ", current_date.month)
print("Day: ", current_date.day)

#time class

current_time = datetime.datetime.now().time()
print(current_time)
print("Hour: ", current_time.hour)
print("Minutes: ", current_time.minute)
print("second: ", current_time.second)

specific_date = datetime.date(2025, 4, 25)
specific_date = datetime.time(12, 30, 0)

#timedelta
duration = datetime.timedelta(days=5, hours=3)

new_date = current_date + duration
print(new_date)

previous_date = current_date - duration
print(previous_date)

utc_time = datetime.datetime.now(datetime.timezone.utc)
print(utc_time)

custom_offset = datetime.timedelta(hours=3)

