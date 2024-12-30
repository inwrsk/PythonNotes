#we know date,time and we should create datetime object
from datetime import datetime
dte=datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
print(dte,dte.date(),type(dte))#2019-11-04 14:53:00 2019-11-04 <class 'datetime.datetime'>
import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
#time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)