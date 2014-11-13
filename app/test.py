import json

data1 = { 'obj1' : 'obj1', 'obj2' : 'obj2' }

data2 = { 'xbj1' : 'xbj1', 'xbj2' : 'xbj2' }

#data = [ data1, data2 ]
data = []
data.append(data1)
data.append(data2)
print json.dumps( data )
