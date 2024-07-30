#note for x/y or x%y or x//y
#if y is positive the x/y will be acc to previous val of x divisible by y
#eg:-15//7 ->-3 (-21)
#if y is negative the x/y will be acc to successive val of x divisible by y
#eg:-15//-7 ->2 (14)
#______________________________________________________________________________________
#remainder -> %
print('remainder')
print('15%7->',15%7)#1
print('-15%7->',-15%7)#6
print('15%-7->',15%-7)#-6
print('-15%-7->',-15%-7)#-1
print('reminder of 23 and 7.05 is ->',23%7.05)
print()
#quotient -> //
print('quotient')
print('15//7->',15//7)#2
print('-15//7->',-15//7)#-3
print('15//-7->',15//-7)#-3(-7*-3)
print('-15//-7->',-15//-7)#2
print('quotient of 23.05 and 7 is ->',23.05//7)#3.0
print()
#division -> /
#note x/y=k means y*k=x only simple math. No sign conventions as before
print('division')
print('15/7->',15/7)#2.14...
print('-15/7->',-15/7)#-2.14..
print('15/-7->',15/-7)#-2.14..
print('-15/-7->',-15/-7)#2.14...
print('division of 23.05 and 7 is ->',23.05/7)#3.29...
print()
#power -> **
print('power')
print('power of 23.05 and 2 is ->',23.05**2)#531.3025
print('power of 23 and 1.99 is ->',23**1.99)#512.6705774574998
#4**1.5 is (4^.5)^3 is 2**3
print()
#others
print('addition, subtraction, mutltiplication')
print('23+7->',23+7)#30
print('23-7->',23-7)#16
print('23*7->',23*7)#161
print('with floating points:')
print('23.05+7->',23.05+7)#30.05
print('23.05-7->',23.05-7)#16.05
print('23.05*7->',23.05*7)#161.35
print()