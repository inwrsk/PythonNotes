#0 to 6 mond to sunday
from datetime import date
d=date.today()
print(d,d.weekday())#2024-05-13 0
#0 is monday to 6 is sunday
d=date(2004,3,5)
print(d.weekday())#4
#4 is friday