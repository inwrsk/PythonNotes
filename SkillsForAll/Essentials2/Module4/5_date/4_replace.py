from datetime import date
d=date(2004,3,5)
print(d)#2004-03-05
#if you want to change the date
print(d.year)#2004
#d.year=2003#not writable
#we can do this by replace
print(d.replace(2003,9,26))#2003-09-26
print(d,type(d))#2004-03-05#<class 'datetime.date'>
d=d.replace(2003,9,26)