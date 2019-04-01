#files_making_list_from_file.py
#retain access to file contents by storing in list

filename = "movies.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())

print("\n------------------------------------------\n")

popped_movies = lines.pop()

for line in lines:
	print(line.strip())

print("\n------------------------------------------\n")

sorted_list = lines.sort()
for line in lines:
	print(line.strip())