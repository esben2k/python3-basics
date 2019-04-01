#dictionaries2.py
#create a dictionary of terms

terms = {'variable' : 'represents or refers to a value stored in memory', 'string' : 'A sequence of characters'}

if 'float' in terms:
	print("I know what a float is")
else:
	print("I do not know what that is")


print(terms['variable'])

new_terms = {}
new_terms['variable'] = 'Represents to a value stored in memory'
new_terms['integer'] = 'A whole number'

print(new_terms['variable'])
print(new_terms['integer'])
