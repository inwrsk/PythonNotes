def funcOut():
    def funcIn():
        return "funcInFunc"
    return funcIn
x=funcOut()
print(x())#funcInFunc