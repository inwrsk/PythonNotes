print(' '.join('anwar'))#a n w a r
#join takes all the strings in the object or string or what ever char and combines them with the string we give
print(''.join(reversed('anwar')))#rawna
x=reversed([1,2,3])
print(x,type(x))#x is a object or class
#print(''.join(x))#type error #int type instead of strings
x=['1','2','anwar']
print('-'.join(reversed(x)))#anwar-2-1
s='12345'
s=s[::-1]
print(s)#54321
#s[0]='a'#strings are immutable
#s[1:4]=s[3:0:-1]#you can't change the string
#instead you can do this
s='a'+s[1:]
print(s)#a4321
s='12345'
s=s[:1]+s[3:0:-1]+s[4:]#reversing specific part 234
print(s)#14325