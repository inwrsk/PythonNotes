#i,j=3,not i #error name error maybe
i=3
j=not i
print(i,j)#3 false
#i is default true so j will be false
p,q=None,None
print(not(p))#True
print(q)#None
print(not(p and q) is (p and not(q)))#False (True is False)
print(True is True)#true
print(False or 'anwar')#'anwar'
print(True is 'anwar')#False
print(0&1)#0
print(0|1)#1
print(5^1)#101^001=100
print(~5)#-6
#step:1->represent 5 in binary form 0000 0101 here i took 8 bit representation actually it is 
#32 and 64 bits according to the system
#step:2->invert all values i.e 1's complement 1111 1010 and it is the req number 
#to find the negative integer's magnitude do two's complements follows as
#left most index represents sign of the bit
#invert the bits 0000 0101
#add 1->00000110
#which is 6
print(~0)#-1