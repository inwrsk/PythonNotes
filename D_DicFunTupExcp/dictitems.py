dict={'key1':'value1','key2':'value2','key3':{'key3.1':'value3.1','key3.2':'value3.2'}}
y=dict.items()
print(type(y))#<class 'dict_items'>
print(y)#dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', {'key3.1': 'value3.1', 'key3.2': 'value3.2'})])
for i,j in y:
    print(i,'->',j)
'''
key1 -> value1
key2 -> value2
key3 -> {'key3.1': 'value3.1', 'key3.2': 'value3.2'}
'''