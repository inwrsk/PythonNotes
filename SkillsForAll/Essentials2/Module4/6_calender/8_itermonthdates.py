import calendar
c=calendar.Calendar()
for i in c.itermonthdates(2003,9):
    print(i)
'''
2003-09-01
2003-09-02
2003-09-03
.
.
.
2003-10-02
2003-10-03
2003-10-04
2003-10-05
'''
#the dates of adjacent months also appear in the matrix
calendar.prmonth(2003,9)
'''
   September 2003
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
'''