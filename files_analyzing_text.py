#files_analyzing_text.py

def word_count(filename):
	"""Count number of words in a file with utf-8 encoding"""
	try:
		with open(filename, encoding="utf8") as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		message = "Sorry the file " + filename + " cannot be found."
		print(message)
	else:
		words = contents.split()
		number_words = len(words)
		print("The file " + filename + " has " + str(number_words) + " words")

word_count("pride_and_prejudice.txt")