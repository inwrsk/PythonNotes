import time
#to get timestamp for particular time
timestamp=time.mktime((2004,3,5,0,0,0,0,0,0))
print(timestamp)#1078425000.0

struct_time=time.localtime(timestamp)
print(struct_time)#time.struct_time(tm_year=2004, tm_mon=3, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=65, tm_isdst=0)