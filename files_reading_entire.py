#files_reading_entire
#read an entire file

with open('movies.txt') as file_object: #	file_object - variable to store file
	contents = file_object.read()#			.read() - get data from file
	print(contents.strip())#				.strip() get rid of white space on either side of lines

