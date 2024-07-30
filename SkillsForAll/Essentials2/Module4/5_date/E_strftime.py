import time
timestamp=1050000000
st=time.gmtime(timestamp)
print(st)
'''
time.struct_time(tm_year=2003, tm_mon=4, tm_mday=10, tm_hour=18, tm_min=40, tm_sec=0, tm_wday=3, 
tm_yday=100, tm_isdst=0)
'''
print(time.strftime('%H:%M:%S %d/%m/%y',st))#18:40:00 10/04/03 #formatted time according to st
print(time.strftime('%H:%M:%S %d/%m/%y'))#10:00:15 14/05/24 #according to current time