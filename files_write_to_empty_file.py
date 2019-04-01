#files_write_to_empty_file.py

filename = 'programming.txt'

with open(filename, 'a') as file_object:# a = append, w = write, r = read modes
	file_object.write("Hello, this is a test")

#if writing numbers, convert to string before writing to file.