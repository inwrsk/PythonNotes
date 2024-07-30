dict={'key1':'value1','key2':'value2','key3':{'key3.1':'value3.1','key3.2':'value3.2'}}
# print(dict.popitem('key1'))
# print(dict)
#error-> popitem takes no arguments
print(dict.pop('key1'))
print(dict)
print(dict.popitem())
print(dict)