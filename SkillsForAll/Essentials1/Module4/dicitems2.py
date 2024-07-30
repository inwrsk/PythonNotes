dict={'key1':'value1','key2':'value2','key3':{'key3.1':'value3.1','key3.2':'value3.2'}}
print('updating values')
dict['key1']=1
print(dict)#'{key1': 1, 'key2': 'value2', 'key3': {'key3.1': 'value3.1', 'key3.2': 'value3.2'}}
print()
print('adding new items')
dict['newkey']='newvalue'
print(dict)#{'key1': 1, 'key2': 'value2', 'key3': {'key3.1': 'value3.1', 'key3.2': 'value3.2'}, 'newkey': 'newvalue'}
print()
print('adding new or update existing items with update')
dict.update({'key2':2.200})
print(dict)#{'key1': 1, 'key2': 2.2, 'key3': {'key3.1': 'value3.1', 'key3.2': 'value3.2'}, 'newkey': 'newvalue'}
print()
print('deleting items')
del dict['key3']['key3.2']
print(dict)#{'key1': 1, 'key2': 2.2, 'key3': {'key3.1': 'value3.1'}, 'newkey': 'newvalue'}
print()
print('poping the last item')
dict.popitem()
print(dict)#{'key1': 1, 'key2': 2.2, 'key3': {'key3.1': 'value3.1'}}