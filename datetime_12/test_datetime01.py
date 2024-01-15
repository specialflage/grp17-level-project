# Here we will show all basic operations on datetime
from datetime import datetime  # from module datetime import class datetime
print('---- Get the current date and time -----')
today = datetime.now()
print(today)
print('---- get only date or time or their parts -------')
print(today.date())
print(today.date().year)
print(today.date().month)
print(today.date().day)

print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)

print('---- Re Formatting date, time --- | we use strftime() function----')
print('----- Convert date into string using strftime() function -----')
print(  today.strftime('%d-%m-%Y %y %y %w') ) # day, month, year, y, weekday
print(  today.strftime('%B-%b-%Y %A %y %a') ) # Month, Mon, Day, dy
print(today.strftime('%H-%M-%S')) # Hours on 24 style

print('-----------------------Create a custom date : 24-04-2023-------------------------------')
print('---1st way : datetime object using constructor ()')
custom_date = datetime(2023, 4, 24) #(Year=2023, month=4, day=24)
print(custom_date)

print('------2nd way - by converting a string to date using strptime() Function-----')
date_style_string = '24-04-2023'
new_custom_date = datetime.strptime(date_style_string, '%d-%m-%Y')
print(new_custom_date)
