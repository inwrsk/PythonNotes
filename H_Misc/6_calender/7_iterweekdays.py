import calendar
c=calendar.Calendar(6)
print(c)
for i in c.iterweekdays():
    print(i,end=' ')#6 0 1 2 3 4 5
calendar.prmonth(2003,9)
'''#not changed it is limited to c object
    September 2003
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
'''
calendar.setfirstweekday(6)
calendar.prmonth(2003,9)
'''
   September 2003
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
'''