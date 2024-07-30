#while converting anything into dict we need to check every item we put should be separated into two parts
colors = (("green", "#008000"), ("blue", "#0000FF"))
dic=dict(colors)
print(dic)#{'green': '#008000', 'blue': '#0000FF'}

# colors = (("green2", "#008000",34), ("blue", "#0000FF"))
#the error occurs as the length of the inside tuples should be 2

#here the error is dict is trying to convert the elements inside the colors key and value, gr has no problem but 008000 does
# colors = ("gr", "#008000")

colors = ("gr", "#0")
dic=dict(colors)
print(dic)#{'g': 'r', '#': '0'}

#similar issue here it wants 2 arguments in the first item
# list1=[34,'an'] 34 can't be split into two \

list1=[[34,45],'an',(True,4.2)]
dic=dict(list1)
print(dic)#{34: 45, 'a': 'n', True: 4.2}