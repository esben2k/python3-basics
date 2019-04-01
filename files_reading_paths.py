#files_reading_entire
#read an entire file

filepath = "C:\\Users\\Esben\\Python\\Python3_Skillshare\\text_files\\copy_of_movies.txt"

with open('text_files\\copy_of_movies.txt') as file_object: #	file_object - variable to store file
	contents = file_object.read()#			.read() - get data from file
	print(contents.strip())#				.strip() get rid of white space on either side of lines

print(filepath)