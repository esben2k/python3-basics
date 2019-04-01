#class_creating


class Book(): #Capitalized names refers to classes
	"""A class to create a book"""

	#functions that are part of a class is a method
	
	#always init first in a class
	def __init__(self, name, price, publisher):
		"""Initialize the name etc."""

		#these variables are available to all the functions inside class.
		self.name = name
		self.price = price
		self.publisher = publisher

	def hardback(self):
		"""Simulate a hardback book"""
		print(self.name.title() + " is a hardback book")

	def softback(self):
		"""Simulate a softback book"""
		print(self.name.title() + " is a softback book")

	def ebook(self):
		"""Simulate an ebook"""
		print(self.name.title() + " is an ebook")

	def ebook_reader(self):
		"""Simulate an ebook reader"""
		print("Library: " + self.name.title() + ", $" + str(self.price) + ", " +self.publisher.title() + ".")


# Creating new books - creating an instance of our book class
my_book = Book('the odyssey', 15.99, 'epic books')
your_book = Book('the illiad', 9.56, 'epic books')

#Accessing attributes
#print("I am currently reading " + my_book.name.title() + ".")
#print("This book cost $" + str(my_book.price) + ".")

#Calling ebook reader method
my_book.ebook_reader()
your_book.hardback()