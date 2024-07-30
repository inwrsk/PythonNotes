stack=[]
def push(val):
    stack.append(val)
def pop():
    val=stack[-1]
    del stack[-1]
    return val
push(1)
push(2)
print(pop())#2
#having stack like this won't assure your data privacy in stack by using objects we can do it
