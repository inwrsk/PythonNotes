dic1={'key1':'value1','key2':{'key2.1':'value2.1','key2.2':'value2.2'}}
print(dic1,len(dic1))#{'key1': 'value1', 'key2': {'key2.1': 'value2.1', 'key2.2': 'value2.2'}} 2
emptydic={}
print(emptydic)#{}
x=dic1.keys()
print(type(x))#<class 'dict_keys'>
print(x)#dict_keys(['key1', 'key2'])
print(type(dic1['key1']))#<class 'str'>
k='key1'
dic2={
    k:'val'
}
print(dic2)#{'key1': 'val'}