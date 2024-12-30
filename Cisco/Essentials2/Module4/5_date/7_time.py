from datetime import time
t=time()
print(t)#00:00:00
t=time(22,30,9,9)
print(t)#22:30:09.000009#hour,min,sec,microsec
print(t.hour,t.minute,t.second)#22 30 9
import time#sec from 1970
print(time.time(),type(time.time()))#1715611618.4985156 <class 'float'>