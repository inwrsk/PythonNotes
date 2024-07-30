beatles=[]
#appending
beatles.append('firstbeatle')
beatles.append('secondbeatle')
beatles.append('thirdbeatle')
del beatles[-1]
print(beatles)#['firstbeatle', 'secondbeatle']
#inserting to first place
beatles.insert(0,'first insertion')#['first insertion', 'firstbeatle', 'secondbeatle']
beatles.insert(1,'second insertion')#['first insertion','second insertion', 'firstbeatle', 'secondbeatle']
del beatles[2]
print(beatles)#['first insertion','second insertion', 'secondbeatle']
#list length
print(len(beatles))#3