x=open('8_file',mode='rb')
print(x.read())#b'anwar'
x.seek(0)
data1=''
# print(x.readinto(data1))# TypeError
data2=bytearray(4)
print(x.readinto(data2))#4
x.seek(0)
print(data2,x.read())#bytearray(b'anwa') b'anwar'