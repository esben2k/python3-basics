#slicing_a_list.py

names = ['tony', 'deirdre', 'senan', 'carol']
print (names[0:2])

print (names[1:3])

print(names[:3])

print(names[2:])

#last 3 names
print(names[-3:])


#looping through slice with a for
names = ['tony', 'deirdre', 'senan', 'carol']
print("Here are the names of the last 3 registrations.")
for name in names[:3]:
	print(name.title())



#copying a list
names = ['tony', 'deirdre', 'senan', 'carol']
first_names = names[:]
print(first_names)