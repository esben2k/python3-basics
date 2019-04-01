#functions_return_dictionary.py

def build_book(name, author, publisher):
	"""Create a dictionary of book info"""
	book = {'name':name, 'author':author, 'publisher':publisher}
	return book

my_book = build_book('Ready Player One', 'Unknown Author', 'Virgin Books')
print(my_book)