import calendar
c=calendar.Calendar()
for i in c.itermonthdays(2004,3):
    print(i,end=' ')#1 2 3 4 5 6 7 8 9....7 28 29 30 31 0 0 0 0