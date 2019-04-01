#dictionaries4.py
#looping through dictionaries

birthday_months = {
'john':'april', 
'june':'april', 
'bob':'november'
}

#for key, value in birthday_months.items():
#	print("\nName: " + key)
#	print("\nMonth: " + value)

#looping through pairs
book_1 = {
	'name':'elon musk',
	'author':'ashlee vance',
	'price':'14.99',
	'publisher':'virgin books'
}

#for key, value in book_1.items():
#	print("\nKey " + key)
#	print("\nValue " + value)

for name in birthday_months.keys():
	print(name.title())

for months in birthday_months.values():
	print(months.title())

for months in set(birthday_months.values()):
	print(months.title())