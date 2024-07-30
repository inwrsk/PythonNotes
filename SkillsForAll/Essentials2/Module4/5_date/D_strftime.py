from datetime import date,time
d=date(2003,9,26)
#by using this we can get date in req format
print(d.strftime('%d/%m/%y'))#26/09/03
print(d)#2003-09-26
t=time(14,34,26)
print(t,t.strftime('%H::%M::%S'))#14:34:26 14::34::26#case sensitive
#eg:m = months, M=min