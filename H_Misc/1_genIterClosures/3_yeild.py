def fun1(n):
    for i in range(n):
        yield i
def fun11(n):
    for i in range(n):
        return i
print(fun1(3))#<generator object fun1 at 0x000001E969145CB0>
for i in fun1(3):
    print(i)
'''
0
1
2
'''
y=fun1(4)
for i in y:
    if i<2:
        print(i,end=' ')#0 1
print()
for i in y:#no output willbe printed as the generator will work only once which is already done in above loop
    print('sfd')
    print(i,end=' ')
print()
print(fun11(3))#0
print(fun11(3))#0

def fun1(n):
    yield 'anwar'
    for i in range(n):
        yield i
print(list(fun1(2)))#['anwar', 0, 1]
for i in fun1(2):
    print(i)
'''
anwar
0
1
'''