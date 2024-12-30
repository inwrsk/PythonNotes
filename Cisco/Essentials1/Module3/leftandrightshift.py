var = -0b110
print(var,type(var))#-6 <class 'int'>
var_right = var >> 1
var_left = var << 2
print(var_left,var, var_right)#-24 -6 -3
print(var>>4)#-1 which is  1111111 last one is value and remaining first one is sign