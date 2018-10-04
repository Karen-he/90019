import json

l = ['a', 'b']
h = ['1', '2']
o = json.dumps({'l': l, 'h': h})
print(o)

hs = {'a': 1, 'b':2}
print(hs['a'].bit_length())

doc = json.loads(o)
for i in ['h', 'l']:
    if len(doc[i]) > 0:
        print(len(doc[i]))
