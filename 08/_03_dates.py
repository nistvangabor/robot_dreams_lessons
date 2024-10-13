from datetime import datetime, timezone, timedelta

now = datetime.now(timezone.utc)
print(f"Current date and time: {now}")
print(type(now))
print(now.tzname())

#STRING TO DATE
date_string = "2023-10-11 15:30:45"
date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(type(date_object))

#DATE TO STRING
date_string = datetime.strftime(date_object, "%Y-%m-%d %H:%M")
print(date_string)


five_days = timedelta(days=5)
new_date = now + five_days
print(f"New date after 5 days: {new_date}")
