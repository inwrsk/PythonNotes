text = "Hello World, This string, is used to get clarified about split"
result = text.split()
print(result)#['Hello', 'World,', 'This', 'string,', 'is', 'used', 'to', 'get', 'clarified', 'about', 'split']
result=text.split('is')
print(result)#['Hello World, Th', ' string, ', ' used to get clarified about split']
result=text.split(maxsplit=3)
print(result)#['Hello', 'World,', 'This', 'string, is used to get clarified about split']
result=text.split('  ')
print(result)#['Hello World, This string, is used to get clarified about split']
text = "Hello World, This string, is used, ,to ge,t, clarified about split"
result=text.split(" ",maxsplit=3)
print(result)#['Hello', 'World,', 'This', 'string, is used, ,to ge,t, clarified about split']