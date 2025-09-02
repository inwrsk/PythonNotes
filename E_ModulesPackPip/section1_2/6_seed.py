from random import random,seed

for i in range(3):
    print(random())#random depends on seed value
#we will get different values for every execution

#by default seed sets with current time
seed(1)

for i in range(3):
    print(random())
'''
0.13436424411240122
0.8474337369372327
0.763774618976614
'''
#same o/p for every execution in any system as we fixed the seed value