t = 'thetath5th'
print(t.find('eta'))#2
print(t.find(''))#0
print(t.find('th'))#0
print(t.find('th',1))#5 #searches in string[1:]
print(t.find('th',3,6))#-1 #no th in string[3:6] i.e tat
print(t.find('haaa'))#-1

#same as index
#but works with only strings and returns -1 if it finds nothing
