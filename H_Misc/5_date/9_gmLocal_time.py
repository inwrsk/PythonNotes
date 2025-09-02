import time
print(time.gmtime())#time.struct_time(tm_year=2024, tm_mon=5, tm_mday=13, tm_hour=15, tm_min=55, tm_sec=15, tm_wday=0, tm_yday=134, tm_isdst=0)
print(time.localtime())#time.struct_time(tm_year=2024, tm_mon=5, tm_mday=13, tm_hour=21, tm_min=25, tm_sec=15, tm_wday=0, tm_yday=134, tm_isdst=0)
#they can take timestamp in arg and gives the date
print(time.localtime().tm_year)#2024