#functions_passing_list.py

def books_available(*books):
	"""show a list of available books"""
	for book in books:
		books_in_stock = "The following title is available to buy " + book.title() + "."
		print(books_in_stock)

#comment to use as module (module_importing)
#available = ['elon musk', 'little book', 'big book']
#books_available(available)

def book_description(author_name, book_type="non-fiction"):
	print(book_type + ", " +author_name)