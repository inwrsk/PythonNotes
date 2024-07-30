tup=(23,45,78.3,True)
print(id(tup))#2601538340480
del tup
#print(tup) #shoots the error as the tup not exist any more
newtup=(23,45,78.3,True)#2601538340480
print(id(newtup))