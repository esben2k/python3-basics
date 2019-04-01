class Ereader():
	"""A class to define an ereader"""

	def __init__(self, make, model, backlight, battery, screen_type):
		"""Initialize the attributes to describe an ereader"""
		self.make = make
		self.model = model
		self.backlight = backlight
		self.battery = battery
		self.screen_type = screen_type
		#define new parameter with default value
		self.library_count = 0

	def get_ereader_name(self):
		"""Return a formatted description for ereader"""
		long_name = self.make + " - " + self.model + " - " + self.backlight + " - " + self.battery + " - " + self.screen_type
		return long_name.title()

	def read_library_count(self):
		"""Show the number of ebooks in our library"""
		print("You have " + str(self.library_count) + " books in your library.")

	def update_library_count(self, ebook_count):
		"""Set the library count"""
		self.library_count = ebook_count

	def increment_library_count(self, purchased_ebooks):
		"""Add our new ebooks to our library count"""
		self.library_count += purchased_ebooks

#Child class. PArent class must exist in the same module/file

class Screen():

	def __init__(self, screen_resolution = '1280 * 800'):
		self.screen_resolution = screen_resolution

	def define_screen(self):
		"""print out marketing stuff about kidnle fire"""
		print("Fire HD 8 features a widescreen " + self.screen_resolution + ".")


class KindleFire(Ereader): #inherits from class Ereader
	"""Represents aspects of an ereader specific to a kindle fire
		Then initialize attributes specific to a kile fire"""

	def __init__(self, make, model, backlight, battery, screen_type):
		"""initialize attributes for the kindle fire"""
		
		#calling the init from the parent class
		super().__init__(make,model,backlight,battery,screen_type)
		self.firescreen = Screen()