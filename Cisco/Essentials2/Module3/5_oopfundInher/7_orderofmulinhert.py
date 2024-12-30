class Left:
    var = "L"
    var_left = "LL"

class Right:
    var = "R"
    var_right = "RR"

class Sub(Left, Right):#left superclass is more preferred
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right)#L LL RR