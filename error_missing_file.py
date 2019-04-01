#error_missing_file.py

filename = "esben.txt"

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	message = "Sorry, the file " + filename + " was not found"
	print(message)