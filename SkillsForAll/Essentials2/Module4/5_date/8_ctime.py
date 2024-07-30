import time
#ctime takes secs and cal date,time from 1970
print(time.ctime())#Mon May 13 20:55:42 2024#it give current time
timestamp=time.time()-86400#seconds from 1970 to yesterday
print(time.ctime(timestamp))#Sun May 12 20:55:42 2024