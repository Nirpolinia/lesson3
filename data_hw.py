from datetime import date, datetime, timedelta

dt_today = date.today()
dt_yesterday = dt_today - timedelta(days=1)
dt_30 = dt_today - timedelta(days=30)
print(dt_today)
print(dt_yesterday)
print(dt_30)

datetime_str = '01/01/25 12:10:03.234567'  
datetime_datetime = datetime.strptime(datetime_str,'%m/%d/%y %H:%M:%S.%f')
print(datetime_datetime)