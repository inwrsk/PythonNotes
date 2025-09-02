data=bytearray(5)
data[0]=ord('a')
data[1]=ord('n')
data[2]=ord('w')
data[3]=ord('a')
data[4]=ord('r')
open('8_file',mode='wb').write(data)
print(open('8_file',mode='rt').read())#anwar