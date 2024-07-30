print(isinstance('anwar',str))#True
test_dict = {"apple" : 1, "Ball" : 2 }
print (isinstance(test_dict, dict))#True
class gfg1:
	a = 10
class gfg2():
	string = 'GeeksforGeeks'
obj1 = gfg1()
obj2 = gfg2()
print(str(isinstance(obj1, gfg1)))#True
print(str(isinstance(obj1, gfg2)))#False