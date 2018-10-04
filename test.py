import json

l = ['a', 'b']
h = ['1', '2']
o = json.dumps({'l': l, 'h': h})
print(o)
