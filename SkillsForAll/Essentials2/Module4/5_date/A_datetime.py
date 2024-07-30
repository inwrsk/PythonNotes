from datetime import datetime
dte=datetime(2004,3,5)
dte2=datetime(2003,9,26,9,26,30)
print(dte,dte.date(),dte.time(),sep='\n')
'''
2004-03-05 00:00:00
2004-03-05
00:00:00
'''
print(dte2,dte2.date(),dte2.time(),sep='\n')
'''
2003-09-26 09:26:30
2003-09-26
09:26:30
'''