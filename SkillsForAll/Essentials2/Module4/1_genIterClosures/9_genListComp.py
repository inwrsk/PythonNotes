for v in [print('lst') or x for x in range(3)]:
    print(v, end=" ")
print()
'''
lst
lst
lst
0 1 2
'''
#for loop is initiated once all the list is completed
for v in (print('gen') or x for x in range(3)):
    print(v, end=" ")
print()
'''
gen
0 gen
1 gen
2 
'''
#loop is initiated even if generator is not complete