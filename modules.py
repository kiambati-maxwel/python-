# core python module

# import datetime
# from datetime import date
# # import time
# from time import time

# today = date.today()

# print(today)

# timestamp = time()

# print(timestamp)


# import custom module
from validator import validate_email

email = 'myemail@emailio'

print(validate_email(email))
