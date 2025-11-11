# ------ Python Date Time ------

# Python has a datetime module to handle date and time.

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
print(dir(datetime))  # ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

# With dir or help built-in commands it is possible to know the available functions in a certain module.
# The datetime module has many functions, but we will focus on date, datetime, time and timedelta.

# ------ Getting Datetime Information ------

now = datetime.now()
print('Now:', now)  # Now: 2025-11-03 15:57:29.129868
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute

if minute < 10:
    minute = '0' + str(minute)  # Add 0 before minute if minutes is under 10

second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)  # 3 11 2025 16 01
print('timestamp:', timestamp)  # timestamp: 1762185704.108623
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 3/11/2025, 16:01

# ------ Formatting Date Output Using strftime ------

new_year = datetime(2026, 1, 1)
print('new_year:', new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute, second)  # 1 1 2026 0 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2026, 0:0

# Current Date and Time
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time:', t)  # time: 16:17:14

time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
# mm/dd/YY H:M:S format
print('time_one:', time_one)

time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
# # dd/mm/YY H:M:S format
print('time_two:', time_two)

# ------ String to Time Using strptime ------

date_string = '25 December, 2025'
print('date_string:', date_string)
date_object = datetime.strptime(date_string, '%d %B, %Y')
print('date_object:', date_object)

# ------ Using date From datetime ------

d = date(2025, 1, 1)
print('d:', d)
print('Current Date:', d.today())  # Current Date: 2025-11-03
# Date object of today's date
today = date.today()
print('Current Year:', today.year)  # Current Year: 2025
print('Current Month:', today.month)  # Current Month: 11
print('Current Day:', today.day)  # Current Day: 3

# ------ Time Objects to Represent Time ------

# time(hour = 0, minute = 0, second = 0)
a = time()
print('a:', a)  # a: 00:00:00

# time(hour, minute and second)
b = time(10, 35, 30)
print('b:', b)  # b: 10:35:30

# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c:", c)  # c: 10:30:50

# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d:", d)  # d: 10:30:50.200555

# ------ Difference Between Two Points in Time ------

today = date.today()
new_year = date(year=2026, month=1, day=1)
time_until_new_year = new_year - today
print('Time Until New Year:', time_until_new_year)  # Time Until New Year: 59 days, 0:00:00

t1 = datetime(year=2025, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print('Time left for new year:', diff)  # Time left for new year: 26 days, 23:01:00

# ------ Difference Between Two Points in Time Using timedelta ------

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t1:", t1)  # t1: 94 days, 4:00:20
print("t2:", t2)  # t2: 7 days, 5:03:30
print("t3:", t3)  # t3: 86 days, 22:56:50

# ------ Exercises ------

# 1: Get the current day, month, year, hour, minute and timestamp from datetime module.
print('1:')
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
if minute < 10:
    minute = '0' + str(minute)
timestamp = now.timestamp()
print(f'{day}/{month}/{year}, {hour}:{minute}')
print('timestamp:', timestamp)

# 2: Format the current date using this format: "%m/%d/%Y, %H:%M:%S".
print('2:')
formatted_datetime = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_datetime)

# 3: Today is 3 November, 2025. Change this time string to time.
print('3:')
date_string = '3 November, 2025'
date_object = datetime.strptime(date_string, '%d %B, %Y')
print(date_object)

# 4: Calculate the time difference between now and new year.
print('4:')
today = date.today()
new_year = date(2026, 1, 1)
difference = new_year - today
print('Time until new year:', difference)

# 5: Calculate the time difference between 1 January 1970 and now.
print('5:')
old_date = date(1970, 1, 1)
difference = today - old_date
print(difference)
