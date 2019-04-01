#get_method.py

terms = {'integer':"A wrong statement", 'string' : 'A sequence of chars'}

print(terms.get('integer'))
print(terms.get('float', 'Not found'))


print(terms)

del terms['integer']

print(terms)
