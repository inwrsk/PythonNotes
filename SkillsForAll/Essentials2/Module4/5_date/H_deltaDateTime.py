from datetime import timedelta,date,datetime
delta=timedelta(days=1,hours=1)
print(delta)#1 day, 1:00:00
dt1=date(2003,9,25)+delta
print(dt1)#2003-09-26
dt2=datetime(2003,9,25,12,23,45)+delta
print(dt2)#2003-09-26 13:23:45