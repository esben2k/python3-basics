#files_reading_line_by_line.txt

filename = "movies.txt"

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())
