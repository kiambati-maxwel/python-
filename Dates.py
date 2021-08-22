 # Get the current date and time
 # We need to use the datetime library
from datetime import datetime, timedelta

current_date = datetime.now()
# the now functions returns a datetime object

print(str(current_date))

# timedelta is delta is used to define a period of time
one_day = timedelta(days=1)
yesterday = current_date - one_day

print(str(current_date.day))

# get a birthday date and store it as a date
# birthday = input('when is your birthday (dd/mm/yy) ?')
# birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

one_week = timedelta(weeks=1)
last_week  = datetime.now() - one_week
print(str(last_week))
