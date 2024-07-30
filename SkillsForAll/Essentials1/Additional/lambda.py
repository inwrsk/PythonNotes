import time
print(list(map(lambda x:x*2,range(5))))#[0, 2, 4, 6, 8]
#in map(x,y) it takes y and convert to x and returns object
print(list(map(lambda x:time.sleep(0.01) , range(4))))#[None, None, None, None] after .04 secs
s=lambda x,y:(
    x**2+y**2
    )
#or lambda x,y:x**2 + y**2 jst to represent that we can go multiline
print(s(3,4))#25
#lambda is a small throwaway function instead of declaring a function