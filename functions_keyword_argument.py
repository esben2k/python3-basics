#functions_keyword_argument.py

# Create a function
def book_description(book_type, author):
	"""Display book information"""

	print("\nThis is a " + book_type + " book.")
	print("The author is " + author + ".")

book_description(book_type="non-fiction", author="Brad Stone")	
