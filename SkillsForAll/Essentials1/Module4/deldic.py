dic={
    'key1':'value1',
    'key1':'value2',    
    'key1':'value1'
}
print(dic)#{'key1': 'value1'}
#observe print statement it removes the duplicates and the last will be the final
del dic['key1']
print(dic)#{}