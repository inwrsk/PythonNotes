dic={ 
    (1,2):'value3',
    'key4':{
        "key4.1":'value4.1',
        'key4.2':'value4.2'
    }
} 
for i in dic:
    print(type(i),i)#i is the key type is string or what ever
'''
<class 'tuple'> (1, 2)
<class 'str'> key4
'''
print(dic.items())#dict_items([ ((1, 2), 'value3'), ('key4', {'key4.1': 'value4.1', 'key4.2': 'value4.2'})])
for i in dic.items():
    print(type(i),i) #i is the tuple
'''
<class 'tuple'> ((1, 2), 'value3')
<class 'tuple'> ('key4', {'key4.1': 'value4.1', 'key4.2': 'value4.2'})
'''