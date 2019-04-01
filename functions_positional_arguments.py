#functions_positional_arguments.py

# Creating our function
def book_description(book_type, author_name):
	"""Display book information"""
	print("\nThis book is " + book_type + ".")
	print("The author of this book is " + author_name.title() + ".")


book_description("rectangular","Leonardo da Vinci")
book_description("fiction","Dan Brown")

