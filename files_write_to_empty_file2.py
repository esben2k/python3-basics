
message = input("What is your favorite book?")
print(message.title())

filename = 'favorite_film.txt'

with open(filename, 'a') as file_object:
	file_object.write(message + "\n")