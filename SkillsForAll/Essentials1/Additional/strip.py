text='###---Data---#'
x=text.strip('##')
print(x)#---Data---
x=text.strip('#-#')
print(x)#Data
x=text.strip('#a-')
print(x)#Dat
x=text.rstrip('a-')
print(x)####---Data---#
x=text.lstrip('#--#')
print(x)#Data---#
text=' ###---Data---#    '
x=text.strip()
print(x)####---Data---#
#it takes the input chars and remove at the ends of the string upto other char