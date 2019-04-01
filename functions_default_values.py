#functions_default_values.py

def book_description(author_name, book_type="non-fiction"):

	print("\nThis is a " + book_type + " book.")
	print("The author is " + author_name.title() + ".")

book_description("john doe")	

#override default value
book_description("john doe", book_type="no-nonsense")	