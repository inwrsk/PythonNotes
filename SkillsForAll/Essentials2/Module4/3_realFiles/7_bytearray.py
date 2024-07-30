data=bytearray(5)
print(data,len(data))#bytearray(b'\x00\x00\x00\x00\x00') 5
#these are hexadecimal values 00 to ff i.e upto 255
print(data[1])#0
# data[1]='s'#TypeError
data[1]=30
print(data)#1e
#(30)10 = (1E)16 i.e hex(30) is 1e
data[2]=0xff
print(data)#bytearray(b'\x00\x1e\xff\x00\x00')
#data[3]=256#ValueError: byte must be in range(0, 256)