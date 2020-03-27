import datetime
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
day2 = now.today().strftime('%A')

print  year , month , day , hour, day2 