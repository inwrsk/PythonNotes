def func(first_name,seconde_name,age):
    print('hello',first_name+seconde_name,'you are',age)
func(seconde_name=' anwar',first_name='shaik',age=19)#hello shaik anwar you are 19
#in python there are two types of giving arguments POSITIONAL i.e func('anwar','shaik',19)
#another is KEYWORD func(seconde_name=' anwar',first_name='shaik',age=19)

#we can mix these two like 
#KEYWORD followed by POSITIONAL (a,c=d)✔️
#but not POSITIONAL followed by KEYWORD(a=b,c)❌
func('anwar',age=19,seconde_name='shaik')#hello anwarshaik you are 19
#eg:func(seconde_name=' anwar',first_name='shaik',19)-->throws error
