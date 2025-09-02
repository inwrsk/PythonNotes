l1=['anwar',23,True]
l2=['sf',False,'ret',[5.32]]
l3=l1+l2
print(l3)#['anwar', 23, True, 'sf', False, 'ret', [5.32]]
l4=[*l1,*l2]
print(l4)#['anwar', 23, True, 'sf', False, 'ret', [5.32]]