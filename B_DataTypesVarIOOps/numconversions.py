#binary in decimal
print('0b111->',0b111)#7
#hexadecimal in decimal
print('0x123->',0x123)#291
print('0o123+0x123->',0o123+0x123)#374
#even when adding two different types, result will be in decimal
x="101"
#oct,bin,hex to decimal
print(int(x,2))#5#imagines that x is a binary number
print(int(x,8))#65#x is a octal number
print(int(x,10))#101#x as a decimal number
print(int(x,16))#257#x as a hexadecimal number
#decimal to oct,hex,bin
print('oct(8),hex(10),bin(3)',oct(8),hex(10),bin(3))
#type
print(type(0b110))#int
print(type(bin(10)))#str