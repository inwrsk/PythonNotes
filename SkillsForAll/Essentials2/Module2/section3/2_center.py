x='a'.center(1)
y='a'.center(2,'_')
print('|'+x+'|')#|a|
print('|'+y+'|')#|a_|
x='a'.center(3)
y='a'.center(4,'_')#_a__
print('|'+x+'|')#| a |
print('|'+y+'|')
#takes the width we give and centers the string within that and adds the string you give
#or ' ' by default on both the sides to center it
print('center'.center(4,'-'))#center
#as we can't fit center in 4 chars