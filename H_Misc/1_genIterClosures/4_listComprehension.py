def fun1(n):
    for i in range(n):
        yield i
print(fun1(3))#<generator object fun1 at 0x000001F846944120>
print(list(fun1(3)))#[0,1,2]