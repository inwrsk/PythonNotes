import time
y=time.time()
print(y)#1715592193.5612142 secs since jan 1 1970
from datetime import date
d=date.fromtimestamp(y)
print(d)#2024-05-13#this is the date after y secs from jan 1 1970
d2=date.fromtimestamp(y+86401)
print(d2)#2024-05-14